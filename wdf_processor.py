from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from renishawWiRE import WDFReader
import numpy as np
from scipy.interpolate import interp1d
from tqdm import tqdm
from PIL import Image
import matplotlib.pyplot as plt

class SafeWDFReader(WDFReader):
    def _parse_wmap(self, *args, **kwargs):
        pass

def load_wdf_files(target_length=1015, truncate_range=None):
    Tk().withdraw()
    file_paths = askopenfilenames(title="Select WDF Files", filetypes=[("WDF Files", "*.wdf")])
    if not file_paths:
        print("No files selected. Exiting...")
        return None, None, None

    all_spectra = []
    all_readers = []

    for file in tqdm(file_paths, desc="Processing Files"):
        try:
            reader = SafeWDFReader(file)
            all_readers.append(reader)
            wavenumber = reader.xdata
            spectra = reader.spectra

            if truncate_range is not None:
                mask = (wavenumber >= truncate_range[0]) & (wavenumber <= truncate_range[1])
                wavenumber = wavenumber[mask]
                spectra = spectra[:, mask] if spectra.ndim > 1 else spectra[mask]

            if spectra.ndim == 1:
                spectra = spectra.reshape(1, -1)

            if spectra.shape[1] != target_length:
                interp_func = interp1d(wavenumber, spectra, kind='linear', axis=1, fill_value="extrapolate")
                new_wavenumber = np.linspace(wavenumber.min(), wavenumber.max(), target_length)
                spectra = interp_func(new_wavenumber)
                wavenumber = new_wavenumber

            all_spectra.append(spectra)

        except Exception as e:
            print(f"Error processing file {file}: {e}")
            continue

    try:
        all_spectra = np.vstack(all_spectra)
    except ValueError:
        print("Error: Inconsistent spectrum lengths. Please check the input files.")
        return None, None, None

    map_spec = all_spectra.T
    return wavenumber, map_spec, all_readers

def plot_spectra(wavenumber, map_spec):
    if wavenumber is None or map_spec is None:
        print("No data to plot.")
        return

    plt.figure(figsize=(12, 6))
    for i in range(map_spec.shape[1]):
        plt.plot(wavenumber, map_spec[:, i], alpha=0.5)

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.xlabel("Wavenumber (cm⁻¹)")
    plt.ylabel("Intensity")
    plt.title("Spectral Data")
    plt.show()

def plot_white_light_image(reader, scale_bar_length_microns=20):
    if hasattr(reader, 'img') and reader.img is not None:
        image = Image.open(reader.img)
        img_x0, img_y0 = reader.img_origins
        img_w, img_h = reader.img_dimensions

        scale_per_pixel = img_w / image.size[0]
        scale_bar_length_pixels = scale_bar_length_microns / scale_per_pixel

        x_bar_start = image.size[0] * 0.1
        y_bar_start = image.size[1] * 0.9
        x_bar_end = x_bar_start + scale_bar_length_pixels

        plt.figure(figsize=(9.4, 6))
        plt.imshow(image, cmap='gray')
        plt.plot([x_bar_start, x_bar_end], [y_bar_start, y_bar_start], color='white', linewidth=2)
        plt.text((x_bar_start + x_bar_end) / 2, y_bar_start - 10,
                 f'{scale_bar_length_microns} µm', color='white', fontsize=12, ha='center')
        plt.axis('off')
        plt.gca().set_position([0, 0, 1, 1])
        plt.title("White Light Image with Scale Bar")
        plt.savefig("white_light_image_with_scalebar.png", bbox_inches='tight', pad_inches=0)
        plt.show()

        return {
            "image": image,
            "scale_bar_coords": (x_bar_start, y_bar_start, x_bar_end, y_bar_start),
            "scale_bar_length_microns": scale_bar_length_microns,
            "scale_per_pixel": scale_per_pixel,
            "image_dimensions": image.size,
        }
    else:
        print("No white light image available.")
        return None

if __name__ == "__main__":
    truncate_range = (100, 2000)
    wavenumber, map_spec, readers = load_wdf_files(truncate_range=truncate_range)
    if wavenumber is not None and map_spec is not None:
        plot_spectra(wavenumber, map_spec)
        if readers:
            plot_white_light_image(readers[0])
