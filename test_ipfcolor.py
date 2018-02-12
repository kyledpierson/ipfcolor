from ipfcolor import Generator


def test_rgb():
    generator = Generator()
    rgb = generator.generate_ipf_color(
        phi1=30, phi=30, phi2=30, ref_dir_0=1, ref_dir_1=1, ref_dir_2=1, deg_to_rad=True)

    assert (rgb == 4288282412)  # Not sure if this is even right
