from dash import html


def gen_CHAMP_data():
    return html.Div([
        html.H1("CHAMP Description", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            The CHAMP (CHAllenging Mini satellite Payload; Reigber et al., 1996) satellite was in a
            near-polar and circular orbit from 2000 to 2010. The data covers the altitude range from
            initially 460 km to 260 km, though most data is collected above 320 km altitude.
            """
        ),
        html.H2("Data Source", style={"font-size": "20px", "font-weight": "bold"}),
        html.P([
            "TU Delft (",
            html.A("ftp://thermosphere.tudelft.nl", href="ftp://thermosphere.tudelft.nl", target="_blank"), 
            "); PI: Christian Siemes, ",
            html.A("c.siemes@tudelft.nl", href="mailto:c.siemes@tudelft.nl", target="_blank")
        ]),
        html.H2("Density Retrieval Method", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Accelerometer-inferred"),
        html.H2("Data Version", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Version_02"),
        html.H2("More Information", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(html.A("https://earth.esa.int/eogateway", href="https://earth.esa.int/eogateway", target="_blank")),
        html.P(html.A("http://thermosphere.tudelft.nl/", href="http://thermosphere.tudelft.nl/", target="_blank"))
    ], className="data-source-metadata")


def gen_GOCE_data():
    return html.Div([
        html.H1("GOCE Description", style={"font-size": "20px", "font-weight": "bold"}),
        html.P([
            "GOCE (Gravity field and steady-state Ocean Circulation Explorer; ", 
            html.A("Drinkwater et al., 2003", href="https://doi.org/10.1023/A:1026104216284", target="_blank"),
            """
            ) was launched on 17 March 2009 in a 96.5° inclination, dawn-dusk orbit, and re-
            entered the atmosphere on 11 November 2013. The orbit was maintained at 255 km
            mean altitude for the largest part of the mission, and then it was lowered in four stages
            ultimately to 224 km in May 2013.
            """
        ]),
        html.H2("Data Source", style={"font-size": "20px", "font-weight": "bold"}),
        html.P([
            "TU Delft (",
            html.A("ftp://thermosphere.tudelft.nl", href="ftp://thermosphere.tudelft.nl", target="_blank"), 
            "); PI: Christian Siemes, ",
            html.A("c.siemes@tudelft.nl", href="mailto:c.siemes@tudelft.nl", target="_blank")
        ]),
        html.H2("Density Retrieval Method", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Accelerometer-inferred"),
        html.H2("Data Version", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Version_01"),
        html.H2("More Information", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(html.A("http://thermosphere.tudelft.nl/", href="http://thermosphere.tudelft.nl/", target="_blank")),
        html.P(html.A("https://earth.esa.int/eogateway", href="https://earth.esa.int/eogateway", target="_blank"))
    ], className="data-source-metadata")


def gen_GRACE_A_data():
    return html.Div([
        html.H1("GRACE-A Description", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            The Gravity Recovery and Climate Experiment (GRACE) mission was a joint project
            between NASA and DLR. The primary science objective of GRACE was to measure the
            Earth’s gravity field and time variability with unprecedented accuracy. GRACE consisted
            of two identical spacecraft that flew approximately 220 kilometers apart in a polar orbit
            500 kilometers above Earth.
            """
        ),
        html.H2("Data Source", style={"font-size": "20px", "font-weight": "bold"}),
        html.P([
            "TU Delft (",
            html.A("ftp://thermosphere.tudelft.nl", href="ftp://thermosphere.tudelft.nl", target="_blank"), 
            "); PI: Christian Siemes, ",
            html.A("c.siemes@tudelft.nl", href="mailto:c.siemes@tudelft.nl", target="_blank")
        ]),
        html.H2("Density Retrieval Method", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Accelerometer-inferred"),
        html.H2("Data Version", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Version_02"),
        html.P(html.A("https://earth.esa.int/eogateway/missions/grace/description", 
                      href="https://earth.esa.int/eogateway/missions/grace/description", target="_blank")),
        html.P(html.A("http://thermosphere.tudelft.nl/", href="http://thermosphere.tudelft.nl/", target="_blank"))
    ], className="data-source-metadata")


def gen_SWARM_A_data():
    return html.Div([
        html.H1("SWARM-A Description", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            Swarm comprises a constellation of three satellites in near-polar low orbits to obtain
            better and more varied measurements. The Swarm mission was launched from
            Plesetsk Cosmodrome on 22 November 2013. Swarm A and C form the lower pair of

            satellites flying side-by-side (1.4° separation in longitude at the equator) at an altitude of
            462 km (initial altitude) and at 87.35° inclination angle.
            """
        ),
        html.H2("Data Source", style={"font-size": "20px", "font-weight": "bold"}),
        html.P([
            "TU Delft (",
            html.A("ftp://thermosphere.tudelft.nl", href="ftp://thermosphere.tudelft.nl", target="_blank"), 
            "); PI: Christian Siemes, ",
            html.A("c.siemes@tudelft.nl", href="mailto:c.siemes@tudelft.nl", target="_blank")
        ]),
        html.H2("Density Retrieval Method", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Derived using precision orbit determination"),
        html.H2("Data Version", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Version_01"),
        html.H2("More Information", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(html.A("https://earth.esa.int/eogateway/missions/swarm", 
                      href="https://earth.esa.int/eogateway/missions/swarm", target="_blank")),
        html.P(html.A("http://thermosphere.tudelft.nl/", href="http://thermosphere.tudelft.nl/", target="_blank"))
    ], className="data-source-metadata")


def gen_GRACE_FO_data():
    return html.Div([
        html.H1("GRACE-FO Description", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            The Gravity Recovery and Climate Experiment Follow-on (GRACE-FO) mission is a
            partnership between NASA and the German Research Centre for Geosciences (GFZ).

            GRACE-FO is a successor to the original GRACE mission. The twin GRACE-Follow-On
            (GRACE-FO) satellites were launched in 2018 and provide measurements until today.
            The data covers the altitude range around 500 km.
            """
        ),
        html.H2("Data Source", style={"font-size": "20px", "font-weight": "bold"}),
        html.P([
            "TU Delft (",
            html.A("ftp://thermosphere.tudelft.nl", href="ftp://thermosphere.tudelft.nl", target="_blank"), 
            "); PI: Christian Siemes, ",
            html.A("c.siemes@tudelft.nl", href="mailto:c.siemes@tudelft.nl", target="_blank")
        ]),
        html.H2("Density Retrieval Method", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Accelerometer-inferred"),
        html.H2("Data Version", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Version_02"),
        html.H2("More Information", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(html.A("https://www.jpl.nasa.gov/missions/gravity-recovery-and-climate-experiment-follow-on-grace-fo",
                      href="https://www.jpl.nasa.gov/missions/gravity-recovery-and-climate-experiment-follow-on-grace-fo",
                      target="_blank")),
        html.P(html.A("http://thermosphere.tudelft.nl/", href="http://thermosphere.tudelft.nl/", target="_blank"))
    ], className="data-source-metadata")


def gen_MSISE00_01_data():
    return html.Div([
        html.H1("MSISE00-01 Description", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            The NRLMSISE-00 empirical atmospheric model extends from the ground to the exobase and is a major upgrade of the MSISE-90 
            model in the thermosphere. The MSIS-class model formulation consists of parametric analytic approximations to physical theory 
            for the vertical structure of the atmosphere as a function of location, time, solar activity (10.7-cm solar radio flux), and 
            geomagnetic activity.
            """
        ),
        html.H2("Solution Type", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Semiempirical"),
        html.H2("Solution Drivers", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("F10.7; ap (array of 7 values)"),
        html.H2("Version Number", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("00"),
        html.H2("Resolution (latitude, longitude, vertical, output cadence)", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("5°, 20°, 5 km, 15 mins"),
        html.H2("More Information", style={"font-size": "20px", "font-weight": "bold"}),
        html.A("https://ccmc.gsfc.nasa.gov/models/NRLMSIS~00/", href="https://ccmc.gsfc.nasa.gov/models/NRLMSIS~00/", target="_blank")
    ], className="data-source-metadata")


def gen_MSIS20_01_data():
    return html.Div([
        html.H1("MSIS20-01 Description", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            NRLMSIS 2.0 is an empirical atmospheric model that extends from the ground to the exobase and describes the average observed 
            behavior of temperature, 8 species densities, and mass density via a parametric analytic formulation.
            """
        ),
        html.H2("Solution Type", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Semiempirical"),
        html.H2("Solution Drivers", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("F10.7; ap (array of 7 values)"),
        html.H2("Version Number", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("2.1"),
        html.H2("Resolution (latitude, longitude, vertical, output cadence)", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("5°, 20°, 5 km, 15 mins"),
        html.H2("More Information", style={"font-size": "20px", "font-weight": "bold"}),
        html.A("https://ccmc.gsfc.nasa.gov/models/NRLMSIS~2.0", href="https://ccmc.gsfc.nasa.gov/models/NRLMSIS~2.0", target="_blank")
    ], className="data-source-metadata")


def gen_JB2008_01_data():
    return html.Div([
        html.H1("JB2008-01 Description", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            The Jacchia-Bowman (JB) 2008 is an empirical thermospheric density model, which is developed as an improved revision to the 
            JB2006 model based on the CIRA72 (COSPAR International Reference Atmosphere 1972) model. The CIRA72 model integrates the 
            diffusion equations using the Jacchia 71 temperature formulation to compute density values for an input geographical 
            location and solar conditions.
            """
        ),
        html.H2("Solution Type", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Semiempirical"),
        html.H2("Solution Drivers", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("S10, F10.7, M10, Y10; Dst, ap"),
        html.H2("Version Number", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("2008"),
        html.H2("More Information", style={"font-size": "20px", "font-weight": "bold"}),
        html.A("https://ccmc.gsfc.nasa.gov/models/JB2008~2008/", href="https://ccmc.gsfc.nasa.gov/models/JB2008~2008/", target="_blank")
    ], className="data-source-metadata")


def gen_DTM2020_01_data():
    return html.Div([
        html.H1("DTM2020-01 Description", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            The Drag Temperature Model (DTM) 2020 is an updated version of DTM 2013. Using DTM2013 as a background model, the temperature 
            and partial densities were re-estimated via least-squares adjustment to better fit the approximately 20–25% smaller observed 
            densities than those used in DTM2013. The DTM2020 operational is driven by F10.7 and Kp, and therefore all density data from 
            the sixties to the present-day can be assimilated.
            """
        ),
        html.H2("Solution Type", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Semiempirical"),
        html.H2("Solution Drivers", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("F10.7; Kp"),
        html.H2("Version Number", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("2020 operational"),
        html.H2("Resolution (latitude, longitude, vertical, output cadence)", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("5°, 5°, 20 km, 15 mins"),
        html.H2("More Information", style={"font-size": "20px", "font-weight": "bold"}),
        html.A("https://ccmc.gsfc.nasa.gov/models/DTM~2020/", href="https://ccmc.gsfc.nasa.gov/models/DTM~2020/", target="_blank")
    ], className="data-source-metadata")


def gen_DTM2013_01_data():
    return html.Div([
        html.H1("DTM2013-01 Description", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            The Drag Temperature Model (DTM) 2013 is a semi-empirical model describing the temperature, density, and composition of the 
            Earth's thermosphere in the altitude range between 120 to 1,500 km.
            """
        ),
        html.H2("Solution Type", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Semiempirical"),
        html.H2("Sollution Drivers", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("F30; Kp"),
        html.H2("Version Number", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("2013"),
        html.H2("Resolution (latitude, longitude, vertical, output cadence)", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("5°, 5°, 20 km, 15 mins"),
        html.H2("More Information", style={"font-size": "20px", "font-weight": "bold"}),
        html.A("https://ccmc.gsfc.nasa.gov/models/DTM~2013/", href="https://ccmc.gsfc.nasa.gov/models/DTM~2013/", target="_blank")
    ], className="data-source-metadata")


def gen_TIEGCM_Heelis_01_data():
    return html.Div([
        html.H1(["TIEGCM-Heelis-01", html.Br(), "Description"], style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            The NCAR Thermosphere-Ionosphere- Electrodynamics General Circulation Model
            (TIE-GCM) is a comprehensive, first-principles, three-dimensional, non-linear
            representation of the coupled thermosphere and ionosphere system that includes a self-
            consistent solution of the low-latitude electric field. The model solves the three-
            dimensional momentum, energy and continuity equations for neutral and ion species at
            each time step, using a semi-implicit, fourth-order, centered finite difference scheme, on
            each pressure surface in a staggered vertical grid.
            """
        ),
        html.H2("Solution Type", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("First Principle"),
        html.H2("Sollution Drivers", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Solomon & Qian Bands; Heelis-Kp"),
        html.H2("Version Number", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("2.0"),
        html.H2("Resolution (latitude, longitude, vertical, output cadence)", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("2.5°, 2.5°, 0.25 scale height, 20 mins"),
        html.H2("More Information", style={"font-size": "20px", "font-weight": "bold"}),
        html.A("https://ccmc.gsfc.nasa.gov/models/TIE-GCM~2.0", href="https://ccmc.gsfc.nasa.gov/models/TIE-GCM~2.0", target="_blank")
    ], className="data-source-metadata")


def gen_TIEGCM_Weimer_01_data():
    return html.Div([
        html.H1("TIEGCM-Weimer-01 Description", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            The NCAR Thermosphere-Ionosphere- Electrodynamics General Circulation Model
            (TIE-GCM) is a comprehensive, first-principles, three-dimensional, non-linear
            representation of the coupled thermosphere and ionosphere system that includes a self-
            consistent solution of the low-latitude electric field. The model solves the three-
            dimensional momentum, energy and continuity equations for neutral and ion species at
            each time step, using a semi-implicit, fourth-order, centered finite difference scheme, on
            each pressure surface in a staggered vertical grid.
            """
        ),
        html.H2("Solution Type", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("First Principle"),
        html.H2("Sollution Drivers", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Solomon & Qian Bands; Weimer"),
        html.H2("Version Number", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("2.0"),
        html.H2("Resolution (latitude, longitude, vertical, output cadence)", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("2.5°, 2.5°, 0.25 scale height, 20 mins"),
        html.H2("More Information", style={"font-size": "20px", "font-weight": "bold"}),
        html.A("https://ccmc.gsfc.nasa.gov/models/TIE-GCM~2.0", href="https://ccmc.gsfc.nasa.gov/models/TIE-GCM~2.0", target="_blank")
    ], className="data-source-metadata")

def gen_WACCMX_Weimer_01_data():
    return html.Div([
        html.H1("WACCMX-Weimer-01 Description", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            The NCAR Whole Atmosphere Community Climate Model with thermosphere and ionosphere extension 
            (WACCM-X) is a self-consistent general circulation model. It fully couples the chemistry and 
            dynamics, while calculating three-dimensional temperature, wind, composition, and ionospheric 
            structures from the surface to the exobase (500-700 km). It is a configuration of the NCAR 
            Community Earth System Model (CESM), which is currently based on the Community Atmosphere 
            Model-6 (CAM-6) physics and the three-dimensional chemical transport Model for Ozone and 
            Related chemical Tracers (MOZART) chemistry.            
            """
        ),
        html.H2("Solution Type", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("First Principle"),
        html.H2("Sollution Drivers", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Solomon & Qian Bands; Weimer"),
        html.H2("Version Number", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("CESM 2.2/WACCM-X 6.2"),
        html.H2("Resolution (latitude, longitude, vertical, output cadence)", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("0.9°, 1.25°, 0.25 scale height in the thermosphere, 10 mins"),
        html.H2("More Information", style={"font-size": "20px", "font-weight": "bold"}),
        html.A("https://ccmc.gsfc.nasa.gov/models/WACCMX~2.2/", href="https://ccmc.gsfc.nasa.gov/models/WACCMX~2.2/", target="_blank")
    ], className="data-source-metadata")

def gen_WACCMX_Heelis_01_data():
    return html.Div([
        html.H1("WACCMX-Heelis-01 Description", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            The NCAR Whole Atmosphere Community Climate Model with thermosphere and ionosphere extension 
            (WACCM-X) is a self-consistent general circulation model. It fully couples the chemistry and 
            dynamics, while calculating three-dimensional temperature, wind, composition, and ionospheric 
            structures from the surface to the exobase (500-700 km). It is a configuration of the NCAR 
            Community Earth System Model (CESM), which is currently based on the Community Atmosphere 
            Model-6 (CAM-6) physics and the three-dimensional chemical transport Model for Ozone and 
            Related chemical Tracers (MOZART) chemistry.            
            """
        ),
        html.H2("Solution Type", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("First Principle"),
        html.H2("Sollution Drivers", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("Solomon & Qian Bands; Heelis-Kp"),
        html.H2("Version Number", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("CESM 2.2/WACCM-X 6.2"),
        html.H2("Resolution (latitude, longitude, vertical, output cadence)", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("0.9°, 1.25°, 0.25 scale height in the thermosphere, 10 mins"),
        html.H2("More Information", style={"font-size": "20px", "font-weight": "bold"}),
        html.A("https://ccmc.gsfc.nasa.gov/models/WACCMX~2.2/", href="https://ccmc.gsfc.nasa.gov/models/WACCMX~2.2/", target="_blank")
    ], className="data-source-metadata")

def gen_CTIPe_01_data():
    return html.Div([
        html.H1("CTIPe-01 Description", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            The Coupled Thermosphere Ionosphere Plasmasphere Electrodynamics Model (CTIPe)
            model simulates the time-dependent global structure of the wind vector, temperature,
            and density of the neutral thermosphere by numerically solving the non-linear primitive
            equations of momentum, energy, and continuity on a 3D spherical polar grid rotating
            with the Earth.
            """
        ),
        html.H2("Solution Type", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("First Principle"),
        html.H2("Solution Drivers", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            F10.7, F81, Solomon &amp; Qian bands; Weimer-2005, solar wind density and velocity,
            interplanetary magnetic field, Hemispheric Power, Kp
            """
        ),
        html.H2("Version Number", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("4.1"),
        html.H2("Resolution (latitude, longitude, vertical, output cadence)", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("2°, 18°, 15 levels between 80 to ~500 km, 15 mins"),
        html.H2("More Information", style={"font-size": "20px", "font-weight": "bold"}),
        html.A("https://ccmc.gsfc.nasa.gov/models/CTIPe~4.1/", href="https://ccmc.gsfc.nasa.gov/models/CTIPe~4.1/", target="_blank")
    ], className="data-source-metadata")


def gen_GITM_01_data():
    return html.Div([
        html.H1("GITM-01 Description", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            The GITM is a 3-dimensional spherical code that models the Earth&#39;s thermosphere and
            ionosphere system using a stretched grid in latitude and altitude. GITM allows for non-
            hydrostatic solutions to develop (i.e., the full vertical momentum equation is solved), so
            more realistic dynamics in the auroral zone can be simulated.
            """
        ),
        html.H2("Solution Type", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("First Principle"),
        html.H2("Solution Drivers", style={"font-size": "20px", "font-weight": "bold"}),
        html.P(
            """
            F10.7; Hemispheric Power Index; IMF Solar wind velocity and Solar irradiance
            """
        ),
        html.H2("Version Number", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("21.11"),
        html.H2("Resolution (latitude, longitude, vertical, output cadence)", style={"font-size": "20px", "font-weight": "bold"}),
        html.P("2.5°, 5°, 0.25 scale height, 10 mins"),
        html.H2("More Information", style={"font-size": "20px", "font-weight": "bold"}),
        html.A("https://ccmc.gsfc.nasa.gov/models/GITM~21.11/", href="https://ccmc.gsfc.nasa.gov/models/GITM~21.11/", target="_blank")
    ], className="data-source-metadata")
