import xarray
from matplotlib.pyplot import figure


def timeprofile(iono: xarray.Dataset, Nplot: int = 4):
    # %% Plots

    if Nplot > 2:
        fig = figure(figsize=(16, 12))
        axs = fig.subplots(Nplot, 1, sharex=True).ravel()
    else:
        fig = figure(figsize=(16, 6))
        axs = fig.subplots(1, 2).ravel()

    fig.suptitle(
        f"{str(iono.time[0].values)[:-13]} to "
        f"{str(iono.time[-1].values)[:-13]}\n"
        f"Glat, Glon: {iono.glat.item()}, {iono.glon.item()}"
    )

    ax = axs[0]

    ax.plot(iono.time, iono["NmF2"], label="N$_m$F$_2$")
    ax.plot(iono.time, iono["NmF1"], label="N$_m$F$_1$")
    ax.plot(iono.time, iono["NmE"], label="N$_m$E")
    ax.set_title("Maximum number densities vs. ionospheric layer")
    ax.set_xlabel("Hour (UT)")
    ax.set_ylabel("(m$^{-3}$)")
    ax.set_yscale("log")
    ax.legend(loc="best")

    ax = axs[1]
    ax.plot(iono.time, iono["hmF2"], label="h$_m$F$_2$")
    ax.plot(iono.time, iono["hmF1"], label="h$_m$F$_1$")
    ax.plot(iono.time, iono["hmE"], label="h$_m$E")
    ax.set_title("Height of maximum density vs. ionospheric layer")
    ax.set_xlabel("Hour (UT)")
    ax.set_ylabel("(km)")
    ax.legend(loc="best")
    # %%
    if Nplot > 2:
        ax = axs[2]

        for a in iono.alt_km:
            ax.plot(iono.time, iono["ne"].sel(alt_km=a), marker=".", label=f"{a.item()} km")
        ax.set_xlabel("time UTC (hours)")
        ax.set_ylabel("[m$^{-3}$]")
        ax.set_title(f"$N_e$ vs. altitude and time")
        ax.set_yscale("log")
        ax.legend(loc="best")
    # %%
    if Nplot > 3:
        ax = axs[3]
        ax.plot(iono.time, iono["TEC"], label="TEC")
        ax.set_xlabel("Hour (UT)")
        ax.set_ylabel("(m$^{-2}$)")
        # ax.set_yscale('log')
        ax.legend(loc="best")
    if Nplot > 4:
        ax = axs[4]
        ax.plot(iono.time, iono["EqVertIonDrift"], label=r"V$_y$")
        ax.set_xlabel("Hour (UT)")
        ax.set_ylabel("(m/s)")
        ax.legend(loc="best")

    for a in axs.ravel():
        a.grid(True)


def altprofile(iono: xarray.Dataset):
    fig = figure(figsize=(16, 6))
    axs = fig.subplots(1, 2)

    fig.suptitle(
        f"{str(iono.time[0].values)[:-13]}\n" f"Glat, Glon: {iono.glat.item()}, {iono.glon.item()}"
    )

    pn = axs[0]
    pn.plot(iono["ne"], iono.alt_km, label="N$_e$")
    # pn.set_title(iri2016Obj.title1)
    pn.set_xlabel("Density (m$^{-3}$)")
    pn.set_ylabel("Altitude (km)")
    pn.set_xscale("log")
    pn.legend(loc="best")
    pn.grid(True)

    pn = axs[1]
    pn.plot(iono["Ti"], iono.alt_km, label="T$_i$")
    pn.plot(iono["Te"], iono.alt_km, label="T$_e$")
    # pn.set_title(iri2016Obj.title2)
    pn.set_xlabel("Temperature (K)")
    pn.set_ylabel("Altitude (km)")
    pn.legend(loc="best")
    pn.grid(True)


def latprofile(iono: xarray.Dataset):

    fig = figure(figsize=(8, 12))
    axs = fig.subplots(2, 1, sharex=True)

    ax = axs[0]

    ax.plot(iono["glat"], iono["NmF2"], label="N$_m$F$_2$")
    ax.plot(iono["glat"], iono["NmF1"], label="N$_m$F$_1$")
    ax.plot(iono["glat"], iono["NmE"], label="N$_m$E")
    ax.set_title(str(iono.time[0].values)[:-13] + f'  latitude {iono["glat"][[0, -1]].values}')
    # ax.set_xlim(iono.lat[[0, -1]])
    ax.set_xlabel(r"Geog. Lat. ($^\circ$)")
    ax.set_ylabel("(m$^{-3}$)")
    ax.set_yscale("log")

    ax = axs[1]
    ax.plot(iono["glat"], iono["hmF2"], label="h$_m$F$_2$")
    ax.plot(iono["glat"], iono["hmF1"], label="h$_m$F$_1$")
    ax.plot(iono["glat"], iono["hmE"], label="h$_m$E")
    ax.set_xlim(iono["glat"][[0, -1]])
    ax.set_title(str(iono.time[0].values)[:-13] + f'  latitude  {iono["glat"][[0, -1]].values}')
    ax.set_xlabel(r"Geog. Lat. ($^\circ$)")
    ax.set_ylabel("(km)")

    for a in axs:
        a.legend(loc="best")
        a.grid(True)
