from PIL import Image
import colorsys

def make_red_icon(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    pixels = img.getdata()
    new_pixels = []

    for pixel in pixels:
        r, g, b, a = pixel

        # Preserve transparency
        if a == 0:
            new_pixels.append((r, g, b, a))
            continue

        # Check if pixel is "white-ish" → keep it as is
        if r > 200 and g > 200 and b > 200:
            new_pixels.append((r, g, b, a))
            continue

        # Convert RGB to HSV for hue shifting
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        # Shift hue from blue (~0.55) to red (~0.0)
        h = (h - 0.55) % 1.0   # move blue base to ~0
        s = min(1, s * 1.2)    # boost saturation a bit
        v = min(1, v * 1.0)    # keep brightness

        # Convert back to RGB
        r2, g2, b2 = colorsys.hsv_to_rgb(h, s, v)
        new_pixels.append((int(r2*255), int(g2*255), int(b2*255), a))

    # Save red icon
    img.putdata(new_pixels)
    img.save(output_path, "PNG")
    print(f"Red icon saved to {output_path}")

# Example usage
make_red_icon("C:\Memphis Map\Leaflet Map\marker-icon-2x.png", "marker-icon-red.png")
