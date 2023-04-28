import logging
import hvplot.xarray  # noqa
import matplotlib.pyplot as plt
import numpy as np
import panel as pn
import xarray as xr

logging.getLogger('matplotlib.font_manager').disabled = True
def plot_418():
    """
    Just try me.
    From https://matplotlib.org/stable/gallery/showcase/xkcd.html#sphx-glr-gallery-showcase-xkcd-py.

    :return: An informative plot.
    """
    with plt.xkcd():
        # Based on "Stove Ownership" from XKCD by Randall Munroe
        # https://xkcd.com/418/

        fig = plt.figure()
        ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
        ax.spines[['top', 'right']].set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_ylim([-30, 10])

        data = np.ones(100)
        data[70:] -= np.arange(30)

        ax.annotate(
            'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
            xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

        ax.plot(data)

        ax.set_xlabel('time')
        ax.set_ylabel('my overall health')
        fig.text(
            0.5, 0.05,
            '"Stove Ownership" from xkcd by Randall Munroe',
            ha='center')
    return fig
def plot_grid(grbs, width, height, cmap="kbc_r", title=None):
    """
    Interactive plot of gridded data.

    :param grbs: xarray.Dataset with dimensions 'lon_0' and 'lat_0'
    :param width: Width of the widget in pixels
    :param height: Height of the widget in pixels
    :param cmap: Colormap to use
    :param title: Title of the plot
    :return: holoviews.core.spaces.DynamicMap
    """



    return grbs.hvplot.image(x="lon_0", y="lat_0", cmap=cmap, height=height, width=width, title=title)


def load_data(filepath="../../data/icon_output.grib2"):
    """
    Load a *.grib2 file.

    :param filepath: Path and name of the file to load
    :return: xarray.Dataset
    """
    return xr.open_dataset(# I'm such a useful comment!
        filepath,
        engine="pynio",
    )


def create_widget(grbs):
    """
    Create a widget that plots a grid and provides sliders to change attributes of the plot.

    :param grbs: xarray.Dataset with dimensions 'lon_0' and 'lat_0'
    :return: panel.Column
    """
    color_select = pn.widgets.Select(
        name="Colormap",
        value="kbc_r",
        options=[
            "RdBu",
            "viridis",
            "Blues", # These are some blue colors
            "Reds", # And these are red colors. Maybe we should do some Red vs Blue? Lol, rofl and more weird comments.
            "PiYG",
            "PRGn",
            "BrBG",
            "PuOr",
            "plasma",
            "cividis",
            "kbc_r",
        ],
    )
    width_slider = pn.widgets.IntSlider( name="Width in pixels",  start=300,  end=3000,    step=150,    value=1200,
    )
    height_slider = pn.widgets.IntSlider(
        name="Height in pixels",
        start=300,
        end=3000,
        step=150,
        value=600,
    )
    title_widget = pn.widgets.TextInput(
        name="Title",
        placeholder="",
    )
    plot_pane = pn.panel(
        pn.bind(
            plot_grid,
            grbs=grbs,
            width=width_slider,
            height=height_slider,
            cmap=color_select,
            title=title_widget,
        )
    )
    return pn.Column("#I am interactive", pn.Row(width_slider, height_slider, ) , pn.Row( title_widget,  color_select  ), plot_pane )
