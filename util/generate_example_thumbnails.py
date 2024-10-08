from pathlib import Path
from itertools import chain

from PIL import Image


def main():
    input_path = Path('example_code/images')
    output_path = Path('example_code/images/thumbs/')

    png_input_files = input_path.glob('*.png')
    gif_input_files = input_path.glob('*.gif')

    modified_files = []

    for input_file in chain(png_input_files, gif_input_files):
        if out_of_date(input_file, output_path):
            modified_files.append(input_file)

    generate_thumbnails(modified_files, output_path)


def out_of_date(input_file, output_path):
    """Check if the thumbnail is out of date."""
    output_file = output_path / input_file.name

    if not output_file.exists():
        return True

    if input_file.stat().st_mtime > output_file.stat().st_mtime:
        return True
    else:
        return False


def generate_thumbnails(input_files, output_path):
    """Generate thumbnails for the input files."""
    size = 200, 158

    output_path.mkdir(exist_ok=True)

    for input_file in input_files:
        print('Generating thumbnail: ' + input_file.name)
        im = Image.open(input_file)
        im.thumbnail(size)
        im.save(output_path / input_file.name)
    print("Done generating thumbnails.")


if __name__ == '__main__':
    main()
