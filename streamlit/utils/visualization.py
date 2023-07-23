import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import seaborn as sns
import numpy as np

from dataclasses import dataclass
from .logger import get_logger
from .common import check_and_create_dir


LOGGER = get_logger("utils/visualization")


@dataclass
class Padding:
    tpad: float = 2.5
    lpad: float = 0.1
    bpad: float = 0.12


@dataclass
class Labels:
    title: str = ""
    xlabel: str = ""
    ylabel: str = ""
    zlabel: str = ""


def initialize_plot(nrows=1, ncols=1, figsize=(10, 6), labels=Labels(), padding=Padding(), fontsize=12):
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
    fig.tight_layout(pad=padding.tpad)
    fig.subplots_adjust(left=padding.lpad, bottom=padding.bpad)
    fig.suptitle(labels.title, fontsize=fontsize)
    fig.text(x=0.04, y=0.5, s=labels.ylabel, fontsize=fontsize, rotation="vertical", verticalalignment="center")
    fig.text(x=0.5, y=0.04, s=labels.xlabel, fontsize=fontsize, horizontalalignment="center")
    return fig, axes


def savefig_and_close(filename: str, output_dir=None, close=True) -> None:
    if output_dir:
        check_and_create_dir(output_dir)
        savepath = f"{output_dir}/{filename}"
        plt.savefig(savepath, facecolor="w")
        LOGGER.info(f"Saved plot at {savepath}.")
    if close:
        plt.close()


def plot_klines(klines: pd.DataFrame, target: str, output_dir=None, close=True) -> None:
    LOGGER.info(f"Plotting kine of {target}...")
    labels = Labels(target)
    fig, ax = initialize_plot(labels=labels)
    mpf.plot(data=klines, type="candle", show_nontrading=True, ax=ax)
    savefig_and_close(f"{target}_klines.png", output_dir, close)
    return fig
