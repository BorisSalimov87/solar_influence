Coronal Holes

Steven R. Cranmer

arXiv:0909.2847v1 [astro-ph.SR] 15 Sep 2009

Harvard-Smithsonian Center for Astrophysics

60 Garden Street, Mail Stop 50

Cambridge, MA 02138, U.S.A.

email: scranmer@cfa.harvard.edu

http://www.cfa.harvard.edu/~scranmer/


## Abstract

Coronal holes are the darkest and least active regions of the Sun, as observed both on the solar disk

and above the solar limb. Coronal holes are associated with rapidly expanding open magnetic fields and

the acceleration of the high-speed solar wind. This paper reviews measurements of the plasma properties

in coronal holes and how these measurements are used to reveal details about the physical processes that

heat the solar corona and accelerate the solar wind. It is still unknown to what extent the solar wind is fed

by flux tubes that remain open (and are energized by footpoint-driven wave-like fluctuations), and to what

extent much of the mass and energy is input intermittently from closed loops into the open-field regions.

Evidence for both paradigms is summarized in this paper. Special emphasis is also given to spectro-

scopic and coronagraphic measurements that allow the highly dynamic non-equilibrium evolution of the

plasma to be followed as the asymptotic conditions in interplanetary space are established in the extended

corona. For example, the importance of kinetic plasma physics and turbulence in coronal holes has been

affirmed by surprising measurements from the UVCS instrument on SOHO that heavy ions are heated to

hundreds of times the temperatures of protons and electrons. These observations point to specific kinds

of collisionless Alfvén wave damping (i.e., ion cyclotron resonance), but complete theoretical models do

not yet exist. Despite our incomplete knowledge of the complex multi-scale plasma physics, however,

much progress has been made toward the goal of understanding the mechanisms ultimately responsible

for producing the observed properties of coronal holes.

# 1 Introduction

Coronal holes are regions of low density plasma on the Sun that have magnetic fields opening freely into the

heliosphere. Because of their low density, coronal holes tend to be the regions of the outer solar atmosphere

that are most prone to behaving as a collisionless plasma. Ionized atoms and electrons flow along the open

magnetic fields to form the highest-speed components of the solar wind.

The term “coronal hole” has come to denote several phenomena that may not always refer to the same

regions. First, the darkest patches on the solar surface, as measured in ultraviolet (UV) and X-ray radiation,

are called coronal holes. Second, the term also applies to the lowest-intensity regions measured above the

solar limb, seen either during a total solar eclipse or with an occulting coronagraph. Third, there is a more

theoretical usage that equates coronal holes with all open-field footpoints of time-steady solar wind flows.

There are good reasons why these three ideas should be related to one another, but the overlap between

them is not complete. To avoid possible confusion, this paper will mainly use the first two observational

definitions, with the third one being only partly applicable.

During times of low solar activity, when the Sun’s magnetic field is dominated by a rotationally-aligned

dipole component, there are large coronal holes that cover the north and south polar caps of the Sun. In

1


---


more active periods of the solar cycle, coronal holes can exist at all solar latitudes, but they may only persist for several solar rotations before evolving into different magnetic configurations.

Despite not being as visually spectacular as active regions, solar flares, or coronal mass ejections

(CMEs), coronal holes are of abiding interest for (at least) three main reasons.

1. The extended corona and solar wind connected with coronal holes tends to exist in an ambient time-

steady state, at least in comparison with other regions. This makes coronal holes a natural starting

point for theoretical modeling, since it often makes sense to begin with the simplest regions before

attempting to understand more complex and variable structures.

2. Coronal hole plasma has the lowest density, which makes it an optimal testbed for studies of colli-

sionless kinetic processes that are the ultimate dissipation mechanisms in many theories of coronal

heating. Other regions tend to have higher densities and more rapid Coulomb collisions, and thus the

unique signatures of the kinetic processes (in their particle velocity distributions) are not as straight-

forward to measure as in coronal holes.

3. Coronal holes and their associated high-speed wind streams are also responsible for a fraction of

major geomagnetic storms at 1 AU. Corotating interaction regions (CIRs) form when fast and slow

wind streams collide with one another, and the subsequent interaction between these structures and

the Earth’s magnetosphere can give rise to long-lasting fluxes of energetic electrons.

This paper reviews measurements of the plasma properties of coronal holes and how these measure- ments have been used to put constraints on theoretical models of coronal heating and solar wind accel- eration. There have been several earlier reviews that have focused mainly on the topic of coronal holes, including Zirker (1977), Suess (1979), Harvey and Sheeley Jr (1979), Parker (1991), Kohl and Cranmer (1999), Hudson (2002), Cranmer (2002a), Ofman (2005), de Toma and Arge (2005), Jones (2005), and Wang (2009). Interested readers are urged to survey these other reviews in order to fill in any gaps in topical coverage in the present paper.

The remainder of this paper is organized as follows. Section 2 gives a brief history of the discovery

and early years of research on coronal holes. Section 3 summarizes the observations and derived plasma properties of “on-disk” coronal holes (i.e., primarily using the definition of holes as dark patches on the solar surface at UV and X-ray wavelengths). Section 4 reviews the measurements of “off-limb” coronal holes and describes our current knowledge of how these structures are linked to various kinds of solar wind streams measured in situ. Section 5 discusses a broad range of possible theoretical explanations for how the plasma in coronal holes is heated and how the solar wind in these regions is accelerated. Section 6 concludes this paper with a few words about how the study of coronal holes helps to improve our wider understanding of heliophysics, astrophysics, and plasma physics.

# 2 Historical Overview

Although the term “coronal hole” was not first used until the middle of the 20th century, people have reported the existence of visible features associated with the Sun’s corona – seen during total eclipses – for centuries (see, e.g., Wang and Siscoe, 1980; Vaquero, 2003). A popular astronomy book from the first decade of the 20th century (Serviss, 1909) contained clear descriptions of coronal streamers, eruptive prominences, and polar plumes in coronal holes. The following description of the latter, from an eclipse in 1900, conveys that early speculation may sometimes be prescient:

“The sheaves of light emanating from the poles look precisely like the ‘lines of force’ surrounding

the poles of a magnet. It will be noticed in this photograph that the corona appears to consist of two portions: one comprising the polar rays just spoken of, and the other consisting of the broader, longer, and less-defined masses of light extending out from the equatorial and middle-latitude zones. Yet even in this more diffuse part of the phenomenon one can detect the presence of submerged curves bearing more

2


---


Figure 1: Left: Adaptation of a sketch of the quiet solar corona made by Piddington (1972), based on prior drawings (Waldmeier, 1955) and photographs (Gold, 1955) of the 30 June 1954 eclipse. Right: Contrast- adjusted eclipse image taken with the POISE instrument on 26 February 1998, in Westpunt, Curaçao. The original image was made available courtesy of the High Altitude Observatory (HAO), University Corpora- tion for Atmospheric Research (UCAR), Boulder, Colorado. UCAR is sponsored by the National Science Foundation.

or less resemblance to those about the poles. Just what part electricity or electro-magnetism plays in the mechanism of solar radiation it is impossible to say, but on the assumption that it is a very important part is based the hypothesis that there exists a direct solar influence not only upon the magnetism, but upon the weather of the earth” (Serviss, 1909).

The first quantitative observations of coronal holes were made by Waldmeier (1956, 1957) at the Swiss

Federal Observatory in Zürich. These features were identified as long-lived regions of negligible intensity in coronagraphic (off-limb) images of the 5303 Å green emission line (see also Waldmeier, 1975, 1981). Waldmeier called the features that appeared more-or-less circular when projected onto the solar disk Löcher (holes), and the more elongated features were called Kanal (channels) or Rinne (grooves).

In off-limb eclipse and coronagraph images, the darkest coronal hole regions are surrounded by brighter

and more complex streamers. These wispy structures appear to be connected to closed magnetic field lines at the solar surface, but they are often stretched upwards to an elongated cusp-like point, with thin “stalks” of radial rays at the top. For this reason their appearance was likened to a pointed German helmet (or a brush-topped Greek or Roman helmet), and the common phrase helmet streamers is often seen. The earliest studies of coronal morphology tended to concentrate more on streamers than coronal holes because the former are significantly easier to see than the latter (see, e.g., Miller, 1908; Mitchell, 1932; Newkirk, 1967; Pneuman, 1968). Piddington (1972) outlined some early ideas about the global structure of the “quiet” (i.e., solar minimum) corona. Figure 1 compares an adaptation of J. H. Piddington’s sketch of the quiet corona to a more recent photograph from another eclipse around solar minimum.

As the quality of the observations improved, coronal holes became objects of study in their own right.

The largest coronal holes were observed to contain fine thread-like polar plumes that appear to follow the superradially expanding open magnetic field lines above the solar limb (Saito, 1958; Stoddard et al., 1966; Newkirk and Harvey, 1968). These elongated structures were found to correlate with bright chromospheric faculae on the surface (e.g., Harvey, 1965) and with longer extensions for the small jet-like spicules that continually rise and fall above the limb (Lippincott, 1957; Beckers, 1968).

Coronal holes were essentially re-discovered in the late 1960s and early 1970s as discrete dark patches

on the X-ray and ultraviolet solar disk. Newkirk (1967) reviewed some of the earliest rocket-based mea- surements in the extreme UV, and Tousey et al. (1968) discussed how the UV emission was “usually weaker over the poles” in images from a series of rocket flights between 1963 and 1967 (around solar minimum). These regions on the solar disk came to be called coronal holes in parallel with the earlier off-limb usage. Munro and Withbroe (1972) analyzed OSO–4 observations to conclude that both the density and electron

3


---


Figure 2: X-ray corona (0.25–4.0 keV) observed by the Soft X-ray Telescope (SXT) on Yohkoh, on 6 December 2000. Yohkoh is a mission of the Institute of Space and Astronautical Sciences in Japan, with participation from the U.S. and U.K.

temperature were lower in these dark regions. In 1973 and 1974, solar instruments on the Apollo telescope mount (ATM) on Skylab confirmed many earlier ideas about coronal holes with data significantly better in quantity and quality (Huber et al., 1974; Kahler, 2000).

In addition to the large north and south polar holes, there were also found to be smaller coronal holes

that exist at lower latitudes (often at times other than solar minimum). Sometimes the largest coronal holes can exhibit thin “peninsulas” that jut out from the main regions. Harvey and Recely (2002) called these regions “polar lobes.” Notable examples have been the so-called “Boot of Italy” seen by Skylab in 1974 (e.g., Zirker, 1977) and the “Elephant’s Trunk” seen by SOHO in 1996 (Del Zanna and Bromage, 1999). A third example, from December 2000, is shown in Figure 2.

Additional insights came from the fusion of spectroscopy and coronagraphic occultation. Inspired by

rocket-borne UV observations of the extended corona during a solar eclipse in March 1970, Kohl et al. (1978) developed a UV coronagraph spectrometer to measure the profile shape of the bright H I Lyman α emission line at 1216 Å. This line is sensitive to several key properties of the velocity distribution of coronal protons, and thus these observations could be used to begin distinguishing proton temperatures from electron temperatures in the collisionless outer regions of coronal holes (see Section 4.3). The rocket- borne UV coronagraph spectrometer was launched three times (in 1979, 1980, and 1982), and the results included the first direct evidence for proton heating and supersonic outflow in coronal holes (Kohl et al., 1980; Strachan et al., 1993; Kohl et al., 2006).

The fact that coronal holes coincide with regions of open magnetic field that expands out into inter-

planetary space was realized during the first decade of in situ solar wind observations (e.g., Wilcox, 1968; Altschuler et al., 1972; Hundhausen, 1972). Noci (1973) made a theoretical argument, on the basis of mea- sured wave fluxes and heat conduction, that coronal holes should have the largest solar wind kinetic energy fluxes (i.e., the highest speeds). Pneuman (1973) argued that coronal holes need not have lower energy de- position than closed-field regions (as is suggested by the lower intensities of coronal holes) if the solar wind carries away much of that energy. Krieger et al. (1973) utilized X-ray sounding rocket images to identify a large coronal hole as the solar source of a strong high-speed stream as measured by the Pioneer 6 and Vela spacecraft. Around this time it was also realized that coronal holes and high-speed wind streams are also responsible for a fraction of the geomagnetic storms seen at 1 AU (Bell and Noci, 1973; Neupert and Pizzo, 1974; Bell and Noci, 1976). (See also Tanskanen et al. (2005) and Zhang et al. (2007).) Although there is still no complete understanding of which types of solar wind flow are connected with which types of coronal structures, the causal link between the largest coronal holes and high-speed streams remains firm (see also Section 4.1).

# 3 Properties of On-Disk Coronal Holes

The traditional observational distinction between coronal holes and their surroundings (i.e., active regions and “quiet Sun”) is that coronal holes have the lowest emission in the UV and X-ray. This definition must

4


---


be amended, however, to exclude filaments (which are often dark when projected against the solar disk) that are cool magnetic structures and not part of the corona (see, e.g., Scholl and Habbal, 2008; Krista and Gallagher, 2009). Coronal hole magnetic fields are known to be more uniform and unipolar than in other regions (see below). The boundaries between coronal holes and surrounding regions are sometimes sharp, sometimes diffuse, and sometimes filled with many small loops (Hudson, 2002).

Coronal holes are more or less indistinguishable from their surroundings in the photosphere and low

chromosphere, and usually one cannot see any significant intensity contrast between hole and non-hole re- gions until the temperature exceeds about 105 K. Spectra, however, can help make the distinction clearer. Teplitskaya et al. (2007) found that central self-reversals in the chromospheric Ca II H and K lines are noticeably different in coronal holes as opposed to surrounding quiet-Sun regions. A frequently used ob- servational diagnostic of coronal hole boundaries is the He I 10830 Å near-infrared absorption line triplet (Harvey et al., 1975; Harvey and Recely, 2002). At these wavelengths, the absorption is weakest in coronal holes (i.e., the intensity is highest) and spectroheliogram images show the coronal holes quite clearly. It is somewhat counterintuitive that a spectral line of a neutral species (He0 ) should be sensitive to the properties of the hot corona. However, the atomic level populations that determine the He I 10830 Å source function are unusually responsive to photoionization from UV wavelengths shortward of 504 Å. The overlying solar corona emits these wavelengths in abundance. In coronal hole regions, though, the corona generally has a lower density and temperature, and thus there is less intense UV and X-ray emission to populate the upper levels of the He0 triplet state (see, e.g., Zirin, 1975; Andretta and Jones, 1997; Centeno et al., 2008). This gives rise to reduced absorption. The He I 10830 Å lines are also good probes of supersonic outflow veloc- ities in distant stellar winds (see, e.g., Dupree et al., 2005; Kwan et al., 2007; Sanz-Forcada and Dupree, 2008).

Another observational diagnostic of coronal holes is their elemental abundance signature (e.g., Feld-

man, 1998; Feldman and Widing, 2003). In the upper chromosphere, transition region, and low corona, holes exhibit abundances very close to those measured in the photosphere. This stands in contrast to other regions (quiet Sun and active regions), which show significant enhancements in the abundances of elements with low first ionization potential (FIP). This selective fractionation is believed to occur in the upper chro- mosphere, where low-FIP elements become ionized and high-FIP elements remain more neutral. These patterns extend into the heliosphere, where high-speed flows associated with coronal holes are often iden- tifiable from their near-photospheric FIP abundances (von Steiger et al., 1995; Zurbuchen et al., 2002). However, there is still no widespread agreement about the exact physical processes that give rise to this preferential ionization.

The number, sizes, and heliographic locations of coronal holes vary as a function of the solar activity

cycle. Large polar holes exist for about 7 years around solar minimum, and are not present for about 3 or 4 years around solar maximum. However, in the declining phase of activity soon after the maximum, it is possible to see the gradual growth of the new-polarity polar coronal holes. This occurs as a number of smaller high-latitude holes eventually collect together at the poles (Timothy et al., 1975; Harvey and Recely, 2002). Taking this growth phase into account, there are only about 1 or 2 years at solar maximum without any distinct high-latitude coronal hole presence. Figure 3 illustrates the growth phase around the peak of solar cycle 23 in 2001. The growth and full “reappearance” of polar coronal holes at this time was described by Miralles et al. (2001b) and McComas et al. (2002). The post-maximum growth of new polar coronal holes lasts about twice as long as their disappearance in the rising phase of the next maximum (Waldmeier, 1981; Fisher and Sime, 1984).

Many low-latitude coronal holes tend to be situated near the edges of magnetically complex active

regions. Sometimes active regions emerge within the coronal holes themselves; these have been called “sea anemone” type regions from their spiky, flower-like appearance (Shibata et al., 1994; Asai et al., 2008). Evolving magnetic interactions between active regions and coronal holes have been studied both as a means of enhancing the mass flux of the associated solar wind on nearby open flux tubes (e.g., Habbal et al., 2008; Wang et al., 2009) and as a possible explanation for the nearly rigid rotation of coronal holes (Wang et al., 1996; Antiochos et al., 2007). A burst of emerging magnetic flux in one of these active regions may give

5


---


Figure 3: Polar view of the development of the north polar coronal hole from January to August 2001 (e.g., Carrington rotations 1972 to 1979), using reconstructed coronal hole boundaries from Kitt Peak He I 10830 Å maps. The maximum of solar activity occurred between late 2000 and early 2001. Data from the National Solar Observatory/Kitt Peak were produced cooperatively by NSF/NOAO, NASA/GSFC, and NOAA/SEL.

rise to new systems of loop connections in the area bordering the coronal hole, and thus cause the coronal hole to decrease in size. This kind of rapid topological evolution of the magnetic field may be relevant in explaining extreme space weather events such as “the day the solar wind disappeared” (i.e., the dramatic drop in the in situ density seen on 11 May 1999; see Janardhan et al., 2008).

Photospheric magnetograms show that coronal holes are more unipolar than other regions; i.e., they

have a larger degree of magnetic flux imbalance between the two polarities (Levine, 1982; Wang, 2009). For the large polar coronal holes, this appears to be the long-term outcome of the decay of active-region magnetic fields and their eventual diffusion up to the poles. The unipolar nature of coronal holes is likely to be related to their connection with open-field solar wind streams. As described in Section 2, one reason why coronal holes are dark is that the solar wind carries away both mass and energy, leaving a lower density and pressure. In addition, Abramenko et al. (2006a) and Hagenaar et al. (2008) found that the local rate of emergence of small-scale magnetic flux (mostly in the form of “ephemeral” small-scale bipoles) is substan- tially lower in unipolar regions than in more mixed or balanced regions of positive and negative magnetic polarity. In most theories of coronal heating of closed loops, the total flux and the overall complexity of the field both drive the total heating rate. Thus, the lower emergence rate of new flux elements in coronal holes may be another factor determining why they have lower densities and pressures (i.e., less coronal heating; see, e.g., Rosner et al., 1978) and thus why they are dark.

Over the past few decades, the magnetic connection between coronal holes and the fast solar wind has

been traced down to ever smaller spatial scales. We now can say with some certainty that much of the plasma that eventually becomes the time-steady solar wind seems to originate in thin magnetic flux tubes (with observed sizes of order 50–200 km) observed mainly in the dark lanes between the ∼1000 km size photospheric granulation cells. These strong-field (1–2 kG) flux tubes have been called G-band bright points and network bright points, and groups of them have been sometimes termed “solar filigree” (e.g., Dunn and Zirker, 1973; Spruit, 1984; Berger and Title, 2001; Tsuneta et al., 2008). These flux tubes are concentrated most densely in the supergranular network (i.e., the bright lanes between the larger ∼30,000 km size su- pergranulation cells). Somewhere in the low chromosphere, the thin flux tubes expand laterally to the point where they merge with one another into a more-or-less homogeneous network field distribution of order ∼100 G. This merged (mainly vertically oriented) field is associated mainly with the lanes and vertices be-

6


---


Figure 4: Summary of the largely unipolar magnetic field structure of polar coronal holes, with the fields of view successively widening from flux tubes in intergranular lanes (a), to a “funnel” rooted in a supergranular network lane (b), and finally to the extended corona (c). Adapted from Figure 1 of Cranmer and van Ballegooijen (2005).

tween supergranular cells. Because this field does not fill the entire coronal volume, it is still susceptible to an additional stage of lateral expansion and weakening. Thus, at a larger height in the chromosphere, these network flux bundles are believed to undergo further broadening into so-called “funnels” (Gabriel, 1976; Dowdy et al., 1986). However, it is still unclear to what extent the closed fields in the supergranular cell centers affect the canopy-like regions between funnels (e.g., Schrijver and Title, 2003). Figure 4 illustrates the successive merging of unipolar field in coronal holes.

Observations of blueward Doppler shifts in supergranular network lanes and vertices, especially in

large coronal holes, may be evidence for either the “launching” of the solar wind itself or for upward- going waves that are linked to wind acceleration processes (e.g., Hassler et al., 1999; Peter and Judge, 1999; Aiouaz et al., 2005; Tu et al., 2005). These measurements are consistent with several models of the dynamic, multi-species solar wind in superradially expanding funnels (Byhring et al., 2008; Marsch et al., 2008). However, this interpretation of the data is still not definitive, because there are other observational diagnostics that have shown more of a blueshift in the supergranular cell-centers between funnels (e.g., He I 10830 Å; Dupree et al., 1996; Malanushenko and Jones, 2004). There may be subtle radiative transfer effects that preferentially brighten regions of upflow or downflow (see, e.g., Chae et al., 1997; Avrett, 1999), and these may need to be taken into account in order to understand the meaning of the measured Doppler shifts in these regions.

Lastly, it is important to mention the phenomenon of transient coronal holes (sometimes known as

“coronal dimmings”). These are rapid reductions in the UV and X-ray intensity in discrete patches that appear to be spatially and temporally correlated with the liftoff of CME plasma (e.g., Rust, 1983; Thompson et al., 2000; Yang et al., 2009). Spectroscopically, these regions are seen to exhibit similar characteristics as normal coronal holes, including Doppler blueshifts (Harra et al., 2007) and large amplitudes of nonthermal wave broadening (McIntosh, 2009). UV coronal dimmings are beginning to be used as diagnostics for the amount of plasma released – i.e., the total mass – in the CME event (e.g., Aschwanden et al., 2009). It should be noted that transient coronal holes represent just one kind of observed dimming that is associated with time-dependent flare/CME activity; there are other types of dimmings that do not resemble coronal holes (Hudson, 2002).

7


---


# 4 Properties of Off-Limb Coronal Holes

Coronal holes observed above the solar limb usually trace out the same regions that are identified as dark coronal-hole “patches” directly on the solar disk. Thus, the lower plasma density that more or less defines the off-limb coronal hole is directly related to the lower density measured on the disk. Section 4.1 briefly discusses how these regions are believed to be connected magnetically with the broader heliosphere. The observations of off-limb coronal holes made with visible-light imaging and polarimetry (Section 4.2) and ultraviolet spectroscopy (Section 4.3) are also summarized below.

## 4.1 Magnetic connectivity with the solar wind

Although the magnetic field in the solar corona is generally too weak to be measured directly, the overall morphology of the field lines can be extrapolated from magnetograms taken at the level of the photosphere. One popular technique is the “potential field source surface” (PFSS) method, which assumes the corona is current-free out to a spherical surface (set typically at a radius between 2.5 and 3.5 solar radii, or R⊙ ), above which the field is radial (e.g., Schatten et al., 1969; Altschuler and Newkirk, 1969; Hoeksema and Scherrer, 1986). The PFSS method has been shown to create a relatively good mapping between the Sun and the heliosphere (Arge and Pizzo, 2000; Luhmann et al., 2002; Wang and Sheeley Jr, 2006; Wang, 2009), although the results can be problematic for regions dominated by stream-stream interactions (Poduval and Zhao, 2004).

By far, the strongest causal link between a specific type of coronal structure (measured via remote

sensing) and a particular type of quasi-steady solar wind flow (measured in situ) is the connection between large coronal holes and high-speed streams (Wilcox, 1968; Krieger et al., 1973). The general interpretation of this correlation – together with the results of magnetic extrapolation models such as PFSS – is that coronal holes represent a bundle of open flux tubes that flare out horizontally as distance increases. In other words, the coronal hole flux tubes expand superradially. Although there are some observations that appear to support other interpretations (Woo et al., 1999; Habbal et al., 2001; Woo, 2005; Woo and Druckmüllerová, 2008), the preponderance of evidence seems clearly to support the idea that fast solar wind streams emerge mainly from superradially expanding coronal holes (e.g., Guhathakurta et al., 1999a; Cranmer et al., 1999b; Jones, 2005; Wang and Sheeley Jr, 2006; Wang et al., 2007).

In contrast to the rather definitive correlation between large coronal holes and the fast solar wind, the

coronal sources of the more chaotic slow-speed solar wind are not as well understood (see Schwenn, 2006). Two regions that are frequently cited as sources of slow wind are: (1) boundaries between coronal holes and streamers, and (2) narrow plasma sheets that extend out from the tops of streamer cusps (Wang et al., 2000; Strachan et al., 2002; Susino et al., 2008). These regions tend to dominate around solar minimum. Note that the former type of boundary region tends to contain flux tubes that may be classified as coronal holes when using the theoretical definition (i.e., footpoints of field lines that are open; see Section 1) but would not be defined as such when using the observational definitions (i.e., low emission or low density).

During more active phases of the solar cycle, there is evidence that slow solar wind streams also emanate

from small coronal holes (e.g., Nolte et al., 1976; Neugebauer et al., 1998; Zhang et al., 2003) and active regions (Hick et al., 1995; Liewer et al., 2004; Sakao et al., 2007). During the rising phase of solar activity, there seems to be a relatively abrupt (< 6 month) change in the locations of slow wind footpoints: from the high-latitude hole/streamer boundaries to the low-latitude active region and small coronal hole regions (Luhmann et al., 2002). The ability of many of these kinds of regions to produce slow wind was modeled by Cranmer et al. (2007) and Wang et al. (2009); see also Section 5.

## 4.2 Visible light observations

Measurements of the plasma properties in the extended corona (i.e., r ≈ 1.5 to 10 R⊙ , where the main solar wind acceleration occurs) require the bright solar disk to be occulted. The coronal emission is many orders

8


---


Figure 5: Comparison of empirically determined densities in the upper solar atmosphere. Avrett and Loeser (2008) values of electron number density (solid black curve) and total hydrogen number density (dot-dashed black curve) are compared with various visible-light pB electron number densities for coronal holes (blue curves) and streamers (red curves); see text for details.

of magnitude less bright than the emission from the solar disk, so even the vast majority of “stray light” that diffracts around the occulting edge must be eliminated. Visible-light coronagraphs that combine stray-light rejection with linear polarimetry have the ability to measure the Thomson-scattered polarization brightness (pB) in the corona. The use of pB rather than the total coronal brightness eliminates the contribution from the dust-scattered F-corona, which is believed to be unpolarized up to distances of about 5 R⊙ . Because the coronal plasma is optically thin to the Thomson-scattered photons, pB is proportional to the line-of- sight integral of the electron density ne , multiplied by a known scattering function. Methods for inverting this integral to derive ne as a function of position in various coronal structures have been developed and improved over the years (e.g., van de Hulst, 1950; Altschuler and Perry, 1972; Munro and Jackson, 1977; Guhathakurta and Holzer, 1994; Frazin et al., 2007). For coronal holes, the LASCO (Large Angle and Spectrometric Coronagraph) instrument on SOHO has also been used to probe the superradial expansion of open magnetic flux tubes (DeForest et al., 1997, 2001) and the evolution of transient polar jets (Wang et al., 1998; Wood et al., 1999). The White Light Coronagraphs on Spartan 201 (Fisher and Guhathakurta, 1995) and on the UVCS (Ultraviolet Coronagraph Spectrometer) instrument aboard SOHO (e.g., Kohl et al., 1995; Romoli et al., 2002) have provided electron densities between 1.5 and 5 R⊙ in coronal holes.

Figure 5 illustrates a selection of visible-light measurements of the electron density in coronal holes

and compares them to similar measurements of streamers and to a semi-empirical model of the chromo- sphere, transition region, and low corona (Avrett and Loeser, 2008). The blue coronal hole curves were adapted from the results of Fisher and Guhathakurta (1995) (dotted), Cranmer et al. (1999b) (solid), Doyle et al. (1999) (dashed), and Guhathakurta et al. (1999b) (dot-dashed). The red curves for equatorial helmet streamers were adapted from the results of Sittler and Guhathakurta (1999) (solid) and Gibson et al. (1999) (dashed).

Note that streamers are denser than coronal holes by about a factor of 10, but the hole measurements

themselves can often exhibit variations in the electron density by factors of the order of 2–3. Much of this spread is likely to be the result of different lines of sight passing through regions that contain varying

9


---


numbers of polar plumes (see, e.g., Cranmer et al., 1999b, 2008). Some of the cited pB observations were optimized to avoid bright concentrations of plumes, and others have been purposefully averaged over the full range of coronal hole substructure. It is also possible that absolute calibration uncertainties may still exist between the different instruments used to determine pB and ne , and this could compound the reported range of variation in coronal hole electron densities.

For a steady-state solar wind outflow, the conservation of mass demands that the product of density, flow

speed, and cross-sectional area of the flux tube remain constant. Thus, if the magnetic geometry and the electron density are known, mass conservation allows the solar wind outflow speed to be computed. Kohl et al. (2006) used the representative values of ne shown in Figure 5 together with a range of estimates for the superradial flux-tube expansion of coronal holes to determine outflow speeds in coronal holes. Figure 41a of Kohl et al. (2006) illustrates the result of this process, which shows a large range of values reflecting the uncertainties in both ne and the flux-tube area factor. Despite these uncertainties, though, the electron densities that became available in the 1990s demonstrated that the fast solar wind accelerates rapidly in coronal holes – probably reaching half of its asymptotic terminal speed (u∞ ≈ 700–800 km s−1 ) by heights no larger than 2–4 R⊙ .

The increased sensitivity of the LASCO instrument over earlier coronagraphs revealed a nearly contin-

ual release of low-contrast density inhomogeneities, or “blobs,” from the cusps of helmet streamers (Shee- ley Jr et al., 1997; Tappin et al., 1999; Wang et al., 2000; Chen et al., 2009). These features were seen to accelerate up to speeds of order 300–400 km s−1 by the time they reached the outer edge of the LASCO field of view (r ≈ 30 R⊙ ); see also Figure 8 below. The blobs are typically only about 10% to 15% brighter or dimmer than the surrounding streamer material. Because of this low contrast, these features do not appear to comprise a large fraction of the mass flux of the slow solar wind. However, it is still unclear whether blobs are passive “tracers” that flow with the solar wind speed, or whether they are wavelike fluctuations that propagate relative to the background solar wind reference frame. This diagnostic tool has been much more difficult to apply in coronal holes than it has in the bright streamers, so no firm measurements of the fast wind acceleration yet exist from this technique.

Visible light measurements have also revealed evidence for compressive magnetohydrodynamic (MHD)

waves that propagate along open field lines in coronal holes. Intensity oscillations measured by the UVCS and EIT instruments on SOHO were found to have periodicities between about 10 and 30 minutes and are consistent with being upwardly propagating slow-mode magnetosonic waves (DeForest and Gurman, 1998; Ofman et al., 1999, 2000). The relative amplitude of the density fluctuations (δn/n0 ) for these waves was found to range between about 0.03 and 0.15 (see Cranmer, 2004a). This is consistent with measurements of the density fluctuation amplitudes made at larger distances via radio scintillations (Spangler, 2002) and in situ instruments (Tu and Marsch, 1994). There have also been claims that low-frequency oscillations have been measured in H I Lyα emission (Morgan et al., 2004; Bemporad et al., 2008; Telloni et al., 2009). In these cases, however, it is extremely important to take into account all of the relevant instrumental effects. These measurements still appear to be provisional.

As seen in Section 2 above, coronal holes have long been observed as the sites of thin, ray-like polar

plumes. The earliest measurements of polar plume properties were made in broad-band visible light, and these dense strands are often seen to stand out distinctly from the ambient interplume corona. It is not clear, though, to what extent off-limb observations (which integrate over long optically thin lines of sight) ever capture only the “pure” plume or interplume plasmas. Space-based observations from, e.g., Spartan 201 and SOHO improved our ability to measure the physical properties in and between plumes (e.g., Fisher and Guhathakurta, 1995; DeForest et al., 1997; Cranmer et al., 1999b; DeForest et al., 2001). Although the brightest plumes are still discernible at the uppermost heights observed by LASCO (i.e., 30–40 R⊙ ), the plume/interplume density contrast becomes too low to measure clearly in interplanetary space (r > 60 R⊙ ). However, indirect and possibly plume-related signatures in the in situ data have been reported by Thieme et al. (1990), Reisenfeld et al. (1999), and Yamauchi et al. (2002). The disappearance of plumes probably is the result of some combination of transverse pressure balance (i.e., dense plumes expanding to fill more of the available volume; see Del Zanna et al., 1998) and MHD instabilities that can mix the two components

10


---


(Parhi et al., 1999; Andries and Goossens, 2001).

## 4.3 Ultraviolet spectroscopy

Ultraviolet spectroscopy of the corona is a powerful tool for obtaining detailed empirical descriptions of solar plasma conditions (see, e.g., Kohl and Withbroe, 1982; Withbroe et al., 1982). Coronal holes, being the lowest density regions of the outer solar atmosphere, exhibit a complex array of plasma parameters due to their nearly collisionless nature. As a result, every ion species tends to have its own unique temperature, its own type of departure from a Maxwellian velocity distribution, and its own outflow speed. After a brief summary of near-limb measurements made with the SUMER instrument on SOHO, this section mainly describes results at larger heights (in the more clearly collisionless extended corona) from UVCS.

The un-occulted SUMER (Solar Ultraviolet Measurements of Emitted Radiation) spectrometer has ob-

served off-limb regions up to heights of approximately 1.3 R⊙ in coronal holes (Wilhelm et al., 1995, 2000, 2004, 2007). In polar regions at solar minimum, ion temperatures exceed electron temperatures even at r ∼ 1.05 R⊙, where densities were presumed to be so high as to ensure rapid collisional coupling and thus equal temperatures for all species (Seely et al., 1997; Tu et al., 1998; Landi and Cranmer, 2009). Spectro- scopic evidence is also mounting for the presence of transverse Alfvén waves propagating into the corona (Banerjee et al., 1998, 2009; Dolla and Solomon, 2008; Landi and Cranmer, 2009).

Electron temperatures derived from line ratios (Habbal et al., 1993; David et al., 1998; Doschek et al.,

2001; Wilhelm, 2006; Landi, 2008) exhibit relatively low values in the off-limb coronal holes (Te ∼ 800, 000 K) that are not in agreement with higher temperatures derived from “frozen-in” in situ charge states (Ko et al., 1997). It is difficult to reconcile these observations with one another in the absence of either non- Maxwellian electron velocity distributions or strong differential flows between different ion species near the Sun (Esser and Edgar, 2000). However, some models consistent with both the SUMER temperatures and the in situ charge states are being produced (e.g., Laming and Lepri, 2007).

Figure 6 displays a range of temperatures measured in coronal holes and high-speed wind streams, and

it shows how the SUMER electron temperatures (Te ) are noticeably lower than the heavy ion temperatures (e.g., shown for the O+5 ions that correspond to the bright O VI 1032, 1037 Å spectral lines) even in the low corona. The degree of agreement between the spectroscopic measurements and one-fluid models of the low corona (i.e., the semi-empirical model of Avrett and Loeser (2008) and the theoretical model of Cranmer et al. (2007)) depends on the height of the sharp transition region between chromospheric (104 K) and coronal (106 K) temperatures.

The UVCS instrument on SOHO is a combination of an ultraviolet spectrometer and a linearly occulted

coronagraph that observes a 2.5 R⊙ long swath of the extended corona, oriented tangentially to the radial direction at heliocentric distances ranging between about 1.5 and 10 R⊙ (Kohl et al., 1995, 1997, 1998, 2006). In coronal holes, UVCS measurements have allowed many key details about the velocity distribu- tions of H0 , O+5 , and Mg+9 to be derived. For the resonantly scattered emission lines seen at large heights with UVCS, the most straightforward plasma diagnostic is to use the Doppler-broadened line width as a sensitive probe of the overall variance of random particle motions along the line of sight. In other words, measuring the line width provides a constraint on the so-called “kinetic temperature” (i.e., a combination of microscopic stochastic motions and macroscopic [but unresolved] motions due to waves or turbulence) along the direction perpendicular to the (nearly radial) magnetic field lines.

In the ionized solar corona, a given hydrogen nucleus spends most of its time as a free proton, and only

a small fraction of time as a bound H0 atom. Thus, the measured plasma properties of neutral hydrogen are considered to be valid proxies of the proton properties below about 3 R⊙ (Allen et al., 2000). Spartan 201 and UVCS observations of the H I Lyα emission line in coronal holes indicated rather large proton kinetic temperatures in the direction perpendicular to the magnetic field (Tp⊥ ∼ 3 MK) and also the possibility of a mild temperature anisotropy (with Tp⊥ > Tpk ) above heights of 2–3 R⊙ (Kohl et al., 1997; Cranmer et al., 1999b; Antonucci et al., 2004; Kohl et al., 2006).

UVCS observations indicated that the O+5 ions are much more strongly heated than protons in coronal

11


---


Figure 6: Radial dependence of empirical and model temperatures in polar coronal holes and fast wind streams. Mean plasma temperatures from a semi-empirical model (dashed black curve; Avrett and Loeser, 2008) and from a turbulence-driven coronal heating model (solid black curve; Cranmer et al., 2007). Te from off-limb SUMER measurements made by Wilhelm (2006) (dark blue bars) and Landi (2008) (light blue bars), Tp from UVCS measurements assembled by Cranmer (2004b) (see text), and perpendicular O+5 ion temperatures from Landi and Cranmer (2009) (open green circles) and Cranmer et al. (2008) (filled green circles). In situ proton and electron temperatures in the fast wind (r > 60 R⊙ ) are from Cranmer et al. (2009).

holes, with perpendicular temperatures in excess of 200 MK (see Figure 7). This exceeds the temperature at the central core of the Sun by an order of magnitude! The UVCS measurements also provided signa- tures of temperature anisotropies possibly greater than T⊥i /Tki ≈ 10 (e.g., Cranmer et al., 1999b, 2008). The measured kinetic temperatures of O+5 and Mg+9 are significantly greater than mass-proportional when compared with protons, with Ti /Tp > mi /m p (see also Kohl et al., 1999, 2006). The surprisingly “extreme” properties of heavy ions in coronal holes have led theorists to develop a number of new ideas regarding the heating and acceleration of the solar wind; these are discussed further in Section 5.4.

Figure 6 shows UVCS perpendicular temperatures for protons and O+5 ions in coronal holes. The O+5

data points were taken from the recent re-analysis of solar minimum data from 1996–1997 by Cranmer et al. (2008). The proton temperature data were assembled by Cranmer (2004b) from a number of indi- vidual measurements of the H I Lyα profile at solar minimum. The sources of these measurements are: Cranmer et al. (1999b) (squares), Esser et al. (1999) (diamonds), Zangrilli et al. (1999) (asterisks), and Antonucci et al. (2000) (triangles). The kinetic proton temperatures are of order 2–3.5 MK, but in Figure 6 we attempted to remove the contribution of nonthermal wave broadening. The semi-empirical model of Cranmer and van Ballegooijen (2005) was used to specify the amplitude of transverse Alfvén waves as a function of height, and their contribution to the line widths was subtracted. The remaining “microscopic” T⊥p does not show as clear a signal of “preferential” proton heating as would be apparent from the larger kinetic temperature. Although one can still marginally see that Tp > Te , the existing measurements of Tp and Te do not fully overlap with one another in radius. Improved measurements are needed in order to better constrain the proton and electron heating rates in the corona.

The UVCS emission line data contain information about the Doppler motions of atoms and ions along

the magnetic field (i.e., transverse to the line of sight). The so-called “Doppler dimming” diagnostic tech-

12


---


Figure 7: Combined image of the solar corona from 17 August 1996, showing the solar disk in Fe XII 195 Å intensity from EIT (yellow inner image) and the extended corona in O VI 1032 Å intensity from UVCS (red outer image). Axisymmetric field lines are from the solar-minimum model of Banaszkiewicz et al. (1998), and O VI emission line profiles (bottom) are from SUMER (Warren et al., 1997, left) and UVCS (Kohl et al., 1997, right).

nique provides constraints on both the bulk outflow speed along the field and the parallel kinetic tempera- ture (for more details, see Kohl and Withbroe, 1982; Noci et al., 1987; Kohl et al., 2006). In coronal holes, Doppler-dimmed line intensities from UVCS are consistent with the outflow velocity for O+5 being larger than the outflow velocity for protons by as much as a factor of two at large heights (Kohl et al., 1998; Li et al., 1998; Cranmer et al., 1999b). Figure 8 illustrates the outflow speeds measured by UVCS in coronal holes, and compares with the theoretical model of the fast solar wind presented by Cranmer et al. (2007). Also shown for comparison are observational and theoretical data for the slow solar wind associated with equatorial helmet streamers at solar minimum.

In contrast to many prior analyses of UVCS data, which concluded that there must be both intense

preferential heating of the O+5 ions and a strong field-aligned anisotropy, Raouafi and Solanki (2004), Raouafi and Solanki (2006), and Raouafi et al. (2007) reported that there may not be a compelling need for O+5 anisotropy depending on the assumptions made about the other plasma properties of the coronal hole (e.g., electron density). However, Cranmer et al. (2008) performed a detailed re-analysis of these observations and concluded that there remains strong evidence in favor of both preferential O+5 heating and acceleration and significant O+5 ion anisotropy (in the sense T⊥i > Tki ) above r ≈ 2.1 R⊙ in coronal holes. In determining these properties, it was found to be important to search the full range of possible

13


---


Figure 8: Radial dependence of solar wind outflow speeds. UVCS Doppler dimming determinations for protons (red; Kohl et al., 2006) and O+5 ions (green; Cranmer et al., 2008) are shown for polar coronal holes, and are compared with theoretical models of the polar and equatorial solar wind at solar minimum (black curves; Cranmer et al., 2007) and the speeds of “blobs” measured by LASCO above equatorial streamers (open circles; Sheeley Jr et al., 1997).

ion temperatures and flow speeds, and not to make arbitrary assumptions about any given subset of the parameters.

The UVCS results discussed above are similar in character to in situ measurements made in the fast so-

lar wind, but they imply more extreme departures from thermodynamic equilibrium in the extended corona. For example, proton velocity distributions measured in the fast solar wind between 0.3 and 1 AU have anisotropic cores with Tp⊥ > Tpk , and their magnetic moments increase with increasing distance; this im- plies net input of perpendicular energy on kinetic scales (e.g., Marsch et al., 1982; Marsch, 2006). Many heavy ions appear to flow faster than the protons by about the local Alfvén speed (Hefti et al., 1998; Reisen- feld et al., 2001), and in the fastest solar wind streams they are also heated preferentially in the same sense as in the corona (Collier et al., 1996).

In the years since the solar minimum of 1996–1997, UVCS observed a large number of other coronal

holes that appeared throughout the maximum of solar cycle 23 and the new-millennium solar minimum of 2007–2009. UVCS tends to observe only the largest coronal holes, since when the smallest holes rotate to the solar limb their UV line profiles tend to be contaminated by emission from streamers in the foreground and background. This selection effect naturally screens out small coronal holes that have been correlated with slow solar wind streams at 1 AU (Nolte et al., 1976; Neugebauer et al., 1998). In the cases where UVCS and in situ measurements were made for the same regions associated with large coronal holes, high speeds in excess of 600 km s−1 were inevitably seen in interplanetary space (Miralles et al., 2004, 2006). However, the O+5 outflow speeds measured in the extended corona via Doppler dimming have showed a substantial range of variation. For example, Miralles et al. (2001a) found that the outflow speeds at 2–3 R⊙ in an equatorial coronal hole were approximately three times lower than those measured in the polar coronal holes from 1996–1997 at similar heights (see also Poletto et al., 2002). This implies that the range of coronal heights over which the acceleration of the solar wind occurs can vary greatly, even when the

14


---


wind at 1 AU ends up similarly fast.

UVCS also has measured the plasma properties in bright polar plumes. The densest concentrations of

polar plumes along the line of sight are seen to exhibit narrower line widths – i.e., lower kinetic tempera- tures – than the lower-density interplume regions (Kohl et al., 1997; Noci et al., 1997; Kohl et al., 2006). Similarly, plumes are seen to have lower outflow speeds than the interplume regions (Giordano et al., 2000; Teriaca et al., 2003; Raouafi et al., 2007), although at low heights the data are not as clear-cut (e.g., Gabriel et al., 2003). UVCS also has put constraints on the plume/interplume density contrast and the filling factor of polar plumes in coronal holes. Cranmer et al. (1999b) used a large number of UVCS synoptic mea- surements to determine statistically that, at heights around r ≈ 2 R⊙ , the plume/interplume density ratio is approximately 2, and polar coronal holes are comprised of about 25% plume and 75% interplume plasma (corresponding to ∼40 individual plumes distributed throughout the coronal hole). Earlier measurements made closer to the limb showed a higher density contrast and a smaller filling factor, so the UVCS data are generally consistent with lateral expansion of polar plumes with increasing distance.

It is still relatively unknown how much of the mass, momentum, and energy flux of the fast solar wind

comes from polar plumes. Despite that uncertainty, though, there have been several reasonably successful models of polar plume formation. Wang (1994, 1998) presented models of polar plumes as the extensions of flux tubes with concentrated bursts of added coronal heating at the base – presumably via nanoflare-like reconnection events in X-ray bright points (see also DeForest et al., 2001). In these models, the extra basal heat input is balanced by conductive losses to produce the larger plume density. The heating rate in the extended corona is not affected by the basal burst, but the larger density in the flux tube gives rise to less heating per particle at all heights, which leads to lower temperatures in the extended corona and a smaller gas pressure force for solar wind acceleration. This model is consistent with the smaller temperatures and outflow speeds measured in plumes with UV spectroscopy.

UVCS made the first spectroscopic measurements of polar jets in coronal holes (Dobrzycka et al., 2000,

2006). The events observed by EIT, LASCO, and UVCS during the 1996–1997 solar minimum tended to be “cool jets” with higher densities, lower temperatures, and faster outflows than the surrounding coronal holes (see also Wang et al., 1998). More recently, Hinode has observed a new population of “hot” X-ray jets in coronal holes (Culhane et al., 2007; Cirtain et al., 2007; Shimojo et al., 2007; Filippov et al., 2009). UVCS found that some of these events persist up to heights of at least 1.7 R⊙ and that the jet protons remain hotter than the surrounding coronal hole (Miralles et al., 2007). Thus, there appear to exist two distinct kinds of polar jets (cool and hot), with differences possibly related to the relative degrees of heating and adiabatic expansion of the jet parcels. Jets and plumes have roughly similar angular sizes and intensity contrasts near the solar limb, and there is growing evidence that they share a common origin (e.g., Raouafi et al., 2008). It is possible that the only substantial difference between the two phenomena is the duration of the bursts of basal heating; i.e., jets seem to be the result of short-lived bursts of heating, whereas plumes may be the product of base-heating events that last longer than several hours.

# 5 Coronal Heating and Solar Wind Acceleration

Despite more than a half-century of study, the basic physical processes that are responsible for heating the million-degree corona and accelerating the supersonic solar wind are not known. This section broadens the topic of this paper a bit beyond just coronal holes, since an understanding of solar wind acceleration naturally encompasses not only the question of why fast solar wind streams are fast, but also why (various kinds of) slow solar wind streams are slow. Section 5.1 summarizes some of the major issues regarding coronal energy deposition. The next two subsections describe two alternate views of solar wind acceleration via waves and turbulence in open flux tubes (Section 5.2) and reconnection between open and closed flux tubes (Section 5.3). Lastly, Section 5.4 reviews how collisionless kinetic effects in coronal holes (i.e., preferential ion heating and temperature anisotropies) can be used to more conclusively identify the detailed physical processes that produce the solar wind.

15


---


## 5.1 Sources of energy

Different physical mechanisms for heating the corona probably govern active regions, closed loops in the quiet corona, and the open field lines that give rise to the solar wind (see other reviews by Marsch, 1999; Hollweg and Isenberg, 2002; Longcope, 2004; Gudiksen, 2005; Aschwanden, 2006; Klimchuk, 2006). The ultimate source of the energy is the solar convection zone (e.g., Abramenko et al., 2006b; McIntosh et al., 2007). A key aspect of solving the “coronal heating problem” is thus to determine how a small fraction of that mechanical energy is transformed into magnetic free energy and thermal energy above the photosphere. It seems increasingly clear that loops in the low corona are heated by small-scale, intermittent magnetic reconnection that is driven by the continual stressing of their magnetic footpoints. However, the extent to which this kind of impulsive energy addition influences the acceleration of the solar wind is not yet known.

Intertwined with the coronal heating problem is the heliophysical goal of being able to make accurate

predictions of how both fast and slow solar wind streams are accelerated. Empirical correlation techniques have become more sophisticated and predictively powerful (e.g., Wang and Sheeley Jr, 1990, 2006; Arge and Pizzo, 2000; Leamon and McIntosh, 2007; Cohen et al., 2007; Vršnak et al., 2007) but they are limited because they do not identify or utilize the physical processes actually responsible for solar wind accelera- tion. There seem to be two broad classes of physics-based models that attempt to self-consistently answer the question: “How are fast and slow wind streams heated and accelerated?”

1. In wave/turbulence-driven (WTD) models, it is generally assumed that the convection-driven jostling

of magnetic flux tubes in the photosphere drives wave-like fluctuations that propagate up into the ex-

tended corona. These waves (usually Alfvén waves) are often proposed to partially reflect back down

toward the Sun, develop into strong MHD turbulence, and dissipate over a range of heights. These

models also tend to explain the differences between fast and slow solar wind not by any major dif-

ferences in the lower boundary conditions, but instead as an outcome of different rates of lateral

flux-tube expansion over several solar radii as the wind accelerates (see, e.g., Hollweg, 1986; Wang

and Sheeley Jr, 1991; Matthaeus et al., 1999; Cranmer, 2005; Suzuki, 2006; Suzuki and Inutsuka,

2006; Cranmer et al., 2007; Verdini and Velli, 2007; Verdini et al., 2009).

2. In reconnection/loop-opening (RLO) models, the flux tubes feeding the solar wind are assumed to

be influenced by impulsive bursts of mass, momentum, and energy addition in the lower atmosphere.

This energy is usually assumed to come from magnetic reconnection between closed, loop-like mag-

netic flux systems (that are in the process of emerging, fragmenting, and being otherwise jostled by

convection) and the open flux tubes that connect to the solar wind. These models tend to explain

the differences between fast and slow solar wind as a result of qualitatively different rates of flux

emergence, reconnection, and coronal heating at the basal footpoints of different regions on the Sun

(see, e.g., Axford and McKenzie, 1992, 1997; Fisk et al., 1999; Ryutova et al., 2001; Markovskii

and Hollweg, 2002, 2004; Fisk, 2003; Schwadron and McComas, 2003; Woo et al., 2004; Fisk and

Zurbuchen, 2006).

It is notable that both the WTD and RLO models have recently passed some basic “tests” of comparison with observations. Both kinds of model have been shown to be able to produce fast (v > 600 km/s), low- density wind from coronal holes and slow (v < 400 km/s), high-density wind from streamers rooted in quiet regions. Both kinds of model also seem able to reproduce the observed in situ trends of how frozen-in charge states and the FIP effect vary between fast and slow wind streams.

The fact that both sets of ideas described above seem to mutually succeed at explaining the fast/slow

solar wind could imply that a combination of both ideas would work best. However, it may also imply that the existing models do not yet contain the full range of physical processes – and that once these are included, one or the other may perform noticeably better than the other. It also may imply that the comparisons with observations have not yet been comprehensive enough to allow the true differences between the WTD and RLO ideas to be revealed.

16


---


Several recent observations have pointed to the importance of understanding the relationships and dis- tinctions between the WTD and RLO models. The impulsive polar jets discussed in Section 4 may be evidence that that magnetic reconnection drives some fraction of the fast solar wind (see also Fisk, 2005; Moreno-Insertis et al., 2008; Pariat et al., 2009). Also, direct observations of Alfvén waves above the solar limb indicate the highly intermittent nature of how kinetic energy is distributed in spicules, loops, and the open-field corona (De Pontieu et al., 2007; Tomczyk et al., 2007; Tomczyk and McIntosh, 2009). Spectro- scopic observations of blueshifts in the chromospheric network have long been interpreted as the launching points of solar wind streams, but it remains unclear how nanoflare-like events or loop-openings contribute to the interpretation of these diagnostics (He et al., 2007; Aschwanden et al., 2007; McIntosh et al., 2007). Even out in the in situ solar wind – far above the roiling “furnace” of flux emergence at the Sun – there remains evidence for ongoing reconnection (Gosling et al., 2005; Gosling and Szabo, 2008). There is also evidence that the dominant range of turbulence timescales measured in interplanetary space (i.e., tens of minutes to hours) is related to the timescale of flux cancellation in the low corona (Hollweg, 1990, 2006).

Determining whether the WTD or RLO paradigm – or some combination of the two – is the dominant

cause of global solar wind variability is a key prerequisite to building physically realistic predictive models of the heliosphere. Many of the widely-applied global modeling codes (e.g., Riley et al., 2001; Roussev et al., 2003; Tóth et al., 2005; Usmanov and Goldstein, 2006; Feng et al., 2007) continue to utilize relatively simple empirical prescriptions for coronal heating in the energy conservation equation. Improving the identification and characterization of the key physical processes will provide a clear pathway for inserting more physically realistic coronal heating “modules” into three-dimensional MHD codes.

## 5.2 The Wave/Turbulence-Driven (WTD) solar wind idea

There has been substantial work over the past few decades devoted to exploring the idea that the plasma heating and wind acceleration along open flux tubes may be explained as a result of wave damping and tur- bulent cascade. No matter the relative importance of reconnections and loop-openings in the low corona, we do know that waves and turbulent motions are present everywhere from the photosphere to the heliosphere, and it is important to determine how they affect the mean state of the plasma. A review of the observational evidence for waves and turbulence in the solar wind is beyond the scope of this paper, but several recent reviews of the remote-sensing and in situ data include Tu and Marsch (1995), Mullan and Yakovlev (1995), Goldstein et al. (1997), Roberts (2000), Bastian (2001), and Cranmer (2002a, 2004a, 2007). Although this subsection mainly describes recent work by the author, these results would not have been possible without earlier work on wave/turbulent heating by, e.g., Coleman (1968), Hollweg (1986), Hollweg and Johnson (1988), Isenberg (1990), Li et al. (1999), Matthaeus et al. (1999), Dmitruk et al. (2001, 2002), and many others.

Cranmer et al. (2007) described a set of models in which the time-steady plasma properties along a one-

dimensional magnetic flux tube are determined. These model flux tubes are rooted in the solar photosphere and are extended into interplanetary space. The numerical code developed in that work, called ZEPHYR, solves the one-fluid equations of mass, momentum, and energy conservation simultaneously with transport equations for Alfvénic and acoustic wave energy. ZEPHYR is the first code capable of producing self- consistent solutions for the photosphere, chromosphere, corona, and solar wind that combine: (1) shock heating driven by an empirically guided acoustic wave spectrum, (2) extended heating from Alfvén waves that have been partially reflected, then damped by anisotropic turbulent cascade, and (3) wind acceleration from gradients of gas pressure, acoustic wave pressure, and Alfvén wave pressure.

The only input “free parameters” to ZEPHYR are the photospheric lower boundary conditions for the

waves and the radial dependence of the background magnetic field along the flux tube. The majority of heating in these models comes from the turbulent dissipation of partially reflected Alfvén waves (see also Matthaeus et al., 1999; Dmitruk et al., 2002; Verdini and Velli, 2007; Chandran et al., 2009a). Photospheric measurements of the horizontal motions of strong-field intergranular flux concentrations (i.e., G-band bright points) were used to constrain the Alfvén wave power spectrum at the lower boundary. This empirically

17


---


determined power spectrum is dominated by wave periods of order 5–10 minutes. It is important to note, however, that radio and in situ measurements find that most of the fluctuation power in the solar wind is at lower frequencies (i.e., periods of hours). We still do not yet know (1) if the shape of the power spectrum evolves significantly between the lower solar atmosphere and interplanetary space, or (2) if some low-frequency power is missed by the existing measurements of G-band bright point motions. In any case, as seen below, the resulting wave reflection and turbulent dissipation that comes from just the 5–10 minute periods appear to be sufficient to explain the observed levels of coronal heating and solar wind acceleration.

Non-WKB wave transport equations were solved to determine the degree of linear reflection at heights

above the photospheric base (see Cranmer and van Ballegooijen, 2005). The resulting values of the Elsasser amplitudes Z± , which denote the energy contained in upward (Z− ) and downward (Z+ ) propagating waves, were then used to constrain the energy flux in the cascade. Cranmer et al. (2007) used a phenomenological form for the damping rate that has evolved from studies of Reduced MHD and comparisons with numerical simulations. The resulting heating rate (in units of erg s−1 cm−3 ) is given by

Z− Z+ + Z+2 Z−

                      2

1

Q=ρ                                                                    (1)

1 + [teddy/tref ] n      4L⊥ where ρ is the mass density and L⊥ is an effective perpendicular correlation length of the turbulence (see, e.g., Hossain et al., 1995; Zhou and Matthaeus, 1990; Breech et al., 2008; Podesta and Bhattacharjee, 2009; Beresnyak and Lazarian, 2009). Cranmer et al. (2007) used a standard assumption that L⊥ scales with the cross-sectional width of the flux tube (Hollweg, 1986). The term in parentheses above is an efficiency factor that accounts for situations in which the cascade does not have time to develop before the waves or the wind carry away the energy (Dmitruk and Matthaeus, 2003). In open field regions, the cascade is “quenched” when the nonlinear eddy time scale teddy becomes much longer than the macroscopic wave reflection time scale tref . In closed field regions, the correction factor may behave in an opposite sense as it does for open field regions (see, e.g., Gómez et al., 2000; Rappazzo et al., 2008). In most of the solar wind models, though, Cranmer et al. (2007) used n = 1 in equation (1) based on analytic and numerical results (Dobrowolny et al., 1980; Oughton et al., 2006), but they also tried n = 2 to explore a stronger form of the quenching effect.

Figure 9 summarizes the results of varying the magnetic field properties while keeping the lower bound-

ary conditions fixed. For a single choice for the photospheric wave properties, the models produced a real- istic range of slow and fast solar wind conditions. A two-dimensional model of coronal holes and streamers at solar minimum reproduces the latitudinal bifurcation of slow and fast streams seen by Ulysses. An active- region-like enhancement of the magnetic field strength in the low corona generates a high mass flux and a slow wind speed, in agreement with observations of open field lines connected with active regions (see also Wang et al., 2009). As predicted by earlier studies, a larger coronal “expansion factor” naturally gives rise to a slower and denser wind, higher temperature at the coronal base, and lower-amplitude Alfvén waves at 1 AU.

In these models, the radial gradient of the Alfvén speed affects where the waves are reflected and

damped, and thus whether energy is deposited below or above the Parker (1958a) critical point. Early studies of solar wind energetics (e.g., Leer and Holzer, 1980; Pneuman, 1980; Leer et al., 1982) showed that if there is substantial heating below the critical point, its primary impact is to “puff up” the hydrostatic scale height, drawing more particles into the accelerating wind and thus producing a slower and more massive wind. If most of the heating occurs at or above the critical point, the subsonic atmosphere is relatively unaffected, and the local increase in energy flux has nowhere else to go but into the kinetic energy of the wind (leading to a faster and less dense outflow). The ZEPHYR results shown in Figure 9 display this kind of dichotomy because the superradial expansion creates a much higher critical point over the equatorial regions than over the poles. Additional studies of how and where the mass flux and wind speed are determined include Withbroe (1988), Hansteen and Leer (1995), Hansteen et al. (1997), Janse et al. (2007), and Wang et al. (2009).

Perhaps more surprisingly, varying the coronal expansion factor in the models shown in Figure 9 also

18


---


Figure 9: Summary of Cranmer et al. (2007) models: (a) The adopted solar-minimum field geometry of Banaszkiewicz et al. (1998), with radii of wave-modified critical points marked by symbols. (b) Latitudinal dependence of wind speed at ∼2 AU for models with n = 1 (multi-color curve) and n = 2 (brown curve), compared with data from the first Ulysses polar pass in 1994–1995 (black curve; Goldstein et al., 1996). (c) T (r) for polar coronal hole (red solid curve), streamer edge (blue dashed curve), and strong-field active region (black dotted curve) models.

produces correlative trends that are in good agreement with in situ measurements of commonly measured ion charge state ratios (e.g., O7+ /O6+ ) and FIP-sensitive abundance ratios (e.g., Fe/O). Cranmer et al. (2007) showed that the slowest solar wind streams – associated with active-region fields at the base – can pro- duce a factor of ∼30 larger frozen-in ionization-state ratio of O7+ /O6+ than high-speed streams from polar coronal holes, despite the fact that the temperature at 1 AU is lower in slow streams than in fast streams. Furthermore, when elemental fractionation is modeled using a theory based on preferential wave-pressure acceleration (Laming, 2004, 2009; Bryans et al., 2009), the slow wind streams exhibit a substantial relative buildup of elements with low FIP with respect to the high-speed streams. Although the WTD models uti- lize identical photospheric lower boundary conditions for all of the flux tubes, the self-consistent solutions for the upper chromosphere, transition region, and low corona are qualitatively different. Feedback from larger heights (i.e., from variations in the flux tube expansion rate and the resulting heating rate) extends downward to create these differences.

Another empirical “marker” of heliospheric stream structure is the proton specific entropy, or entropy

per proton, which is often approximated as being proportional to ln(Tp /nγ−1p ), where γ ≈ 1.5 is an empirical adiabatic index for solar wind protons (e.g., Burlaga et al., 1990; Pagel et al., 2004). When measured in regions of the (non-CME) heliosphere where corotating interaction regions have not yet formed shocks, this quantity is seen to clearly distinguish slow wind streams from fast wind streams. Figure 10 shows how the specific entropy is positively correlated with wind speed, both in measurements made by the Solar Wind Electron Proton Alpha Monitor (SWEPAM) instrument on ACE (McComas et al., 1998) and in the Cranmer et al. (2007) ZEPHYR models discussed above. Each model data point was computed independently of the

19


---


Figure 10: Solar wind specific entropy plotted as a function of solar wind speed, computed for both the ZEPHYR models at 1 AU (black symbols, curve) and from ACE/SWEPAM data (blue points).

others. The models had identical lower boundary conditions at the photosphere, and they differed from one another only by having a different radial dependence of the magnetic field. Because entropy should be conserved in the absence of significant small-scale dissipation, the quantity that is measured at 1 AU may be a long-distance proxy for the near-Sun locations of strong coronal heating. In other words, the comparison of measured and modeled solar wind entropy variations may be a key way to discriminate between competing explanations of solar wind acceleration.

Although equation (1) describes the plasma heating rate in terms of the local properties of MHD turbu-

lence, it is also possible to see that this expression gives a heating rate proportional to the mean magnetic flux density at the coronal base. As illustrated above in Figure 4, the mean field strength in the low corona is determined by both the photospheric field strength in the intergranular bright points and the total number of bright points that eventually merge their fields together in the low corona. The field strength at this merg- ing height can thus be estimated as B ≈ f∗ B∗ , where B∗ ≈ 1500 G is the (nearly universal) photospheric bright-point field strength and f∗ is the area filling factor of bright points in the photosphere. The latter quantity appears to vary by more than an order of magnitude in different regions on the Sun, from about 0.002 (at low latitudes at solar minimum) to ∼0.1 (in active regions). If the regions below the merging height can be treated using approximations from “thin flux tube theory” (e.g., Spruit, 1981; Cranmer and van Ballegooijen, 2005), then it is possible to express each term in equation (1) as a function of f∗ and the photospheric properties. For example, B ∝ ρ1/2 applies to thin flux tubes in pressure equilibrium, and thus ρ at the merging height can be estimated as f∗2 ρ∗ (where ρ∗ is the photospheric density). For Alfvén waves at low heights, Z± ∝ ρ−1/4 , and so Z± at the merging height scales like Z±∗ / f∗ . Also, we assumed that

1/2

L⊥ ∝ B−1/2 . If the quenching factor in parentheses in equation (1) is neglected, then

−3/2

ρZ 3     ρ∗ Z∗3 f∗2 f∗

       

Q≈         ≈              −1/2

≈ Q∗ f ∗ .                              (2)

L⊥       L⊥∗      f∗ Equivalently, equation (2) implies that Q/Q∗ ≈ B/B∗ , and thus that the heating in the low corona scales directly with the mean magnetic field strength there. In a more highly structured field, the latter is equivalent to the magnetic “flux density” averaged over a given region. Observational evidence for such a linear scaling

20


---


has been found for both a variety of solar regions and other stars as well (see, e.g., Pevtsov et al., 2003; Schwadron et al., 2006; Suzuki, 2006; Kojima et al., 2007; Pinto et al., 2009).

## 5.3 The Reconnection/Loop-Opening (RLO) solar wind idea

It is clear from observations of the Sun’s highly dynamical “magnetic carpet” (Schrijver et al., 1997; Ti- tle and Schrijver, 1998; Hagenaar et al., 1999) that much of coronal heating is driven by the continuous interplay between the emergence, separation, merging, and cancellation of small-scale magnetic elements. Reconnection seems to be the most likely channel for the injected magnetic energy to be converted to heat (e.g., Priest and Forbes, 2000). Only a small fraction of the photospheric magnetic flux is in the form of open flux tubes connected to the heliosphere (Close et al., 2003). Thus, the idea has arisen that the dom- inant source of energy for open flux tubes is a series of stochastic reconnection events between the open and closed fields (e.g., Fisk et al., 1999; Ryutova et al., 2001; Fisk, 2003; Schwadron and McComas, 2003; Feldman et al., 2005; Schwadron et al., 2006; Schwadron and McComas, 2008; Fisk and Zhao, 2009).

The natural appeal of the RLO idea is evident from the fact that open flux tubes are always rooted in

the vicinity of closed loops (e.g., Dowdy et al., 1986) and that all layers of the solar atmosphere seem to be in continual motion with a wide range of timescales. In fact, observed correlations between the lengths of closed loops in various regions, the electron temperature in the low corona, and the wind speed at 1 AU (Feldman et al., 1999; Gloeckler et al., 2003) are highly suggestive of a net transfer of Poynting flux from the loops to the open-field regions that may be key to understanding the macroscopic structure of the solar wind. The proposed RLO reconnection events may also be useful in generating energetic particles and cross-field diffusive transport throughout the heliosphere (e.g., Fisk and Schwadron, 2001).

Testing the RLO idea using theoretical models seems to be more difficult than testing the WTD idea

because of the complex multi-scale nature of magnetic reconnection. It can be argued that one needs to create fully three-dimensional models of the coronal magnetic field (arising from multiple magnetic elements on the surface) to truly assess the full range of closed/open flux interactions. The idea of modeling the coronal field via a collection of discrete magnetic sources (referred to in various contexts as “magneto- chemistry,” “tectonics,” or “magnetic charge topology”) has been used extensively to study the evolution of the closed-field corona (e.g., Longcope, 1996; Schrijver et al., 1997; Longcope and Kankelborg, 1999; Sturrock et al., 1999; Priest et al., 2002; Beveridge et al., 2003; Barnes et al., 2005; Parnell, 2007; Ng and Bhattacharjee, 2008) but applications to open fields and the solar wind have been rarer (see, however, Fisk, 2005; Tu et al., 2005).

In order to develop the RLO paradigm to the point where it can be tested more quantitatively, several

key questions remain to be answered. For example, how much magnetic flux actually opens up in the magnetic carpet? Also, what is the time and space distribution of reconnection-driven energy addition into the (transiently) open flux tubes? Lastly, how is the reconnection energy distributed into various forms (e.g., bulk kinetic energy in “jets,” thermal energy, waves, turbulence, and energetic particles) that each affect the accelerating solar wind in different ways? Combinations of simulations, analytic scaling relations, and observations are needed to make further progress.

## 5.4 Kinetic microphysics

The theoretical models discussed in the previous two subsections mainly involved a “one-fluid” or MHD approach to the coronal heating and solar wind acceleration. However, at large heights in coronal holes, the collisionless divergence of plasma parameters for protons, electrons, and heavy ions allows the multi- fluid kinetic processes to be distinguished in a more definitive way. The UVCS measurements of strong O+5 preferential heating, preferential acceleration, and temperature anisotropy have spurred a great deal of theoretical work in this direction (see reviews by Hollweg and Isenberg, 2002; Cranmer, 2002a; Marsch, 2005, 2006; Kohl et al., 2006). Specifically, the observed ordering of Ti ≫ Tp > Te and the existence of

21


---


Reconnection events in the low corona generate:

Ion cyclotron resonant Alfvén waves . . . . . . . . . . . . . . . . Tu & Marsch 1997; Cranmer 2000, 2001

Electron beams → ion cyclotron waves . . . . . . . . . . . . . . . . . . . Markovskii & Hollweg 2002, 2004

Fast collisionless shocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Lee & Wu 2000

MHD turbulence in the extended corona generates:

Ion cyclotron waves (“parallel cascade?”), with:

≫ Alfvén and fast-mode nonlinear coupling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Chandran 2005

≫ Three-wave (ion-sound/parametric) coupling . . . . . . . . . . . . . . . . . . . . . . . . . Yoon & Fang 2008

≫ Fermi-like diffusion between inward/outward wave resonances . . . . . . . . . . . . . Isenberg 2001

Kinetic Alfvén waves (“perpendicular cascade”), with:

≫ Shear instabilities → ion cyclotron waves . . . . . . . . . . . . . . . . . . . . . . . . Markovskii et al. 2006

≫ Nonlinear wave-particle resonances . . . . . . . . . . . . . . . . . . . . Voitenko & Goossens 2003, 2004

≫ Debye-scale electron holes . . . . . . . . . . . . Matthaeus et al. 2003; Cranmer & van Balle. 2003

Oblique MHD waves (high kk , high k⊥ ) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Li & Habbal 2001

Current sheets → coherent Fermi acceleration . . . . . . . . . . . . . . . . . . . . . . . . . . . Dmitruk et al. 2004

Transverse density gradients → drift currents . . . . . . . . . . . . . . . . . . Markovskii 2001; Zhang 2003

Low-frequency Alfvén waves in the corona directly undergo:

Polarization drift → lower-hybrid waves . . . . . . . . . . . . . . . . . . . . . . Singh & Khazanov 2004, 2007

Nonresonant stochastic heating . . . . . . . . . . . . . . . . . . . . . . . . . . . . Lu & Li 2007; Wu & Yoon 2007

Stochastic heating at fractional cyc. resonance . . . . . . . . . . . . . . Chen et al. 2001; Guo et al. 2008

Heavy ion velocity filtration . . . . . . . . . . . . . . . . . . . . . . Pierrard & Lamy 2003; Pierrard et al. 2004

Figure 11: Tabular outline of suggested physical processes for preferentially heating and accelerating minor ions in coronal holes.

anisotropies of the form T⊥ > Tk in coronal holes led to a resurgence of interest in models of ion cyclotron resonance.

The ion cyclotron heating mechanism is a classical resonance between left-hand polarized Alfvén waves

and the Larmor gyrations of positive ions around the background magnetic field. If the wave frequency and the natural ion gyrofrequency are equal, then in the rest frame of the ion the oscillating electric and magnetic fields of the wave are no longer felt by the ion to be oscillating. The ion in such a frame senses a constant DC electric field, and it can secularly gain or lose energy depending on the relative phase between the ion’s velocity vector and the electric field direction. In a wave field with random phases, an ion will undergo a random walk in energy. Thus, on average the ions can be considered to “diffuse” into faster (i.e., wider) Larmor orbits with larger perpendicular energy (see Rowlands et al., 1966; Galinsky and Shevchenko, 2000; Isenberg, 2001; Cranmer, 2001; Isenberg and Vasquez, 2009).

In the actual solar corona, however, it is not likely that the situation is as straightforward as summarized

above. Instead of a population of pre-existing, linear cyclotron waves that are dissipated, there may be a rich variety of nonlinear plasma mechanisms at play. The observed ion heating is likely to be just the final stage of a multi-step process of energy conversion between waves, turbulent motions, reconnection structures, and various kinds of distortions in the particle velocity distributions. Figure 11 surveys the field of suggested possibilities, and the remainder of this section discusses these ideas in more detail.

One potential obstacle to the idea of ion cyclotron heating is that the required gyroresonant wave fre-

quencies in the corona are of order 102 to 104 Hz, whereas the dominant frequencies of Alfvén waves believed to be emitted by the Sun are thought to be much lower (i.e., less than 0.01 Hz, corresponding to periods of minutes to hours). Axford and McKenzie (1992) suggested that the right kinds of high-frequency waves may be generated in small-scale reconnection events in the chaotic “furnace” of the supergranular

22


---


network. These waves could propagate upwards in height – and downwards in magnetic field strength – until they reached a location where they became cyclotron resonant with the local ions, and thus would damp rapidly to provide the ion heating (see also Schwartz et al., 1981; Tu and Marsch, 1997).

The above scenario of “basal generation” of ion cyclotron waves has been called into question for several

reasons. Cranmer (2000, 2001) argued that the passive sweeping of a pre-existing fluctuation spectrum would involve ions with low gyrofrequencies (i.e., small ratios of charge to mass; qi /mi ≈ 0.1 to 0.2 in proton units) encountering waves of a given frequency at lower heights than the ions that have been observed to exhibit preferential heating, like O+5 (qi /mi = 0.31) and Mg+9 (qi /mi = 0.37). Thus, the resonances of many minor ion species may be strong enough to damp out a base-generated spectrum of waves before they can become resonant with the observed species. Furthermore, Hollweg (2000) found that a base- generated spectrum of ion cyclotron waves would exhibit a very different appearance in interplanetary radio scintillations than the observed radio data. There remains some uncertainty about these criticisms of a basal spectrum of ion cyclotron waves, and definitive conclusions cannot yet be made (see discussions in Tu and Marsch, 2001; Hollweg and Isenberg, 2002).

There are several other interesting consequences of the Axford and McKenzie (1992) idea of rapid re-

connection events at the coronal base. It is possible, for example, that such microflaring activity would give rise to intermittent bursts of parallel electron beams that propagate up into the extended corona. Sufficiently strong beams may be unstable to the growth of wave power at the ion cyclotron frequencies (Markovskii and Hollweg, 2002, 2004; Voitenko and Goossens, 2002), and these waves would then go on to heat the ions. Also, Lee and Wu (2000) suggested that small-scale reconnection events could produce fast collisionless shocks in the extended corona. For shocks sufficiently thin and strong (i.e., with a bulk velocity jump of at least ∼0.3 times the Alfvén speed), ions that cross from one side of the shock to the other remain “nonde- flected” by the rapid change in direction of the magnetic field. Thus, they can convert some of their parallel motion into perpendicular gyration. Mancuso et al. (2002) suggested this mechanism may be applied to understanding UVCS measurements of ion heating in shocks associated with CMEs. However, it is unclear to what extent the open magnetic regions in coronal holes are filled with sufficiently strong shocks to enable this process to occur (see also Hollweg and Isenberg, 2002).

In contrast to the ideas of base-generation of ion cyclotron waves, there have been several proposed

mechanisms for “gradual generation” of these waves over a range of distances in the corona and solar wind. A natural way to produce such an extended source of fluctuations is MHD turbulent cascade, which continually transports power at large scales to small scales via the stochastic shredding of transient eddies. A strong turbulent cascade is certainly present in interplanetary space (see reviews by Tu and Marsch, 1995; Goldstein et al., 1997). It is well known, though, that in both numerical simulations and analytic descriptions of Alfvén-wave turbulence (with a strong background “guide field” like in the corona) the cascade from large to small length scales (i.e., from small to large wavenumbers) occurs most efficiently for modes that do not increase in frequency. In other words, the cascade acts most rapidly to increase the perpendicular wavenumber k⊥ while leaving the parallel wavenumber kk largely unchanged (e.g., Strauss, 1976; Shebalin et al., 1983; Goldreich and Sridhar, 1995; Cho et al., 2002; Oughton et al., 2004). This type of cascade is expected to generate so-called kinetic Alfvén waves (KAWs) with k⊥ ≫ kk , but not ion cyclotron waves.

Under typical “low plasma beta” conditions in the corona and fast solar wind, the linear dissipation of

KAWs would lead to the preferential parallel heating of electrons (Leamon et al., 1999; Cranmer and van Ballegooijen, 2003; Gary and Borovsky, 2008). This is essentially the opposite of what has been observed with UVCS. However, there have been several suggestions for more complex (nonlinear or multi-step) processes that may be responsible for ions to receive perpendicular heating from KAW-type fluctuations.

1. Markovskii et al. (2006) discussed how a perpendicular turbulent cascade produces increasingly

strong shear motions transverse to the magnetic field, and that this shear may eventually be un-

stable to the generation of cyclotron resonant waves that can in turn heat protons and ions (see also

Mikhailenko et al., 2008). This effect may also produce a steepening in the power spectrum of the

magnetic field fluctuations that agrees with the observed “dissipation range” (Smith et al., 2006).

23


---


2. Voitenko and Goossens (2003, 2004) suggested that high-k⊥ KAWs with sufficiently large amplitudes

could begin to exhibit nonlinear resonance effects (“demagnetized wave phases”) leading to rapid ion

perpendicular heating. There are definite thresholds in the KAW amplitude that must be exceeded for

these mechanisms to be initiated, and it is unclear whether the actual coronal turbulent spectrum has

enough power in the relevant regions of wavenumber space (see also Wu and Yang, 2006, 2007).

3. The damping of low-frequency KAWs may give rise to substantial parallel electron acceleration. If

the resulting electron velocity distributions were sufficiently beamed, they could become unstable to

the generation of parallel Langmuir waves. In turn, the evolved Langmuir wave trains may exhibit a

periodic electric potential-well structure in which some of the beam electrons can become trapped.

Adjacent potential wells can then merge with one another to form isolated “electron phase space

holes” of saturated potential. Ergun et al. (1999), Matthaeus et al. (2003), and Cranmer and van

Ballegooijen (2003) described how these tiny (Debye-scale) electrostatic structures can heat ions

perpendicularly via Coulomb-like quasi-collisions.

4. Obliquely propagating MHD waves with large perpendicular and parallel wavenumbers – including

KAWs and fast-mode waves – can interact resonantly with positive ions via channels that are not

available when either kk or k⊥ are small. Li and Habbal (2001) found that oblique fast-mode waves

with large wavenumbers may be even more efficient than Alfvén waves at heating ions under coronal

conditions. Hollweg and Markovskii (2002) discussed how the higher-order cyclotron resonances

become available to obliquely propagating waves with large wavenumbers, and how these can lead

to stochastic velocity-space diffusion for ions.

5. On the smallest spatial scales, the plasma in numerical simulations of MHD turbulence is seen to

develop into a collection of narrow current sheets undergoing oblique magnetic reconnection (i.e.,

with the strong “guide field” remaining relatively unchanged). Dmitruk et al. (2004) performed

test-particle simulations in a turbulent plasma and found that protons can become perpendicularly

accelerated around the guide field because of coherent forcing from the perturbed fields associated

with the current sheets (see also Parashar et al., 2009). It remains to be seen whether this process

could lead to more than mass-proportional energization for minor ions.

6. If the plasma contains sufficiently small-scale density gradients transverse to the magnetic field

(∇⊥ ρ), then drift currents can be excited that are unstable to the generation of high-frequency waves

(Markovskii, 2001; Zhang, 2003; Vranjes and Poedts, 2008; Mecheri and Marsch, 2008). These

instabilities depend on both the amplitudes and scale lengths of ∇⊥ ρ. To measure the latter, it is im-

portant to take into account both remote-sensing measurements of coronal density inhomogeneities

(e.g., Woo, 2006; Pasachoff et al., 2007) and constraints from radio scintillation power spectra at

larger distances (Bastian, 2001; Spangler, 2002; Harmon and Coles, 2005).

Despite the fact that theory predicts a predominantly perpendicular cascade, there is some evidence that the turbulent fluctuations in the solar wind have some energy that extends up to large kk values in a power-law tail (see, e.g., Bieber et al., 1996; Dasso et al., 2005; MacBride et al., 2008). Whether or not this means that true “parallel cascade” occurs in the corona and solar wind is still not known. However, some progress has been made using a phenomenological approach to modeling the cascade as a combination of advection and diffusion in wavenumber space. In the model of Cranmer and van Ballegooijen (2003), the relative strengths of perpendicular advection and diffusion determine the slope of the power-law spectrum in kk , and thus they specify the amount of wave energy that is available at the ion cyclotron frequencies (see also Cranmer et al., 1999a; Landi and Cranmer, 2009; Jiang et al., 2009).

There have also been proposals for additional mechanisms that could allow a parallel cascade to occur

in the corona and solar wind. Nonlinear couplings between the dominant Alfvén waves and other modes such as fast magnetosonic waves (Chandran, 2005; Luo and Melrose, 2006) and ion-acoustic waves (Yoon and Fang, 2008) have the potential to enhance the wave power at high frequencies. It has also been known

24


---


for some time that nonlinear coupling between Alfvén and fast-mode waves may help explain why the measured in situ magnetic field magnitude |B| remains roughly constant while its direction varies strongly (Barnes and Hollweg, 1974; Vasquez and Hollweg, 1996, 1998).

If MHD waves have sufficiently large amplitudes, they may undergo nonlinear wave steepening, which

leads to density variations as well as oscillations in the parallel components of the velocity and magnetic field. These may generate progressively smaller scales along the magnetic field (e.g., Medvedev, 2000; Suzuki et al., 2007). There is also a “bootstrap” kind of effect for ion cyclotron wave generation that was discussed by Isenberg et al. (2001). If some outward-propagating cyclotron waves exist, the resonant diffusion may act to produce proton velocity distributions that are unstable to the generation of inward- propagating cyclotron waves. In response, the proton distributions would become further deformed and thus could become unstable to the growth of both inward and outward waves. It is not yet known if this process could reach the point of becoming self-sustaining, but if so, it may also serve as an extended generation mechanism for high-kk waves.

In addition to the above ideas that involve large wavenumbers and kinetic effects, there have been other

suggested physical processes that do not require high-k resonances to be initially present in order to heat the ions.

1. Particles in large-amplitude Alfvén waves exhibit both E × B drift motions (i.e., their standard ve-

locity amplitude) and a polarization drift velocity Vpol that is smaller than the former by the ratio

ω/Ωi , where ω is the wave frequency and Ωi is the ion cyclotron frequency. A sufficiently large Vpol

can lead to cross-field currents unstable to the generation of high-frequency waves, and to eventual

equipartition between Vpol and the ion thermal speed (Singh and Khazanov, 2004; Singh et al., 2007;

Khazanov and Singh, 2007). It is not yet known whether the effective Vpol for the coronal fluctuation

spectrum is large enough to provide a significant fraction of the ion thermal speeds.

2. Recently there have been suggested some completely nonresonant mechanisms that depend on the

stochasticity of MHD turbulence to produce an effective increase in random ion motions (Lu and Li,

2007; Wu and Yoon, 2007; Bourouaine et al., 2008). Questions still remain, though, concerning the

spatial scales over which one should refer to particle motions as “heating” versus “wave sloshing.”

This energization mechanism may be just a more chaotic form of the standard velocity amplitude that

an ion feels when in the presence of a spectrum of Alfvén waves (see, e.g., Wang and Wu, 2009).

In this case, the maximum amount of heating from this process would provide mass-proportional

heating for minor ions and protons (i.e., Ti /Tp = mi /m p ), and it is clear that the UVCS measurements

for O+5 show heating in excess of this amount (see Section 4.3).

3. Both numerical and analytic studies of Alfvén waves show that, at sufficiently large amplitudes, there

can be gyroresonance-like ion energization for sets of frequencies at specific fractions of the local

ion cyclotron resonance frequency (e.g., Chen et al., 2001; Guo et al., 2008). Like several other

processes listed above, this effect becomes active only above certain thresholds of wave amplitude.

Also, Markovskii et al. (2009) showed that mildly nonlinear Alfvén waves – with frequencies slightly

below the local proton gyrofrequency and power in both the upward and downward directions along

the field – can also undergo additional modes of dissipation and proton heating that are not anticipated

in linear ion cyclotron resonance theories.

Finally, there has been some development of the so-called velocity filtration theory, which requires nei- ther direct heating nor wave damping in order to energize coronal ions. Spacecraft measurements of plasma velocity distributions, both in the solar wind and in planetary magnetospheres and magnetosheaths, have revealed that “suprathermal” power-law tails are quite common. These observations led to the suggestion by Scudder (1992a, 1994) of an an alternative to theories that demand explicit energy deposition in the low corona (see also Parker, 1958b; Levine, 1974). A velocity distribution having a suprathermal tail will become increasingly dominated by its high-energy particles at larger distances from the solar gravity well.

25


---


Thus an effective “heating” occurs as a result of particle-by-particle conservation of energy. The major unresolved issue is whether suprathermal tails of the required strength can be produced and maintained in the upper chromosphere and transition region – where Coulomb collisions are traditionally believed to be strong enough to rapidly drive velocity distributions toward Maxwellians. Whether the solar atmosphere actually plays host to strong nonthermal tails is still under debate, with some evidence existing in favor of their presence (e.g., Esser and Edgar, 2000; Ralchenko et al., 2007) and other evidence against them (Anderson et al., 1996; Ko et al., 1996; Feldman et al., 2007).

The original (Scudder, 1992a,b) ideas about suprathermal velocity filtration were applied only to the

primary (proton and electron) coronal plasma. More recently, Pierrard and Lamy (2003) and Pierrard et al. (2004) have shown that this mechanism can produce extremely high temperatures for heavy ions in the corona – providing they had suprathermal tails in the chromosphere. The primary quantities presented in these papers, however, were integrated isotropic temperatures T . No information was given about the predicted sense of the temperature anisotropy for the minor ions. For a collisionless exospheric model, there is a suspicion that a combination of several effects (e.g., the initial velocity filtration and subsequent magnetic moment conservation) would result in velocity distributions with Tk ≫ T⊥ , which is not what is observed.

Since it is obvious that not all of the proposed mechanisms described above (and shown in Figure 11)

can be the dominant cause of the collisionless ion energization in coronal holes, there is a great need to “cut through the jungle” and assess the validity of each of these processes. For many of these suggested ideas, further theoretical development is required so that specific observational predictions can be made. However, there are also several types of measurement that have not been widely recognized or utilized as constraints on theoretical models. A prime example is the use of radio sounding (i.e., interplanetary scintillations and Faraday rotation) to measure the fine structure of the corona and solar wind in density, velocity, and magnetic field strength (see, however, Hollweg and Isenberg, 2002; Spangler, 2002; Harmon and Coles, 2005; Chandran et al., 2009b). Another example is the use of high-resolution UV spectral line profiles to probe departures from Maxwellian or bi-Maxwellian ion velocity distributions (e.g., Cranmer, 2001).

# 6 Summary and Conclusions

The last decade has seen significant progress toward identifying and characterizing the processes that pro- duce coronal holes. As remote-sensing plasma measurements have become possible in the extended solar corona (i.e., the region of primary acceleration of the solar wind), the traditional gap between solar physics and in situ space physics has become narrower. However, there are still many unanswered questions: How and where in the solar atmosphere are the relevant waves and turbulent motions generated? Which kinds of fluctuation modes (i.e., linear or nonlinear; Alfvén, fast, or slow; high kk or high k⊥ ) are most important? What frequencies dominate the radially evolving power spectrum? What fraction of the interplanetary solar wind comes from filamentary structures such as polar plumes and polar jets? Are there relatively simple “scaling laws” that will allow us to use only the measured properties at the solar surface to predict the resulting amount of coronal heating and solar wind acceleration?

Answering the above questions involves moving forward in both the theoretical and observational di-

rections. Section 5 described the large number of suggested physical processes for energizing the plasma in coronal holes. The validity of many of these processes still needs to be assessed, and their relative contri- butions to the heating and acceleration of the actual solar corona need to be quantified. If, at the end of this process, there are still a number of mutually inconsistent theories that are still viable, the only way forward is to determine what future measurements would best put the remaining models to the test. These activ- ities are ongoing with the planning of inner heliospheric missions such as Solar Probe (McComas et al., 2007) and Solar Orbiter (Marsden and Fleck, 2007), as well as next-generation ultraviolet coronagraph spectroscopy missions that would follow up on the successes of UVCS/SOHO (see, e.g., Cranmer, 2002b;

26


---


Figure 12: Illustration of the evolving circumstellar environment of a solar-mass star (see text), showing various kinds of open-field structures that may be analogous to present-day coronal holes.

Gardner et al., 2003; Kohl et al., 2006).

The development of more physically sound models of the solar wind feeds back in many ways to a

wider understanding of stellar outflows and star/planet evolution. Figure 12 shows some of the the early stages of evolution for a representative solar-type star. At all ages, cool stars are inferred to exhibit some kind of wind or jet-like outflow (Lamers and Cassinelli, 1999; Wood, 2004; Güdel, 2007; Cranmer, 2008a). Young stars first become visible as dust-obscured cloud cores and protostars (e.g., Lada, 1985; Hartmann, 2000), and these objects are often associated with bipolar, collimated jets. These outflows indicate some kind of transfer of energy from the accretion disk’s orbital motion to torqued magnetic fields (rooted on the stellar surface) that relieve the buildup of angular momentum and eject plasma out the poles (e.g., Blandford and Payne, 1982; van Ballegooijen, 1994). As the accretion rates decrease over time, protostars become visible as classical T Tauri stars (CTTS), and there remains ample evidence for polar outflows in the form of both “disk winds” and true stellar winds (Hartigan et al., 1995; Ferreira et al., 2006; Cranmer, 2008b). The primordial accretion disk is dissipated gradually as the star enters the weak-lined T Tauri star (WTTS) phase, with a likely transition to a protoplanetary dust/debris disk. Strong stellar magnetic activity remains evident during these stages from, e.g., X-rays (Feigelson and Montmerle, 1999). Many “post T Tauri” stars, once they reach the zero-age main sequence (ZAMS), remain rapidly rotating, and for young ZAMS stars such as AB Dor there is evidence for a range of X-ray emitting plasma from dark polar spots (which probably do not correspond to open magnetic field regions like coronal holes) to huge “slingshot prominences” extending over several stellar radii (e.g., Güdel et al., 2001, 2003; Jardine and van Ballegooijen, 2005).

Learning about the fundamental physics responsible for solar coronal holes has relevance that reaches

into other areas of study besides astrophysics, including plasma physics, space physics, and astronautical engineering. The practical benefits of improving long-term predictions for the conditions of the Earth’s local space environment are manifold (see, e.g., Feynman and Gabriel, 2000; Eastwood, 2008). In addition, parallel research into the expansion of the polar wind from the Earth’s ionosphere has led to an improved understanding of kinetic processes in plasmas on the boundary between collisional and collisionless con- ditions (Lemaire and Pierrard, 2001; Barakat and Schunk, 2006). Finally, a growing realization that strict topical compartmentalization is often a hindrance to making progress has given rise to greater interest in interdisciplinary studies of “universal processes in heliophysics” (Crooker, 2004; Davila et al., 2009).

27


---


# 7 Acknowledgements

I would like to thank the editors of Living Reviews in Solar Physics for the invitation to prepare this review. I gratefully acknowledge John Kohl, Adriaan van Ballegooijen, Leonard Strachan, John Raymond, William Matthaeus, Philip Isenberg, Joseph Hollweg, S. Peter Gary, Eckart Marsch, Marco Velli, Mari Paz Miralles, Larry Gardner, and Enrico Landi for many valuable discussions and collaborations. I would especially like to thank the colleagues with whom I have engaged in more adversarial debates over the years, such as Ian Axford, Chuanyi Tu, Nathan Schwadron, and Nour-Eddine Raouafi. “As brothers fight ye!”

This work was supported by the National Aeronautics and Space Administration (NASA) under grants

NNG04GE77G, NNX06AG95G, NNX07AL72G, and NNX09AB27G to the Smithsonian Astrophysical Observatory. SOHO is a project of international cooperation between ESA and NASA. This research made extensive use of NASA’s Astrophysics Data System (ADS) and the John G. Wolbach Library at the Harvard- Smithsonian Center for Astrophysics.


## References

Abramenko, V.I., Fisk, L.A., Yurchyshyn, V.B., 2006a, “The Rate of Emergence of Magnetic Dipoles in

Coronal Holes and Adjacent Quiet-Sun Regions”, Astrophys. J. Lett., 641, L65–L68.

ADS: http://adsabs.harvard.edu/abs/2006ApJ...641L..65A Abramenko, V.I., Pevtsov, A.A., Romano, P., 2006b, “Coronal Heating and Photospheric Turbulence Pa-

rameters: Observational Aspects”, Astrophys. J. Lett., 646, L81–L84.

ADS: http://adsabs.harvard.edu/abs/2006ApJ...646L..81A Aiouaz, T., Peter, H., Lemaire, P., 2005, “The correlation between coronal Doppler shifts and the super-

granular network”, Astron. Astrophys., 435, 713–721.

ADS: http://adsabs.harvard.edu/abs/2005A&A...435..713A Allen, L.A., Habbal, S.R., Li, X., 2000, “Thermal coupling of protons and neutral hydrogen with anisotropic

temperatures in the fast solar wind”, J. Geophys. Res., 105, 23 123–23 134.

ADS: http://adsabs.harvard.edu/abs/2000JGR...10523123A Altschuler, M.D., Newkirk, G., 1969, “Magnetic fields and the structure of the solar corona, I: Methods of

calculating coronal fields”, Solar Phys., 9, 131–149.

ADS: http://adsabs.harvard.edu/abs/1969SoPh....9..131A Altschuler, M.D., Perry, R.M., 1972, “On Determining the Electron Density Distribution of the Solar

Corona from K-Coronameter Data”, Solar Phys., 23, 410–428.

ADS: http://adsabs.harvard.edu/abs/1972SoPh...23..410A Altschuler, M.D., Trotter, D.E., Orrall, F.Q., 1972, “Coronal Holes”, Solar Phys., 26, 354–365.

ADS: http://adsabs.harvard.edu/abs/1972SoPh...26..354A

Anderson, S.W., Raymond, J.C., van Ballegooijen, A., 1996, “Ultraviolet Emission-Line Intensities and

Coronal Heating by Velocity Filtration: Collisionless Results”, Astrophys. J., 457, 939–948.

ADS: http://adsabs.harvard.edu/abs/1996ApJ...457..939A Andretta, V., Jones, H.P., 1997, “On the Role of the Solar Corona and Transition Region in the Excitation

of the Spectrum of Neutral Helium”, Astrophys. J., 489, 375–394.

ADS: http://adsabs.harvard.edu/abs/1997ApJ...489..375A Andries, J., Goossens, M., 2001, “Kelvin-Helmholtz instabilities and resonant flow instabilities for a coronal

plume model with plasma pressure”, Astron. Astrophys., 368, 1083–1094.

ADS: http://adsabs.harvard.edu/abs/2001A&A...368.1083A

28


---


Antiochos, S.K., DeVore, C.R., Karpen, J.T., Mikić, Z., 2007, “Structure and dynamics of the Sun’s open

magnetic field”, Astrophys. J., 671, 936–946.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...671..936A Antonucci, E., Dodero, M., Giordano, S., 2000, “Fast Solar Wind Velocity in a Polar Coronal Hole during

Solar Minimum”, Solar Phys., 197, 115–134.

ADS: http://adsabs.harvard.edu/abs/2000SoPh..197..115A Antonucci, E., Dodero, M.A., Giordano, S., Krishnakumar, V., Noci, G., 2004, “Spectroscopic measure-

ment of the plasma electron density and outflow velocity in a polar coronal hole”, Astron. Astrophys.,

416, 749–758.

ADS: http://adsabs.harvard.edu/abs/2004A&A...416..749A

Arge, C.N., Pizzo, V.J., 2000, “Improvement in the prediction of solar wind conditions using near-real time

solar magnetic field updates”, J. Geophys. Res., 105, 10 465–10 480.

ADS: http://adsabs.harvard.edu/abs/2000JGR...10510465A Asai, A., Shibata, K., Hara, H., Nitta, N.V., 2008, “Characteristics of Anemone Active Regions Appearing

in Coronal Holes Observed with the Yohkoh Soft X-Ray Telescope”, Astrophys. J., 673, 1188–1193.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...673.1188A Aschwanden, M.J., 2006, Physics of the Solar Corona: An Introduction with Problems and Solutions, 2nd

ed., Springer-Praxis Books in Geophysical Sciences, Springer; Praxis, Berlin; New York; Chichester

Aschwanden, M.J., Winebarger, A., Tsiklauri, D., Peter, H., 2007, “The Coronal Heating Paradox”, Astro-

phys. J., 659, 1673–1681.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...659.1673A Aschwanden, M.J., Nitta, N.V., Wuelser, J.P., Lemen, J.R., Sandman, A., Vourlidas, A., Colaninno, R.C.,

2009, “First Measurements of the Mass of Coronal Mass Ejections from the EUV Dimming Observed

with STEREO EUVI A+B Spacecraft”, Astrophys. J., submitted Avrett, E.H., 1999, “Combined Effects of Mass Flow and Particle Diffusion on the Ionization Structure

of the Solar Transition Region”, in Plasma Dynamics and Diagnostics in the Solar Transition Region

and Corona, (Eds.) Vial, J.-C., Kaldeich-Schümann, B., Proceedings of the 8th SOHO Workshop, 22–25

June 1999, Paris, France, vol. SP-446 of ESA Conference Proceedings, pp. 141–147, ESA Publications

Division, Noordwijk.

ADS: http://adsabs.harvard.edu/abs/1999ESASP.446..141A

Avrett, E.H., Loeser, R., 2008, “Models of the Solar Chromosphere and Transition Region from SUMER

and HRTS Observations: Formation of the Extreme-Ultraviolet Spectrum of Hydrogen, Carbon, and

Oxygen”, Astrophys. J. Suppl. Ser., 175, 229–276.

ADS: http://adsabs.harvard.edu/abs/2008ApJS..175..229A

Axford, W.I., McKenzie, J.F., 1992, “The origin of high speed solar wind streams”, in Solar Wind Seven,

(Eds.) Marsch, E., Schwenn, R., Proceedings of the 3rd COSPAR Colloquium held in Goslar, Germany,

16–20 September 1991, vol. 3 of COSPAR Colloquia Series, pp. 1–5, Pergamon Press, Oxford; New

York

Axford, W.I., McKenzie, J.F., 1997, “The Solar Wind”, in Cosmic Winds and the Heliosphere, (Eds.)

Jokipii, J.R., Sonett, C.P., Giampapa, M.S., Space Science Series, pp. 31–66, Arizona University Press,

Tucson

29


---


Banaszkiewicz, M., Axford, W.I., McKenzie, J.F., 1998, “An analytic solar magnetic field model”, Astron.

Astrophys., 337, 940–944.

ADS: http://adsabs.harvard.edu/abs/1998A&A...337..940B Banerjee, D., Teriaca, L., Doyle, J.G., Wilhelm, K., 1998, “Broadening of Si VIII lines observed in the solar

polar coronal holes”, Astron. Astrophys., 339, 208–214.

ADS: http://adsabs.harvard.edu/abs/1998A&A...339..208B Banerjee, D., Pérez-Suárez, D., Doyle, J.G., 2009, “Signatures of Alfvén waves in the polar coronal holes

as seen by EIS/Hinode”, Astron. Astrophys., 501, L15–L18.

ADS: http://adsabs.harvard.edu/abs/2009A&A...501L..15B Barakat, A.R., Schunk, R.W., 2006, “A three-dimensional model of the generalized polar wind”, J. Geophys.

Res., 111, A12 314.

ADS: http://adsabs.harvard.edu/abs/2006JGRA..11112314B Barnes, A., Hollweg, J.V., 1974, “Large-amplitude hydromagnetic waves”, J. Geophys. Res., 79, 2302–

2318.

ADS: http://adsabs.harvard.edu/abs/1974JGR....79.2302B Barnes, G., Longcope, D.W., Leka, K.D., 2005, “Implementing a Magnetic Charge Topology Model for

Solar Active Regions”, Astrophys. J., 629, 561–571.

ADS: http://adsabs.harvard.edu/abs/2005ApJ...629..561B Bastian, T.S., 2001, “Radio Wave Propagation in the Corona and the Interplanetary Medium”, Astrophys.

Space Sci., 277, 107–116.

ADS: http://adsabs.harvard.edu/abs/2001Ap&SS.277..107B Beckers, J.M., 1968, “Solar Spicules (Invited Review Paper)”, Solar Phys., 3, 367–433.

ADS: http://adsabs.harvard.edu/abs/1968SoPh....3..367B

Bell, B., Noci, G., 1973, “Are Coronal Holes M Regions?”, Bull. Am. Astron. Soc., conference paper.

ADS: http://adsabs.harvard.edu/abs/1973BAAS....5S.269B

Bell, B., Noci, G., 1976, “Intensity of the Fe XV emission line corona, the level of geomagnetic activity,

and the velocity of the solar wind”, J. Geophys. Res., 81, 4508–4516.

ADS: http://adsabs.harvard.edu/abs/1976JGR....81.4508B

Bemporad, A., Matthaeus, W.H., Poletto, G., 2008, “Low-frequency Lyα Power Spectra Observed by

UVCS in a Polar Coronal Hole”, Astrophys. J. Lett., 677, L137–L140.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...677L.137B Beresnyak, A., Lazarian, A., 2009, “Structure of Stationary Strong Imbalanced Turbulence”, Astrophys. J.,

702, 460–471.

ADS: http://adsabs.harvard.edu/abs/2009ApJ...702..460B Berger, T.E., Title, A.M., 2001, “On the Relation of G-Band Bright Points to the Photospheric Magnetic

Field”, Astrophys. J., 553, 449–469.

ADS: http://adsabs.harvard.edu/abs/2001ApJ...553..449B Beveridge, C., Longcope, D.W., Priest, E.R., 2003, “A model for elemental coronal flux loops”, Solar Phys.,

216, 27–40.

ADS: http://adsabs.harvard.edu/abs/2003SoPh..216...27B

30


---


Bieber, J.W., Wanner, W., Matthaeus, W.H., 1996, “Dominant two-dimensional solar wind turbulence with

implications for cosmic ray transport”, J. Geophys. Res., 101, 2511–2522.

ADS: http://adsabs.harvard.edu/abs/1996JGR...101.2511B Blandford, R.D., Payne, D.G., 1982, “Hydromagnetic flows from accretion discs and the production of

radio jets”, Mon. Not. Roy. Astron. Soc., 199, 883–903.

ADS: http://adsabs.harvard.edu/abs/1982MNRAS.199..883B Bourouaine, S., Marsch, E., Vocks, C., 2008, “‘On the efficiency of nonresonant ion heating by coronal

Alfvén waves”, Astrophys. J. Lett., 684, L119–L122.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...684L.119B Breech, B., Matthaeus, W.H., Minnie, J., Bieber, J.W., Oughton, S., Smith, C.W., Isenberg, P.A., 2008,

“Turbulence transport throughout the heliosphere”, J. Geophys. Res., 113, A08 105.

ADS: http://adsabs.harvard.edu/abs/2008JGRA..11308105B Bryans, P., Landi, E., Savin, D.W., 2009, “A New Approach to Analyzing Solar Coronal Spectra and Up-

dated Collisional Ionization Equilibrium Calculations: II, Updated Ionization Rate Coefficients”, Astro-

phys. J., 691, 1540–1559.

ADS: http://adsabs.harvard.edu/abs/2009ApJ...691.1540B

Burlaga, L.F., Mish, W.H., Whang, Y.C., 1990, “Coalescence of recurrent streams of different sizes and

amplitudes”, J. Geophys. Res., 95, 4247–4255.

ADS: http://adsabs.harvard.edu/abs/1990JGR....95.4247B Byhring, H.S., Esser, R., Lie-Svendsen, Ø., 2008, “The Funnel Geometry of Open Flux Tubes in the Low

Solar Corona Constrained by O VI and Ne VIII Outflow”, Astrophys. J. Lett., 673, L91–L94.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...673L..91B Centeno, R., Trujillo Bueno, J., Uitenbroek, H., Collados, M., 2008, “The influence of coronal EUV irradi-

ance on the emission in the He I 10830 Å and D3 multiplets”, Astrophys. J., 677, 742–750.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...677..742C Chae, J., Yun, H.S., Poland, A.I., 1997, “Effects of Non-LTE Radiative Loss and Partial Ionization on the

Structure of the Transition Region”, Astrophys. J., 480, 817–824.

ADS: http://adsabs.harvard.edu/abs/1997ApJ...480..817C Chandran, B.D.G., 2005, “Weak Compressible Magnetohydrodynamic Turbulence in the Solar Corona”,

Phys. Rev. Lett., 95, 265 004.

ADS: http://adsabs.harvard.edu/abs/2005PhRvL..95z5004C Chandran, B.D.G., Quataert, E., Howes, G.G., Hollweg, J.V., Dorland, W., 2009a, “The Turbulent Heating

Rate in Strong MHD Turbulence with Nonzero Cross Helicity”, Astrophys. J., 701, 652–657.

ADS: http://adsabs.harvard.edu/abs/2009ApJ...701..652C Chandran, B.D.G., Quataert, E., Howes, G.G., Xia, Q., Pongkitiwanichakul, P., 2009b, “Constraining Low-

Frequency Alfvénic Turbulence in the Solar Wind Using Density Fluctuation Measurements”, Astrophys.

J., submitted Chen, L., Lin, Z., White, R., 2001, “On resonant heating below the cyclotron frequency”, Phys. Plasmas,

8, 4713–4716.

ADS: http://adsabs.harvard.edu/abs/2001PhPl....8.4713C Chen, Y., Li, X., Song, H.Q., Shi, Q.Q., Feng, S.W., Xia, L.D., 2009, “Intrinsic Instability of Coronal

Streamers”, Astrophys. J., 691, 1936–1942.

ADS: http://adsabs.harvard.edu/abs/2009ApJ...691.1936C

31


---


Cho, J., Lazarian, A., Vishniac, E.T., 2002, “Simulations of Magnetohydrodynamic Turbulence in a

Strongly Magnetized Medium”, Astrophys. J., 564, 291–301.

ADS: http://adsabs.harvard.edu/abs/2002ApJ...564..291C Cirtain, J.W., Golub, L., Lundquist, L., van Ballegooijen, A., Savcheva, A., Shimojo, M., DeLuca, E.,

Tsuneta, S., Sakao, T., Reeves, K., Weber, M., Kano, R., Narukage, N., Shibasaki, K., 2007, “Evidence

for Alfvén waves in solar X-ray jets”, Science, 318, 1580–1582.

ADS: http://adsabs.harvard.edu/abs/2007Sci...318.1580C

Close, R.M., Parnell, C.E., Mackay, D.H., Priest, E.R., 2003, “Statistical Flux Tube Properties of 3D Mag-

netic Carpet Fields”, Solar Phys., 212, 251–275.

ADS: http://adsabs.harvard.edu/abs/2003SoPh..212..251C Cohen, O., Sokolov, I.V., Roussev, I.I., Arge, C.N., Manchester, W.B., Gombosi, T.I., Frazin, R.A., Park,

H., Butala, M.D., Kamalabadi, F., Velli, M., 2007, “A Semiempirical Magnetohydrodynamical Model of

the Solar Wind”, Astrophys. J. Lett., 654, L163–L166.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...654L.163C

Coleman, P.J., 1968, “Turbulence, Viscosity, and Dissipation in the Solar-Wind Plasma”, Astrophys. J., 153,

371–388.

ADS: http://adsabs.harvard.edu/abs/1968ApJ...153..371C Collier, M.R., Hamilton, D.C., Gloeckler, G., Bochsler, P., Sheldon, R.B., 1996, “Neon-20, Oxygen-

16, and Helium-4 densities, temperatures, and suprathermal tails in the solar wind determined with

WIND/MASS”, Geophys. Res. Lett., 23, 1191–1194.

ADS: http://adsabs.harvard.edu/abs/1996GeoRL..23.1191C

Cranmer, S.R., 2000, “Ion Cyclotron Wave Dissipation in the Solar Corona: The Summed Effect of more

than 2000 Ion Species”, Astrophys. J., 532, 1197–1208.

ADS: http://adsabs.harvard.edu/abs/2000ApJ...532.1197C Cranmer, S.R., 2001, “Ion cyclotron diffusion of velocity distributions in the extended solar corona”, J.

Geophys. Res., 106, 24,937–24,954.

ADS: http://adsabs.harvard.edu/abs/2001JGR...10624937C Cranmer, S.R., 2002a, “Coronal Holes and the High-Speed Solar Wind”, Space Sci. Rev., 101, 229–294.

ADS: http://adsabs.harvard.edu/abs/2002SSRv..101..229C

Cranmer, S.R., 2002b, “Solar wind acceleration in coronal holes”, in From Solar Min to Max: Half a

Solar Cycle with SOHO, (Ed.) Wilson, A., Proceedings of the SOHO-11 Symposium, 11–15 March

2002, Davos, Switzerland, vol. SP-508 of ESA Conference Proceedings, pp. 361–366, ESA Publications

Division, Noordwijk.

ADS: http://adsabs.harvard.edu/abs/2002ESASP.508..361C Cranmer, S.R., 2004a, “Observational Aspects of Wave Acceleration in Open Magnetic Regions”, in Waves,

Oscillations, and Small-Scale Transient Events in the Solar Atmosphere, (Ed.) Lacoste, H., Proceedings

of the SOHO–13 Workshop, 29 September–3 October 2003, Palma de Mallorca, Spain, vol. SP-547 of

ESA Conference Proceedings, pp. 353–362, ESA Publications Division, Noordwijk.

ADS: http://adsabs.harvard.edu/abs/2004ESASP.547..353C Cranmer, S.R., 2004b, “Coronal Heating versus Solar Wind Acceleration”, in Coronal Heating, (Eds.)

Walsh, R.W., Ireland, J., Danesy, D., Fleck, B., Proceedings of the SOHO–15 Workshop, 6–9 September

2004, St. Andrews, Scotland, UK, vol. SP-575 of ESA Conference Proceedings, pp. 154–163, ESA

Publications Division, Noordwijk.

ADS: http://adsabs.harvard.edu/abs/2004ESASP.575..154C

32


---


Cranmer, S.R., 2005, “Why is the Fast Solar Wind Fast and the Slow Solar Wind Slow? A Survey of

Geometrical Models”, in Connecting Sun and Heliosphere, (Eds.) Fleck, B., Zurbuchen, T.H., Lacoste,

H., Proceedings of Solar Wind 11/SOHO–16, 12–17 June 2005, Whistler, Canada, vol. SP-592 of ESA

Conference Proceedings, pp. 159–164, ESA Publications Division, Noordwijk.

ADS: http://adsabs.harvard.edu/abs/2005ESASP.592..159C Cranmer, S.R., 2007, “Turbulence in the solar corona”, in Turbulence and Nonlinear Processes in Astro-

physical Plasmas, (Eds.) Shaikh, D., Zank, G.P., Proceedings of the Sixth International Astrophysics

Conference, Oahu, Hawaii, 16–22 March 2007, vol. 932 of AIP Conference Proceedings, pp. 327–332,

American Institute of Physics, Melville.

ADS: http://adsabs.harvard.edu/abs/2007AIPC..932..327C Cranmer, S.R., 2008a, “Winds of Main-Sequence Stars: Observational Limits and a Path to Theoretical

Prediction”, in Proceedings of the 14th Cambridge Workshop on Cool Stars, Stellar Systems, and the

Sun, (Ed.) van Belle, G., 5–10 November 2006, Pasadena, California, vol. 384 of ASP Conf. Proc., pp.

317–326, Astronomical Society of the Pacific, San Francisco.

ADS: http://adsabs.harvard.edu/abs/2008ASPC..384..317C Cranmer, S.R., 2008b, “Turbulence-driven polar winds from T Tauri stars energized by magnetospheric

accretion”, Astrophys. J., 689, 316–334.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...689..316C Cranmer, S.R., van Ballegooijen, A.A., 2003, “Alfvénic turbulence in the extended solar corona: kinetic

effects and proton heating”, Astrophys. J., 594, 573–591.

ADS: http://adsabs.harvard.edu/abs/2003ApJ...594..573C Cranmer, S.R., van Ballegooijen, A.A., 2005, “On the generation, propagation, and reflection of Alfvén

waves from the solar photosphere to the distant heliosphere”, Astrophys. J. Suppl. Ser., 156, 265–293.

ADS: http://adsabs.harvard.edu/abs/2005ApJS..156..265C Cranmer, S.R., Field, G.B., Kohl, J.L., 1999a, “Spectroscopic constraints on models of ion cyclotron reso-

nance heating in the polar solar corona and high-speed solar wind”, Astrophys. J., 518, 937–947.

ADS: http://adsabs.harvard.edu/abs/1999ApJ...518..937C Cranmer, S.R., Kohl, J.L., Noci, G., Antonucci, E., Tondello, G., Huber, M.C.E., Strachan, L., Panasyuk,

A.V., Gardner, L.D., Romoli, M., Fineschi, S., Dobrzycka, D., Raymond, J.C., Nicolosi, P., Siegmund,

O.H.W., Spadaro, D., Benna, C., Ciaravella, A., Giordano, S., Habbal, S.R., Karovska, M., Li, X., Martin,

R., Michels, J.G., Modigliani, A., Naletto, G., O’Neal, R.H., Pernechele, C., Poletto, G., Smith, P.L.,

Suleiman, R.M., 1999b, “An Empirical Model of a Polar Coronal Hole at Solar Minimum”, Astrophys.

J., 511, 481–501.

ADS: http://adsabs.harvard.edu/abs/1999ApJ...511..481C Cranmer, S.R., van Ballegooijen, A.A., Edgar, R.J., 2007, “Self-consistent coronal heating and solar wind

acceleration from anisotropic magnetohydrodynamic turbulence”, Astrophys. J. Suppl. Ser., 171, 520–

551.

ADS: http://adsabs.harvard.edu/abs/2007ApJS..171..520C

Cranmer, S.R., Panasyuk, A.V., Kohl, J.L., 2008, “Improved Constraints on the Preferential Heating and

Acceleration of Oxygen Ions in the Extended Solar Corona”, Astrophys. J., 678, 1480–1497.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...678.1480C Cranmer, S.R., Matthaeus, W.H., Breech, B.A., Kasper, J.C., 2009, “Empirical Constraints on Proton and

Electron Heating in the Fast Solar Wind”, Astrophys. J., 702, 1604–1614.

ADS: http://adsabs.harvard.edu/abs/2009ApJ...702.1604C

33


---


Crooker, N.U., 2004, “What Is the International Heliophysical Year?”, Eos Trans. AGU, 85, 351–353.

ADS: http://adsabs.harvard.edu/abs/2004EOSTr..85R.351C

Culhane, L., Harra, L.K., Baker, D., van Driel-Gesztelyi, L., Sun, J., Doschek, G.A., Brooks, D.H.,

Lundquist, L.L., Kamio, S., Young, P.R., Hansteen, V.H., 2007, “Hinode EUV Study of Jets in the

Sun’s South Polar Corona”, Pub. Astron. Soc. Japan, 59, S751–S756.

ADS: http://adsabs.harvard.edu/abs/2007PASJ...59S.751C

Dasso, S., Milano, L.J., Matthaeus, W.H., Smith, C.W., 2005, “Anisotropy in Fast and Slow Solar Wind

Fluctuations”, Astrophys. J. Lett., 635, L181–L184.

ADS: http://adsabs.harvard.edu/abs/2005ApJ...635L.181D David, C., Gabriel, A.H., Bely-Dubau, F., Fludra, A., Lemaire, P., Wilhelm, K., 1998, “Measurement of the

electron temperature gradient in a solar coronal hole”, Astron. Astrophys., 336, L90–L94.

ADS: http://adsabs.harvard.edu/abs/1998A&A...336L..90D Davila, J.M., Gopalswamy, N., Thompson, B.J., 2009, “Universal processes in heliophysics”, in Universal

Heliophysical Processes, (Eds.) Gopalswamy, N., Webb, D.F., Proceedings of IAU Symp. 257, 15–19

September 2008, Ioannina, Greece, pp. 11–16, Cambridge University Press, Cambridge.

ADS: http://adsabs.harvard.edu/abs/2009IAUS..257...11D

De Pontieu, B., McIntosh, S.W., Carlsson, M., Hansteen, V.H., Tarbell, T.D., Schrijver, C.J., Title, A.M.,

Shine, R.A., Tsuneta, S., Katsukawa, Y., Ichimoto, K., Suematsu, Y., Shimizu, T., Nagata, S., 2007,

“Chromospheric Alfvénic waves strong enough to power the solar wind”, Science, 318, 1574–1577.

ADS: http://adsabs.harvard.edu/abs/2007Sci...318.1574D

de Toma, G., Arge, C.N., 2005, “Multi-wavelength Observations of Coronal Holes”, in Large-scale Struc-

tures and their Role in Solar Activity, (Eds.) Sankarasubramanian, K., Penn, M., Pevtsov, A., Proceedings

of the 22nd Sacramento Peak Workshop, 18–22 October 2004, Sunspot, New Mexico, vol. 346 of ASP

Conf. Proc., pp. 251–260, Astronomical Society of the Pacific, San Francisco.

ADS: http://adsabs.harvard.edu/abs/2005ASPC..346..251T DeForest, C.E., Gurman, J.B., 1998, “Observation of Quasi-periodic Compressive Waves in Solar Polar

Plumes”, Astrophys. J. Lett., 501, L217–L220.

ADS: http://adsabs.harvard.edu/abs/1998ApJ...501L.217D DeForest, C.E., Hoeksema, J.T., Gurman, J.B., Thompson, B.J., Plunkett, S.P., Howard, R., Harrison, R.C.,

Hassler, D.M., 1997, “Polar Plume Anatomy: Results of a Coordinated Observation”, Solar Phys., 175,

393–410.

ADS: http://adsabs.harvard.edu/abs/1997SoPh..175..393D

DeForest, C.E., Lamy, P.L., Llebaria, A., 2001, “Solar Polar Plume Lifetime and Coronal Hole Expansion:

Determination from Long-Term Observations”, Astrophys. J., 560, 490–498.

ADS: http://adsabs.harvard.edu/abs/2001ApJ...560..490D Del Zanna, G., Bromage, B.J.I., 1999, “The Elephant’s Trunk: Spectroscopic diagnostics applied to

SOHO/CDS observations of the August 1996 equatorial coronal hole”, J. Geophys. Res., 104, 9753–

9766.

ADS: http://adsabs.harvard.edu/abs/1999JGR...104.9753D

Del Zanna, L., von Steiger, R., Velli, M., 1998, “The Expansion of Coronal Plumes in the Fast Solar Wind”,

Space Sci. Rev., 85, 349–356.

ADS: http://adsabs.harvard.edu/abs/1998SSRv...85..349D

34


---


Dmitruk, P., Matthaeus, W.H., 2003, “Low-Frequency Waves and Turbulence in an Open Magnetic Region:

Timescales and Heating Efficiency”, Astrophys. J., 597, 1097–1105.

ADS: http://adsabs.harvard.edu/abs/2003ApJ...597.1097D Dmitruk, P., Milano, L.J., Matthaeus, W.H., 2001, “Wave-driven Turbulent Coronal Heating in Open Field

Line Regions: Nonlinear Phenomenological Model”, Astrophys. J., 548, 482–491.

ADS: http://adsabs.harvard.edu/abs/2001ApJ...548..482D Dmitruk, P., Matthaeus, W.H., Milano, L.J., Oughton, S., Zank, G.P., Mullan, D.J., 2002, “Coronal Heating

Distribution Due to Low-Frequency, Wave-driven Turbulence”, Astrophys. J., 575, 571–577.

ADS: http://adsabs.harvard.edu/abs/2002ApJ...575..571D Dmitruk, P., Matthaeus, W.H., Seenu, N., 2004, “Test Particle Energization by Current Sheets and Nonuni-

form Fields in Magnetohydrodynamic Turbulence”, Astrophys. J., 617, 667–679.

ADS: http://adsabs.harvard.edu/abs/2004ApJ...617..667D Dobrowolny, M., Mangeney, A., Veltri, P., 1980, “Fully developed anisotropic hydromagnetic turbulence in

interplanetary space”, Phys. Rev. Lett., 45, 144–147.

ADS: http://adsabs.harvard.edu/abs/1980PhRvL..45..144D Dobrzycka, D., Raymond, J.C., Cranmer, S.R., 2000, “Ultraviolet Spectroscopy of Polar Coronal Jets”,

Astrophys. J., 538, 922–931.

ADS: http://adsabs.harvard.edu/abs/2000ApJ...538..922D Dobrzycka, D., Raymond, J., DeLuca, E., Gurman, J., Fludra, A., Biesecker, D., 2006, “SOHO Observa-

tions of Polar Coronal Jets over the Last Solar Cycle”, in 10 Years of SOHO and Beyond, (Eds.) Lacoste,

H., Ouwehand, L., Proceedings of the SOHO-17 Conference, 7–12 May 2006, Giardini Naxos, Italy, vol.

SP-617 of ESA Conference Proceedings, pp. 87.1–87.4, ESA Publications Division, Noordwijk.

ADS: http://adsabs.harvard.edu/abs/2006ESASP.617E..87D Dolla, L., Solomon, J., 2008, “Solar off-limb line widths: Alfvén waves, ion-cyclotron waves, and prefer-

ential heating”, Astron. Astrophys., 483, 271–283.

ADS: http://adsabs.harvard.edu/abs/2008A&A...483..271D Doschek, G.A., Feldman, U., Laming, J.M., Schühle, U., Wilhelm, K., 2001, “Properties of Solar Polar

Coronal Hole Plasmas Observed above the Limb”, Astrophys. J., 546, 559–568.

ADS: http://adsabs.harvard.edu/abs/2001ApJ...546..559D Dowdy, J.F., Rabin, D., Moore, R.L., 1986, “On the magnetic structure of the quiet transition region”, Solar

Phys., 105, 35–45.

ADS: http://adsabs.harvard.edu/abs/1986SoPh..105...35D Doyle, J.G., Teriaca, L., Banerjee, D., 1999, “Coronal hole diagnostics out to 8 R⊙ ”, Astron. Astrophys.,

349, 956–960.

ADS: http://adsabs.harvard.edu/abs/1999A&A...349..956D Dunn, R.B., Zirker, J.B., 1973, “The Solar Filigree”, Solar Phys., 33, 281–304.

ADS: http://adsabs.harvard.edu/abs/1973SoPh...33..281D

Dupree, A.K., Penn, M.J., Jones, H.P., 1996, “He I 10830 Å Wing Asymmetry in Polar Coronal Holes:

Evidence for Radial Outflows”, Astrophys. J. Lett., 467, L121–L124.

ADS: http://adsabs.harvard.edu/abs/1996ApJ...467L.121D Dupree, A.K., Brickhouse, N.S., Smith, G.H., Strader, J., 2005, “A Hot Wind from the Classical T Tauri

Stars: TW Hydrae and T Tauri”, Astrophys. J. Lett., 625, L131–L134.

ADS: http://adsabs.harvard.edu/abs/2005ApJ...625L.131D

35


---


Eastwood, J.P., 2008, “The science of space weather”, Phil. Trans. Roy. Soc. A, 366, 4489–4500.

ADS: http://adsabs.harvard.edu/abs/2008RSPTA.366.4489E

Ergun, R.E., Carlson, C.W., Muschietti, L., Roth, I., McFadden, J.P., 1999, “Properties of fast solitary

structures”, Nonlinear Proc. Geophys., 6, 187–194.

ADS: http://adsabs.harvard.edu/abs/1999NPGeo...6..187E Esser, R., Edgar, R.J., 2000, “Reconciling Spectroscopic Electron Temperature Measurements in the Solar

Corona with In Situ Charge State Observations”, Astrophys. J., 532, L71–L74.

ADS: http://adsabs.harvard.edu/abs/2000ApJ...532L..71E Esser, R., Fineschi, S., Dobrzycka, D., Habbal, S.R., Edgar, R.J., Raymond, J.C., Kohl, J.L., Guhathakurta,

M., 1999, “Plasma Properties in Coronal Holes Derived from Measurements of Minor Ion Spectral Lines

and Polarized White Light Intensity”, Astrophys. J. Lett., 510, L63–L67.

ADS: http://adsabs.harvard.edu/abs/1999ApJ...510L..63E

Feigelson, E.D., Montmerle, T., 1999, “High-energy processes in young stellar objects”, Ann. Rev. Astron.

Astrophys., 37, 363–408.

ADS: http://adsabs.harvard.edu/abs/1999ARA&A..37..363F Feldman, U., 1998, “FIP Effect in the Solar Upper Atmosphere: Spectroscopic Results”, Space Sci. Rev.,

85, 227–240.

ADS: http://adsabs.harvard.edu/abs/1998SSRv...85..227F Feldman, U., Widing, K.G., 2003, “Elemental Abundances in the Solar Upper Atmosphere Derived by

Spectroscopic Means”, Space Sci. Rev., 107, 665–720.

ADS: http://adsabs.harvard.edu/abs/2003SSRv..107..665F Feldman, U., Widing, K.G., Warren, H.P., 1999, “Morphology of the quiet solar upper atmosphere in the

4 × 104 < Te < 1.4 × 106 K temperature regime”, Astrophys. J., 522, 1133–1147.

ADS: http://adsabs.harvard.edu/abs/1999ApJ...522.1133F Feldman, U., Landi, E., Schwadron, N.A., 2005, “On the sources of fast and slow solar wind”, J. Geophys.

Res., 110, A07 109.

ADS: http://adsabs.harvard.edu/abs/2005JGRA..11007109F Feldman, U., Landi, E., Doschek, G.A., 2007, “Diagnostics of Suprathermal Electrons in Active-Region

Plasmas Using He-like UV Lines”, Astrophys. J., 660, 1674–1682.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...660.1674F Feng, X., Zhou, Y., Wu, S.T., 2007, “A Novel Numerical Implementation for Solar Wind Modeling by the

Modified Conservation Element/Solution Element Method”, Astrophys. J., 655, 1110–1126.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...655.1110F Ferreira, J., Dougados, C., Cabrit, S., 2006, “Which jet launching mechanism(s) in T Tauri stars?”, Astron.

Astrophys., 453, 785–796.

ADS: http://adsabs.harvard.edu/abs/2008A&A...453..785F Feynman, J., Gabriel, S.B., 2000, “On space weather consequences and predictions”, J. Geophys. Res., 105,

10 543–10 564.

ADS: http://adsabs.harvard.edu/abs/2000JGR...10510543F Filippov, B., Golub, L., Koutchmy, S., 2009, “X-Ray Jet Dynamics in a Polar Coronal Hole Region”, Solar

Phys., 254, 259–269.

ADS: http://adsabs.harvard.edu/abs/2009SoPh..254..259F

36


---


Fisher, R., Guhathakurta, M., 1995, “Physical Properties of Polar Coronal Rays and Holes as Observed with

the Spartan 201-01 Coronagraph”, Astrophys. J. Lett., 447, L139–L142.

ADS: http://adsabs.harvard.edu/abs/1995ApJ...447L.139F Fisher, R., Sime, D.G., 1984, “Solar activity cycle variation of the K corona”, Astrophys. J., 285, 354–358.

ADS: http://adsabs.harvard.edu/abs/1984ApJ...285..354F

Fisk, L.A., 2003, “Acceleration of the solar wind as a result of the reconnection of open magnetic flux with

coronal loops”, J. Geophys. Res., 108, 1157.

ADS: http://adsabs.harvard.edu/abs/2003JGRA..108.1157F Fisk, L.A., 2005, “The open magnetic flux of the Sun: I: Transport by reconnections with coronal loops”,

Astrophys. J., 626, 563–573.

ADS: http://adsabs.harvard.edu/abs/2005ApJ...626..563F Fisk, L.A., Schwadron, N.A., 2001, “The Behavior of the Open Magnetic Field of the Sun”, Astrophys. J.,

560, 425–438.

ADS: http://adsabs.harvard.edu/abs/2001ApJ...560..425F Fisk, L.A., Zhao, L., 2009, “The heliospheric magnetic field and the solar wind during the solar cycle”,

in Universal Heliophysical Processes, (Eds.) Gopalswamy, N., Webb, D.F., Proceedings of IAU Symp.

257, 15–19 September 2008, Ioannina, Greece, pp. 109–120, Cambridge University Press, Cambridge.

ADS: http://adsabs.harvard.edu/abs/2009IAUS..257..109F

Fisk, L.A., Zurbuchen, T.H., 2006, “Distribution and properties of open magnetic flux outside of coronal

holes”, J. Geophys. Res., 111, A09 115.

ADS: http://adsabs.harvard.edu/abs/2006JGRA..11109115F Fisk, L.A., Schwadron, N.A., Zurbuchen, T.H., 1999, “Acceleration of the fast solar wind by the emergence

of new magnetic flux”, J. Geophys. Res., 104, 19 765–19 772.

ADS: http://adsabs.harvard.edu/abs/1999JGR...10419765F Frazin, R.A., Vásquez, A.M., Kamalabadi, F., Park, H., 2007, “Three-dimensional Tomographic Analysis

of a High-Cadence LASCO-C2 Polarized Brightness Sequence”, Astrophys. J. Lett., 671, L201–L204.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...671L.201F Gabriel, A.H., 1976, “A magnetic model of the solar transition region”, Phil. Trans. Roy. Soc. A, 281, 339–

352.

ADS: http://adsabs.harvard.edu/abs/1976RSPTA.281..339G Gabriel, A.H., Bely-Dubau, F., Lemaire, P., 2003, “The contribution of polar plumes to the fast solar wind”,

Astrophys. J., 589, 623–634.

ADS: http://adsabs.harvard.edu/abs/2003ApJ...589..623G Galinsky, V.L., Shevchenko, V.I., 2000, “Nonlinear Cyclotron Resonant Wave-Particle Interaction in a

Nonuniform Magnetic Field”, Phys. Rev. Lett., 85, 90–93.

ADS: http://adsabs.harvard.edu/abs/2000PhRvL..85...90G Gardner, L.D., Kohl, J.L., Daigneau, P.S., Smith, P.L., Strachan, L., Howard, R.A., Socker, D.G., Davila,

J.M., Noci, G., Romoli, M., Fineschi, S., 2003, “Advanced spectroscopic and coronographic explorer:

Science payload design concept”, Proc. SPIE, 4843, 1–7.

ADS: http://adsabs.harvard.edu/abs/2003SPIE.4843....1G

Gary, S.P., Borovsky, J.E., 2008, “Damping of long-wavelength kinetic Alfvén fluctuations: Linear theory”,

J. Geophys. Res., 113, A12 104.

ADS: http://adsabs.harvard.edu/abs/2008JGRA..11312104G

37


---


Gibson, S.E., Fludra, A., Bagenal, F., Biesecker, D., Del Zanna, G., Bromage, B., 1999, “Solar minimum

streamer densities and temperatures using Whole Sun Month coordinated data sets”, J. Geophys. Res.,

104, 9691–9700.

ADS: http://adsabs.harvard.edu/abs/1999JGR...104.9691G

Giordano, S., Antonucci, E., Noci, G., Romoli, M., Kohl, J.L., 2000, “Identification of the Coronal Sources

of the Fast Solar Wind”, Astrophys. J. Lett., 531, L79–L82.

ADS: http://adsabs.harvard.edu/abs/2000ApJ...531L..79G Gloeckler, G., Zurbuchen, T.H., Geiss, J., 2003, “Implications of the observed anticorrelation between solar

wind speed and coronal electron temperature”, J. Geophys. Res., 108, 1158.

ADS: http://adsabs.harvard.edu/abs/2003JGRA..108.1158G Gold, T., 1955, “The symmetry of the corona of 1954 June 30”, Mon. Not. Roy. Astron. Soc., 115, 340–342.

ADS: http://adsabs.harvard.edu/abs/1955MNRAS.115..340G

Goldreich, P., Sridhar, S., 1995, “Toward a Theory of Interstellar Turbulence: 2, Strong Alfvénic Turbu-

lence”, Astrophys. J., 438, 763–775.

ADS: http://adsabs.harvard.edu/abs/1995ApJ...438..763G Goldstein, B.E., Neugebauer, M., Phillips, J.L., Bame, S., Gosling, J.T., McComas, D., Wang, Y.-M., Shee-

ley Jr, N.R., Suess, S.T., 1996, “Ulysses plasma parameters: Latitudinal, radial, and temporal variations”,

Astron. Astrophys., 316, 296–303.

ADS: http://adsabs.harvard.edu/abs/1996A&A...316..296G

Goldstein, M.L., Roberts, D.A., Matthaeus, W.H., 1997, “Magnetohydrodynamic Turbulence in Cosmic

Winds”, in Cosmic Winds and the Heliosphere, (Eds.) Jokipii, J.R., Sonett, C.P., Giampapa, M.S., Space

Science Series, pp. 521–580, University of Arizona Press, Tucson Gómez, D.O., Dmitruk, P.A., Milano, L.J., 2000, “Recent theoretical results on coronal heating”, Solar

Phys., 195, 299–318.

ADS: http://adsabs.harvard.edu/abs/2000SoPh..195..299G Gosling, J.T., Szabo, A., 2008, “Bifurcated current sheets produced by magnetic reconnection in the solar

wind”, J. Geophys. Res., 113, A10 103.

ADS: http://adsabs.harvard.edu/abs/2008JGRA..11310103G Gosling, J.T., Skoug, R.M., McComas, D.J., Smith, C.W., 2005, “Magnetic disconnection from the Sun:

Observations of a reconnection exhaust in the solar wind at the heliospheric current sheet”, Geophys.

Res. Lett., 32, L05 105.

ADS: http://adsabs.harvard.edu/abs/2005GeoRL..3205105G

Güdel, M., 2007, “The Sun in Time: Activity and Environment”, Living Rev. Solar Phys., 4, lrsp-2007-3.

URL (cited on 1 July 2009):

http://www.livingreviews.org/lrsp-2007-3 Güdel, M., Audard, M., Briggs, K., Haberl, F., Magee, H., Maggio, A., Mewe, R., Pallavicini, R., Pye, J.,

2001, “The XMM-Newton view of stellar coronae: X-ray spectroscopy of the corona of AB Doradus”,

Astron. Astrophys., 365, L336–L343.

ADS: http://adsabs.harvard.edu/abs/2001A&A...365L.336G

Güdel, M., Arzner, K., Audard, M., Mewe, R., 2003, “Tomography of a stellar X-ray corona: alpha Coronae

Borealis”, Astron. Astrophys., 403, 155–171.

ADS: http://adsabs.harvard.edu/abs/2003A&A...403..155G

38


---


Gudiksen, B.V., 2005, “DC Heating: Is it Enough?”, in Connecting Sun and Heliosphere, (Eds.) Fleck,

B., Zurbuchen, T.H., Lacoste, H., Proceedings of Solar Wind 11/SOHO–16, 12–17 June 2005, Whistler,

Canada, vol. SP-592 of ESA Conference Proceedings, pp. 165–169, ESA Publications Division, Noord-

wijk.

ADS: http://adsabs.harvard.edu/abs/2005ESASP.592..165G Guhathakurta, M., Holzer, T.E., 1994, “Density structure inside a polar coronal hole”, Astrophys. J., 426,

782–786.

ADS: http://adsabs.harvard.edu/abs/1994ApJ...426..782G Guhathakurta, M., Sittler, E., Fisher, R., McComas, D., Thompson, B., 1999a, “Coronal magnetic field

topology and source of fast solar wind”, Geophys. Res. Lett., 26, 2901–2904.

ADS: http://adsabs.harvard.edu/abs/1999GeoRL..26.2901G Guhathakurta, M., Fludra, A., Gibson, S.E., Biesecker, D., Fisher, R., 1999b, “Physical properties of a

coronal hole from a coronal diagnostic spectrometer, Mauna Loa Coronagraph, and LASCO observations

during the Whole Sun Month”, J. Geophys. Res., 104, 9801–9808.

ADS: http://adsabs.harvard.edu/abs/1999JGR...104.9801G

Guo, Z., Crabtree, C., Chen, L., 2008, “Theory of charged particle heating by low-frequency Alfvén waves”,

Phys. Plasmas, 15, 032311.

ADS: http://adsabs.harvard.edu/abs/2008PhPl...15c2311G Habbal, S.R., Esser, R., Arndt, M.B., 1993, “How reliable are coronal hole temperatures deduced from

observations?”, Astrophys. J., 413, 435–444.

ADS: http://adsabs.harvard.edu/abs/1993ApJ...413..435H Habbal, S.R., Woo, R., Arnaud, J., 2001, “On the Predominance of the Radial Component of the Magnetic

Field in the Solar Corona”, Astrophys. J., 558, 852–858.

ADS: http://adsabs.harvard.edu/abs/2001ApJ...558..852H Habbal, S.R., Scholl, I.F., McIntosh, S.W., 2008, “Impact of Active Regions on Coronal Hole Outflows”,

Astrophys. J. Lett., 683, L75–L78.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...683L..75H Hagenaar, H.J., Schrijver, C.J., Title, A.M., Shine, R.A., 1999, “Dispersal of Magnetic Flux in the Quiet

Solar Photosphere”, Astrophys. J., 511, 932–944.

ADS: http://adsabs.harvard.edu/abs/1999ApJ...511..932H Hagenaar, H.J., DeRosa, M.L., Schrijver, C.J., 2008, “The Dependence of Ephemeral Region Emergence

on Local Flux Imbalance”, Astrophys. J., 678, 541–548.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...678..541H Hansteen, V.H., Leer, E., 1995, “Coronal heating, densities, and temperatures and solar wind acceleration”,

J. Geophys. Res., 100, 21,577–21,594.

ADS: http://adsabs.harvard.edu/abs/1995JGR...10021577H Hansteen, V.H., Leer, E., Holzer, T.E., 1997, “The Role of Helium in the Outer Solar Atmosphere”, Astro-

phys. J., 482, 498–509.

ADS: http://adsabs.harvard.edu/abs/1997ApJ...482..498H Harmon, J.K., Coles, W.A., 2005, “Modeling radio scattering and scintillation observations of the inner

solar wind using oblique Alfvén/ion cyclotron waves”, J. Geophys. Res., 110, A03 101.

ADS: http://adsabs.harvard.edu/abs/2005JGRA..11003101H

39


---


Harra, L.K., Hara, H., Imada, S., Young, P.R., Williams, D.R., Sterling, A.C., Korendyke, C., Attrill,

G.D.R., 2007, “Coronal Dimming Observed with Hinode: Outflows Related to a Coronal Mass Ejection”,

Pub. Astron. Soc. Japan, 59, S801–S806.

ADS: http://adsabs.harvard.edu/abs/2007PASJ...59S.801H

Hartigan, P., Edwards, S., Ghandour, L., 1995, “Disk Accretion and Mass Loss from Young Stars”, Astro-

phys. J., 452, 736–768.

ADS: http://adsabs.harvard.edu/abs/1995ApJ...452..736H Hartmann, L., 2000, Accretion Processes in Star Formation, Cambridge University Press, Cambridge Harvey, J., Krieger, A.S., Timothy, A.F., Vaiana, G.S., 1975, “Comparison of Skylab X-ray and Ground-

based Helium Observations”, Osserv. Mem. Oss. Astrofis. Arcetri, 104, 50–58.

ADS: http://adsabs.harvard.edu/abs/1975MmArc.104...50H Harvey, J.W., 1965, “Coronal Polar Rays and Polar Magnetic Fields”, Astrophys. J., 141, 832–833.

ADS: http://adsabs.harvard.edu/abs/1965ApJ...141..832H

Harvey, J.W., Sheeley Jr, N.R., 1979, “Coronal holes and solar magnetic fields”, Space Sci. Rev., 23, 139–

158.

ADS: http://adsabs.harvard.edu/abs/1979SSRv...23..139H Harvey, K.L., Recely, F., 2002, “Polar Coronal Holes During Cycles 22 and 23”, Solar Phys., 211, 31–52.

ADS: http://adsabs.harvard.edu/abs/2002SoPh..211...31H

Hassler, D.M., Dammasch, I.E., Lemaire, P., Brekke, P., Curdt, W., Mason, H.E., Vial, J.-C., Wilhelm, K.,

1999, “Solar Wind Outflow and the Chromospheric Magnetic Network”, Science, 283, 810–813.

ADS: http://adsabs.harvard.edu/abs/1999Sci...283..810H He, J.-S., Tu, C.-Y., Marsch, E., 2007, “Can the solar wind originate from a quiet Sun region?”, Astron.

Astrophys., 468, 307–312.

ADS: http://adsabs.harvard.edu/abs/2007A&A...468..307H Hefti, S., Grünwaldt, H., Ipavich, F.M., Bochsler, P., Hovestadt, D., Aellig, M.R., Hilchenbach, M., Kallen-

bach, R., Galvin, A.B., Geiss, J., Gliem, F., Gloeckler, G., Klecker, B., Marsch, E., Möbius, E., Neuge-

bauer, M., Wurz, P., 1998, “Kinetic properties of solar wind minor ions and protons measured with

SOHO/CELIAS”, J. Geophys. Res., 103, 29,697–29,704.

ADS: http://adsabs.harvard.edu/abs/1998JGR...10329697H Hick, P., Jackson, B.V., Rappoport, S., Woan, G., Slater, G., Strong, K., Uchida, Y., 1995, “Synoptic IPS

and Yohkoh soft X-ray observations”, Geophys. Res. Lett., 22, 643–646.

ADS: http://adsabs.harvard.edu/abs/1995GeoRL..22..643H Hoeksema, J.T., Scherrer, P.H., 1986, “An atlas of photospheric magnetic field observations and computed

coronal magnetic fields: 1976–1985”, Solar Phys., 105, 205–211.

ADS: http://adsabs.harvard.edu/abs/1986SoPh..105..205H Hollweg, J.V., 1986, “Transition region, corona, and solar wind in coronal holes”, J. Geophys. Res., 91,

4111–4125.

ADS: http://adsabs.harvard.edu/abs/1986JGR....91.4111H Hollweg, J.V., 1990, “Heating of the solar corona”, Comput. Phys. Rep., 12, 205–232.

ADS: http://adsabs.harvard.edu/abs/1990CoPhR..12..205H

40


---


Hollweg, J.V., 2000, “Compressibility of ion cyclotron and whistler waves: Can radio measurements detect

high-frequency waves of solar origin in the corona?”, J. Geophys. Res., 105, 7573–7582.

ADS: http://adsabs.harvard.edu/abs/2000JGR...105.7573H Hollweg, J.V., 2006, “Drivers of the solar wind: Then and now”, Phil. Trans. Roy. Soc. A, 364, 505–527.

ADS: http://adsabs.harvard.edu/abs/2006RSPTA.364..505H

Hollweg, J.V., Isenberg, P.A., 2002, “Generation of the fast solar wind: A review with emphasis on the

resonant cyclotron interaction”, J. Geophys. Res., 107, 1147.

ADS: http://adsabs.harvard.edu/abs/2002JGRA.107gSSH12H Hollweg, J.V., Johnson, W., 1988, “Transition region, corona, and solar wind in coronal holes: Some two-

fluid models”, J. Geophys. Res., 93, 9547–9554.

ADS: http://adsabs.harvard.edu/abs/1988JGR....93.9547H Hollweg, J.V., Markovskii, S.A., 2002, “Cyclotron resonances of ions with obliquely propagating waves in

coronal holes and the fast solar wind”, J. Geophys. Res., 107, 1080.

ADS: http://adsabs.harvard.edu/abs/2002JGRA.107f.SSH1H Hossain, M., Gray, P.C., Pontius, D.H., Matthaeus, W.H., Oughton, S., 1995, “Phenomenology for the

decay of energy-containing eddies in homogeneous MHD turbulence”, Phys. Fluids, 7, 2886–2904.

ADS: http://adsabs.harvard.edu/abs/1995PhFl....7.2886H Huber, M.C.E., Foukal, P.V., Noyes, R.W., Reeves, E.M., Schmahl, E.J., Timothy, J.G., Vernazza, J.E.,

Withbroe, G. L., 1974, “Extreme-ultraviolet observations of coronal holes: Initial results from Skylab”,

Astrophys. J. Lett., 194, L115–L118.

ADS: http://adsabs.harvard.edu/abs/1974ApJ...194L.115H

Hudson, H.S., 2002, “Coronal holes as seen in soft X-rays by Yohkoh”, in From Solar Min to Max: Half

a Solar Cycle with SOHO, (Ed.) Wilson, A., Proceedings of the SOHO-11 Symposium, 11–15 March

2002, Davos, Switzerland, vol. SP-508 of ESA Conference Proceedings, pp. 341–349, ESA Publications

Division, Noordwijk.

ADS: http://adsabs.harvard.edu/abs/2002ESASP.508..341H Hundhausen, A.J., 1972, Coronal Expansion and the Solar Wind, vol. 5 of Physics and Chemistry in Space,

Springer, Berlin; New York

Isenberg, P.A., 1990, “Investigations of a turbulence-driven solar wind model”, J. Geophys. Res., 95, 6437–

6442.

ADS: http://adsabs.harvard.edu/abs/1990JGR....95.6437I Isenberg, P.A., 2001, “Heating of coronal holes and generation of the solar wind by ion-cyclotron reso-

nance”, Space Sci. Rev., 95, 119–131.

ADS: http://adsabs.harvard.edu/abs/2001SSRv...95..119I Isenberg, P.A., Vasquez, B.J., 2009, “Preferential acceleration and perpendicular heating of minor ions in a

collisionless coronal hole”, Astrophys. J., 696, 591–600.

ADS: http://adsabs.harvard.edu/abs/2009ApJ...696..591I Isenberg, P.A., Lee, M.A., Hollweg, J.V., 2001, “The kinetic shell model of coronal heating and acceleration

by ion-cyclotron waves: 1. Outward propagating waves”, J. Geophys. Res., 106, 5649–5660.

ADS: http://adsabs.harvard.edu/abs/2001JGR...106.5649I Janardhan, P., Tripathi, D., Mason, H.E., 2008, “The solar wind disappearance event of 11 May 1999:

Source region evolution”, Astron. Astrophys., 488, L1–L4.

ADS: http://adsabs.harvard.edu/abs/2001A&A...488L...1J

41


---


Janse, Å.M., Lie-Svendsen, Ø., Leer, E., 2007, “Solar wind originating in funnels: fast or slow?”, Astron.

Astrophys., 474, 997–1013.

ADS: http://adsabs.harvard.edu/abs/2007A&A...474..997J Jardine, M., van Ballegooijen, A.A., 2005, “Slingshot prominences above stellar X-ray coronae”, Mon. Not.

Roy. Astron. Soc., 361, 1173–1179.

ADS: http://adsabs.harvard.edu/abs/2005MNRAS.361.1173J Jiang, Y.W., Liu, S., Petrosian, V., 2009, “Cascade and Damping of Alfvén-Cyclotron Fluctuations: Appli-

cation to Solar Wind Turbulence”, Astrophys. J., 698, 163–183.

ADS: http://adsabs.harvard.edu/abs/2009ApJ...698..163J Jones, H.P., 2005, “Magnetic Fields and Flows in Open Magnetic Structures”, in Large-scale Structures and

their Role in Solar Activity, (Eds.) Sankarasubramanian, K., Penn, M., Pevtsov, A., Proceedings of the

22nd Sacramento Peak Workshop, 18-22 October 2004, Sunspot, New Mexico, vol. 346 of ASP Conf.

Proc., pp. 229–244, Astronomical Society of the Pacific, San Francisco.

ADS: http://adsabs.harvard.edu/abs/2005ASPC..346..229J Kahler, S., 2000, “Skylab”, in Encyclopedia of Astronomy and Astrophysics, (Ed.) Murdin, P., p. 2238,

Institute of Physics Publishing, Bristol.

ADS: http://adsabs.harvard.edu/abs/2000eaa..bookE2238K

Khazanov, I., Singh, N., 2007, “Ion and electron accelerations by large-scale shear Alfvén waves via cross-

field instabilities”, Geophys. Res. Lett., 34, L20 111.

ADS: http://adsabs.harvard.edu/abs/2007GeoRL..3420111K Klimchuk, J.A., 2006, “On Solving the Coronal Heating Problem”, Solar Phys., 234, 41–77.

ADS: http://adsabs.harvard.edu/abs/2006SoPh..234...41K

Ko, Y.-K., Fisk, L.A., Gloeckler, G., Geiss, J., 1996, “Limitations on suprathermal tails of electrons in the

lower solar corona”, Geophys. Res. Lett., 23, 2785–2788.

ADS: http://adsabs.harvard.edu/abs/1996GeoRL..23.2785K Ko, Y.-K., Fisk, L.A., Geiss, J., Gloeckler, G., Guhathakurta, M., 1997, “An Empirical Study of the Electron

Temperature and Heavy Ion Velocities in the South Polar Coronal Hole”, Solar Phys., 171, 345–361.

ADS: http://adsabs.harvard.edu/abs/1997SoPh..171..345K Kohl, J.L., Cranmer, S.R. (Eds.), 1999, Coronal Holes and Solar Wind Acceleration, Kluwer Academic

Publishers, Dordrecht; Boston; London

Kohl, J.L., Withbroe, G.L., 1982, “EUV spectroscopic plasma diagnostics for the solar wind acceleration

region”, Astrophys. J., 256, 263–270.

ADS: http://adsabs.harvard.edu/abs/1982ApJ...256..263K Kohl, J.L., Reeves, E.M., Kirkham, B., 1978, “The Lyman Alpha Coronagraph”, in New Instrumentation

for Space Astronomy, (Eds.) van der Hucht, K.A., Viana, G., Proceedings of the 20th COSPAR Meeting,

Tel Aviv, Israel, 7–18 June 1977, pp. 91–94, Pergamon Press, Oxford.

ADS: http://adsabs.harvard.edu/abs/1978nisa.conf...91K

Kohl, J.L., Weiser, H., Withbroe, G.L., Noyes, R.W., Parkinson, W.H., Reeves, E.M., Munro, R.H., Mac-

Queen, R.M., 1980, “Measurements of coronal kinetic temperatures from 1.5 to 3 solar radii”, Astrophys.

J. Lett., 241, L117–L121.

ADS: http://adsabs.harvard.edu/abs/1980ApJ...241L.117K

42


---


Kohl, J.L., Esser, R., Gardner, L.D., Habbal, S., Daigneau, P.S., Dennis, E.F., Nystrom, G.U., Panasyuk,

A., Raymond, J.C., Smith, P.L., Strachan, L., van Ballegooijen, A.A., Noci, G., Fineschi, S., Romoli,

M., Ciaravella, A., Modigliani, A., Huber, M.C.E., Antonucci, E., Benna, C., Giordano, S., Tondello, G.,

Nicolosi, P., Naletto, G., Pernechele, C., Spadaro, D., Poletto, G., Livi, S., von der Lühe, O., Geiss, J.,

Timothy, J.G., Gloeckler, G., Allegra, A., Basile, G., Brusa, R., Wood, B., Siegmund, O.H.W., Fowler,

W., Fisher, R., Jhabvala, M., 1995, “The Ultraviolet Coronagraph Spectrometer for the Solar and Helio-

spheric Observatory”, Solar Phys., 162, 313–356.

ADS: http://adsabs.harvard.edu/abs/1995SoPh..162..313K

Kohl, J.L., Noci, G., Antonucci, E., Tondello, G., Huber, M.C.E., Gardner, L.D., Nicolosi, P., Strachan,

L., Fineschi, S., Raymond, J.C., Romoli, M., Spadaro, D., Panasyuk, A., Siegmund, O.H.W., Benna,

C., Ciaravella, A., Cranmer, S.R., Giordano, S., Karovska, M., Martin, R., Michels, J., Modigliani, A.,

Naletto, G., Pernechele, C., Poletto, G., Smith, P.L., 1997, “First Results from the SOHO Ultraviolet

Coronagraph Spectrometer”, Solar Phys., 175, 613–644.

ADS: http://adsabs.harvard.edu/abs/1997SoPh..175..613K

Kohl, J.L., Noci, G., Antonucci, E., Tondello, G., Huber, M.C.E., Cranmer, S.R., Strachan, L., Panasyuk,

A.V., Gardner, L.D., Romoli, M., Fineschi, S., Dobrzycka, D., Raymond, J.C., Nicolosi, P., Siegmund,

O.H.W., Spadaro, D., Benna, C., Ciaravella, A., Giordano, S., Habbal, S.R., Karovska, M., Li, X., Martin,

R., Michels, J.G., Modigliani, A., Naletto, G., O’Neal, R.H., Pernechele, C., Poletto, G., Smith, P.L.,

Suleiman, R.M., 1998, “UVCS/SOHO empirical determinations of anisotropic velocity distributions in

the solar corona”, Astrophys. J. Lett., 501, L127–L131.

ADS: http://adsabs.harvard.edu/abs/1998ApJ...501L.127K Kohl, J.L., Esser, R., Cranmer, S.R., Fineschi, S., Gardner, L.D., Panasyuk, A.V., Strachan, L., Suleiman,

R.M., Frazin, R.A., Noci, G., 1999, “EUV Spectral Line Profiles in Polar Coronal Holes from 1.3 to 3.0

R⊙ ”, Astrophys. J. Lett., 510, L59–L62.

ADS: http://adsabs.harvard.edu/abs/1999ApJ...510L..59K

Kohl, J.L., Noci, G., Cranmer, S.R., Raymond, J.C., 2006, “Ultraviolet spectroscopy of the extended solar

corona”, Astron. Astrophys. Review, 13, 31–157.

ADS: http://adsabs.harvard.edu/abs/2006A&ARv..13...31K Kojima, M., Tokumaru, M., Fujiki, K., Itoh, H., Murakami, T., Hakamada, K., 2007, “What Coronal Pa-

rameters Determine Solar Wind Speed?”, in New Solar Physics with Solar-B Mission, (Eds.) Shibata, K.,

Nagata, S., Sakurai, T., Proceedings of the 6th Solar-B Science Meeting, 8–11 November 2005, Kyoto,

Japan, vol. 369 of ASP Conf. Proc., pp. 549–555, Astronomical Society of the Pacific, San Francisco.

ADS: http://adsabs.harvard.edu/abs/2007ASPC..369..549K Krieger, A.S., Timothy, A.F., Roelof, E.C., 1973, “A Coronal Hole and Its Identification as the Source of a

High Velocity Solar Wind Stream”, Solar Phys., 29, 505–525.

ADS: http://adsabs.harvard.edu/abs/1973SoPh...29..505K Krista, L.D., Gallagher, P.T., 2009, “Automated Coronal Hole Detection Using Local Intensity Thresholding

Techniques”, Solar Phys., 256, 87–100.

ADS: http://adsabs.harvard.edu/abs/2009SoPh..256...87K Kwan, J., Edwards, S., Fischer, W., 2007, “Modeling T Tauri Winds from He I 10830 Å Profiles”, Astrophys.

J., 657, 897–915.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...657..897K Lada, C.J., 1985, “Cold outflows, energetic winds, and enigmatic jets around young stellar objects”, Ann.

Rev. Astron. Astrophys., 23, 267–317.

ADS: http://adsabs.harvard.edu/abs/1985ARA&A..23..267L

43


---


Lamers, H.J.G.L.M., Cassinelli, J.P., 1999, Introduction to Stellar Winds, Cambridge University Press,

Cambridge

Laming, J.M., 2004, “A Unified Picture of the First Ionization Potential and Inverse First Ionization Poten-

tial Effects”, Astrophys. J., 614, 1063–1072.

ADS: http://adsabs.harvard.edu/abs/2004ApJ...614.1063L Laming, J.M., 2009, “Non-WKB Models of the FIP Effect: Implications for Solar Coronal Heating and the

Coronal Helium and Neon Abundances”, Astrophys. J., 695, 954–969.

ADS: http://adsabs.harvard.edu/abs/2009ApJ...695..954L Laming, J.M., Lepri, S.T., 2007, “Ion Charge States in the Fast Solar Wind: New Data Analysis and Theo-

retical Refinements”, Astrophys. J., 660, 1642–1652.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...660.1642L Landi, E., 2008, “The off-disk thermal structure of a polar coronal hole”, Astrophys. J., 685, 1270–1276.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...685.1270L

Landi, E., Cranmer, S.R., 2009, “Ion temperatures in the low solar corona: Polar coronal holes at solar

minimum”, Astrophys. J., 691, 794–805.

ADS: http://adsabs.harvard.edu/abs/2009ApJ...691..794L Leamon, R.J., McIntosh, S.W., 2007, “Empirical Solar Wind Forecasting from the Chromosphere”, Astro-

phys. J., 659, 738–742.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...659..738L Leamon, R.J., Smith, C.W., Ness, N.F., Wong, H.K., 1999, “Dissipation range dynamics: Kinetic Alfvén

waves and the importance of βe ”, J. Geophys. Res., 104, 22 331–22 344.

ADS: http://adsabs.harvard.edu/abs/1999JGR...10422331L Lee, L.C., Wu, B.H., 2000, “Heating and Acceleration of Protons and Minor Ions by Fast Shocks in the

Solar Corona”, Astrophys. J., 535, 1014–1026.

ADS: http://adsabs.harvard.edu/abs/2000ApJ...535.1014L Leer, E., Holzer, T.E., 1980, “Energy addition in the solar wind”, J. Geophys. Res., 85, 4681–4688.

ADS: http://adsabs.harvard.edu/abs/1980JGR....85.4681L

Leer, E., Holzer, T.E., Fla, T., 1982, “Acceleration of the solar wind”, Space Sci. Rev., 33, 161–200.

ADS: http://adsabs.harvard.edu/abs/1982SSRv...33..161L

Lemaire, J., Pierrard, V., 2001, “Kinetic models of solar and polar winds”, Astrophys. Space Sci., 277, 169–

180.

ADS: http://adsabs.harvard.edu/abs/2001Ap&SS.277..169L Levine, R.H., 1974, “A new theory of coronal heating”, Astrophys. J., 190, 457–466.

ADS: http://adsabs.harvard.edu/abs/1974ApJ...190..457L

Levine, R.H., 1982, “Open magnetic fields and the solar cycle, I, Photospheric sources of open magnetic

flux”, Solar Phys., 79, 203–230.

ADS: http://adsabs.harvard.edu/abs/1982SoPh...79..203L Li, X., Habbal, S.R., 2001, “Damping of fast and ion cyclotron oblique waves in the multi-ion fast solar

wind”, J. Geophys. Res., 106, 10 669–10 680.

ADS: http://adsabs.harvard.edu/abs/2001JGR...10610669L

44


---


Li, X., Habbal, S.R., Kohl, J., Noci, G., 1998, “The Effect of Temperature Anisotropy on Observations of

Doppler Dimming and Pumping in the Inner Corona”, Astrophys. J. Lett., 501, L133–L137.

ADS: http://adsabs.harvard.edu/abs/1998ApJ...501L.133L Li, X., Habbal, S.R., Hollweg, J.V., Esser, R., 1999, “Heating and cooling of protons by turbulence-driven

ion-cyclotron waves in the fast solar wind”, J. Geophys. Res., 104, 2521–2535.

ADS: http://adsabs.harvard.edu/abs/1999JGR...104.2521L Liewer, P.C., Neugebauer, M., Zurbuchen, T., 2004, “Characteristics of active-region sources of solar wind

near solar maximum”, Solar Phys., 223, 209–229.

ADS: http://adsabs.harvard.edu/abs/2004SoPh..223..209L Lippincott, S.L., 1957, “Chromospheric Spicules”, Smithsonian Contrib. Astrophys., 2, 15–23.

ADS: http://adsabs.harvard.edu/abs/1957SCoA....2...15L

Longcope, D., 2004, “Quantifying Magnetic Reconnection and the Heat it Generates”, in Coronal Heating,

(Eds.) Walsh, R.W., Ireland, J., Danesy, D., Fleck, B., Proceedings of the SOHO–15 Workshop, 6–9

September 2004, St. Andrews, Scotland, UK, vol. SP-575 of ESA Conference Proceedings, pp. 198–

209, ESA Publications Division, Noordwijk.

ADS: http://adsabs.harvard.edu/abs/2004ESASP.575..198L Longcope, D.W., 1996, “Topology and Current Ribbons: A Model for Current, Reconnection, and Flaring

in a Complex, Evolving Corona”, Solar Phys., 169, 91–121.

ADS: http://adsabs.harvard.edu/abs/1996SoPh..169...91L Longcope, D.W., Kankelborg, C.C., 1999, “Coronal Heating by Collision and Cancellation of Magnetic

Elements”, Astrophys. J., 524, 483–495.

ADS: http://adsabs.harvard.edu/abs/1999ApJ...524..483L Lu, Q., Li, X., 2007, “Heating of ions by low-frequency Alfvén waves”, Phys. Plasmas, 14, 042303.

ADS: http://adsabs.harvard.edu/abs/2007PhPl...14d2303L

Luhmann, J.G., Li, Y., Arge, C.N., Gazis, P.R., Ulrich, R., 2002, “Solar cycle changes in coronal holes and

space weather cycles”, J. Geophys. Res., 107, 1154.

ADS: http://adsabs.harvard.edu/abs/2002JGRA..107.1154L Luo, Q., Melrose, D., 2006, “Anisotropic weak turbulence of Alfvén waves in collisionless astrophysical

plasmas”, Mon. Not. Roy. Astron. Soc., 368, 1151–1158.

ADS: http://adsabs.harvard.edu/abs/2006MNRAS.368.1151L MacBride, B.T., Smith, C.W., Forman, M.A., 2008, “The Turbulent Cascade at 1 AU: Energy Transfer and

the Third-Order Scaling for MHD”, Astrophys. J., 679, 1644–1660.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...679.1644M Malanushenko, O.V., Jones, H.P., 2004, “Analysis of He I 1083 nm Imaging Spectroscopy Using a Spectral

Standard”, Solar Phys., 222, 43–60.

ADS: http://adsabs.harvard.edu/abs/2004SoPh..222...43M Mancuso, S., Raymond, J.C., Kohl, J., Ko, Y.-K., Uzzo, M., Wu, R., 2002, “UVCS/SOHO observations

of a CME-driven shock: Consequences on ion heating mechanisms behind a coronal shock”, Astron.

Astrophys., 383, 267–274.

ADS: http://adsabs.harvard.edu/abs/2002A&A...383..267M

Markovskii, S.A., 2001, “Generation of ion-cyclotron waves in coronal holes by a global resonant magne-

tohydrodynamic mode”, Astrophys. J., 557, 337–342.

ADS: http://adsabs.harvard.edu/abs/2001ApJ...557..337M

45


---


Markovskii, S.A., Hollweg, J.V., 2002, “Electron heat flux instabilities in coronal holes: Implications for

ion heating”, Geophys. Res. Lett., 29, 1843.

ADS: http://adsabs.harvard.edu/abs/2002GeoRL..29q..24M Markovskii, S.A., Hollweg, J.V., 2004, “Intermittent Heating of the Solar Corona by Heat Flux-generated

Ion Cyclotron Waves”, Astrophys. J., 609, 1112–1122.

ADS: http://adsabs.harvard.edu/abs/2004ApJ...609.1112M Markovskii, S.A., Vasquez, B.J., Smith, C.W., Hollweg, J.V., 2006, “Dissipation of the Perpendicular Tur-

bulent Cascade in the Solar Wind”, Astrophys. J., 639, 1177–1185.

ADS: http://adsabs.harvard.edu/abs/2006ApJ...639.1177M Markovskii, S.A., Vasquez, B.J., Hollweg, J.V., 2009, “Proton heating by nonlinear field-aligned Alfvén

waves in solar coronal holes”, Astrophys. J., 695, 1413–1420.

ADS: http://adsabs.harvard.edu/abs/2009ApJ...695.1413M Marsch, E., 1999, “Solar wind models from the sun to 1 AU: Constraints by in situ and remote sensing

measurements”, Space Sci. Rev., 87, 1–24.

ADS: http://adsabs.harvard.edu/abs/1999SSRv...87....1M Marsch, E., 2005, “Importance of Kinetic Effects in Heating the Open and Closed Corona”, in Connect-

ing Sun and Heliosphere, (Eds.) Fleck, B., Zurbuchen, T.H., Lacoste, H., Proceedings of Solar Wind

11/SOHO–16, 12–17 June 2005, Whistler, Canada, vol. SP-592 of ESA Conference Proceedings, pp.

191–198, ESA Publications Division, Noordwijk.

ADS: http://adsabs.harvard.edu/abs/2005ESASP.592..191M Marsch, E., 2006, “Kinetic Physics of the Solar Corona and Solar Wind”, Living Rev. Solar Phys., 3, lrsp-

2006-1. URL (cited on 1 July 2009):

http://www.livingreviews.org/lrsp-2006-1 Marsch, E., Mühlhäuser, K.-H., Schwenn, R., Rosenbauer, H., Pilipp, W.G., Neubauer, F.M., 1982, “Solar

wind protons: Three-dimensional velocity distributions and derived plasma parameters measured be-

tween 0.3 and 1 AU”, J. Geophys. Res., 87, 52–72.

ADS: http://adsabs.harvard.edu/abs/1982JGR....87...52M

Marsch, E., Tian, H., Sun, J., Curdt, W., Wiegelmann, T., 2008, “Plasma flows guided by strong magnetic

fields in the solar corona”, Astrophys. J., 685, 1262–1269.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...685.1262M Marsden, R.G., Fleck, B., 2007, “Solar Orbiter: A Mission Update”, in The Physics of Chromospheric Plas-

mas, (Eds.) Heinzel, P., Dorotovič, I., Proceedings of the conference held 9–13 October 2006, Coimbra,

Portugal, vol. 368 of ASP Conf. Proc., p. 645, Astronomical Society of the Pacific, San Francisco.

ADS: http://adsabs.harvard.edu/abs/2007ASPC..368..645M

Matthaeus, W.H., Zank, G.P., Oughton, S., Mullan, D.J., Dmitruk, P., 1999, “Coronal Heating by Mag-

netohydrodynamic Turbulence Driven by Reflected Low-Frequency Waves”, Astrophys. J. Lett., 523,

L93–L96.

ADS: http://adsabs.harvard.edu/abs/1999ApJ...523L..93M

Matthaeus, W.H., Dmitruk, P., Oughton, S., Mullan, D., 2003, “Turbulent dissipation in the solar wind and

corona”, in Solar Wind Ten, (Eds.) Velli, M., Bruno, R., Malara, F., Proceedings of the Tenth International

Solar Wind Conference, Pisa, Italy, 17–21 June 2002, vol. 679 of AIP Conference Proceedings, pp. 427–

432, American Institute of Physics, Melville.

ADS: http://adsabs.harvard.edu/abs/2003AIPC..679..427M

46


---


McComas, D.J., Bame, S.J., Barker, P., Feldman, W.C., Phillips, J.L., Riley, P., Griffee, J.W., 1998, “Solar

Wind Electron Proton Alpha Monitor (SWEPAM) for the Advanced Composition Explorer”, Space Sci.

Rev., 86, 563–612.

ADS: http://adsabs.harvard.edu/abs/1998SSRv...86..563M

McComas, D.J., Elliott, H.A., Gosling, J.T., Reisenfeld, D.B., Skoug, R.M., Goldstein, B.E., Neugebauer,

M., Balogh, A., 2002, “Ulysses’ second fast-latitude scan: Complexity near solar maximum and the

reformation of polar coronal holes”, Geophys. Res. Lett., 29, 1290.

ADS: http://adsabs.harvard.edu/abs/2002GeoRL..29i...4M

McComas, D.J., Velli, M., Lewis, W.S., Acton, L.W., Balat-Pichelin, M., Bothmer, V., Dirling, R.B., Feld-

man, W.C., Gloeckler, G., Habbal, S.R., Hassler, D.M., Mann, I., Matthaeus, W.H., McNutt, R.L.,

Mewaldt, R.A., Murphy, N., Ofman, L., Sittler, E.C., Smith, C.W., Zurbuchen, T.H., 2007, “Under-

standing coronal heating and solar wind acceleration: Case for in situ near-Sun measurements”, Rev.

Geophys., 45, RG1004.

ADS: http://adsabs.harvard.edu/abs/2007RvGeo..45.1004M

McIntosh, S.W., 2009, “The Inconvenient Truth About Coronal Dimmings”, Astrophys. J., 693, 1306–1309.

ADS: http://adsabs.harvard.edu/abs/2009ApJ...693.1306M

McIntosh, S.W., Davey, A.R., Hassler, D.M., Armstrong, J.D., Curdt, W., Wilhelm, K., Lin, G., 2007,

“Observations Supporting the Role of Magnetoconvection in Energy Supply to the Quiescent Solar At-

mosphere”, Astrophys. J., 654, 650–664.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...654..650M

Mecheri, R., Marsch, E., 2008, “Drift instabilities in the solar corona within the multi-fluid description”,

Astron. Astrophys., 481, 853–860.

ADS: http://adsabs.harvard.edu/abs/2008A&A...481..853M Medvedev, M.V., 2000, “Particle Heating by Nonlinear Alfvénic Turbulence in Advection-dominated Ac-

cretion Flows”, Astrophys. J., 541, 811–820.

ADS: http://adsabs.harvard.edu/abs/2000ApJ...541..811M Mikhailenko, V.S., Mikhailenko, V.V., Stepanov, K.N., 2008, “Ion cyclotron instabilities of parallel shear

flow of collisional plasma”, Phys. Plasmas, 15, 092901.

ADS: http://adsabs.harvard.edu/abs/2008PhPl...15i2901M Miller, J.A., 1908, “The Determination of the Heliocentric Position of a Certain Class of Coronal Stream-

ers”, Astrophys. J., 27, 286–295.

ADS: http://adsabs.harvard.edu/abs/1908ApJ....27..286M Miralles, M.P., Cranmer, S.R., Panasyuk, A.V., Romoli, M., Kohl, J.L., 2001a, “Comparison of empirical

models for polar and equatorial coronal holes”, Astrophys. J. Lett., 549, L257–L260.

ADS: http://adsabs.harvard.edu/abs/2001ApJ...549L.257M Miralles, M.P., Cranmer, S.R., Kohl, J.L., 2001b, “Ultraviolet Coronagraph Spectrometer Observations

of a High-Latitude Coronal Hole with High Oxygen Temperatures and the Next Solar Cycle Polarity”,

Astrophys. J. Lett., 560, L193–L196.

ADS: http://adsabs.harvard.edu/abs/2001ApJ...560L.193M

Miralles, M.P., Cranmer, S.R., Kohl, J.L., 2004, “Low-latitude coronal holes during solar maximum”, Adv.

Space Res., 33, 696–700.

ADS: http://adsabs.harvard.edu/abs/2004AdSpR..33..696M

47


---


Miralles, M.P., Cranmer, S.R., Kohl, J.L., 2006, “Coronal Hole Properties During the First Decade of

UVCS/SOHO”, in 10 Years of SOHO and Beyond, (Eds.) Lacoste, H., Ouwehand, L., Proceedings of the

SOHO-17 Conference, 7–12 May 2006, Giardini Naxos, Italy, vol. SP-617 of ESA Conference Proceed-

ings, pp. 15.1–15.4, ESA Publications Division, Noordwijk.

ADS: http://adsabs.harvard.edu/abs/2006ESASP.617E..15M Miralles, M.P., Cranmer, S.R., Raymond, J.C., Kohl, J.L., 2007, “Multi-Instrument Searches for Polar Jets:

Characterizing Jet Heating and Cooling”, conference paper.

ADS: http://adsabs.harvard.edu/abs/2007IUGG...24..691M Mitchell, S.A., 1932, “The Spectrum of the Corona”, Astrophys. J., 75, 1–33.

ADS: http://adsabs.harvard.edu/abs/1932ApJ....75....1M

Moreno-Insertis, F., Galsgaard, K., Ugarte-Urra, I., 2008, “Jets in Coronal Holes: Hinode Observations and

Three-dimensional Computer Modeling”, Astrophys. J. Lett., 673, L211–L214.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...673L.211M Morgan, H., Habbal, S.R., Rifai, S., Li, X., 2004, “Hydrogen Lyα Intensity Oscillations Observed by the

Solar and Heliospheric Observatory Ultraviolet Coronagraph Spectrometer”, Astrophys. J., 605, 521–

527.

ADS: http://adsabs.harvard.edu/abs/2004ApJ...605..521M

Mullan, D.J., Yakovlev, O.I., 1995, “Remote Sensing of the Solar Wind Using Radio Waves: Part 1”, Irish

Astron. J., 22, 119–136.

ADS: http://adsabs.harvard.edu/abs/1995IrAJ...22..119M Munro, R.H., Jackson, B.V., 1977, “Physical properties of a polar coronal hole from 2 to 5 solar radii”,

Astrophys. J., 213, 874–886.

ADS: http://adsabs.harvard.edu/abs/1977ApJ...213..874M Munro, R.H., Withbroe, G.L., 1972, “Properties of a Coronal ‘hole’ Derived from Extreme-Ultraviolet

Observations”, Astrophys. J., 176, 511–520.

ADS: http://adsabs.harvard.edu/abs/1972ApJ...176..511M Neugebauer, M., Forsyth, R.J., Galvin, A.B., Harvey, K.L., Hoeksema, J.T., Lazarus, A.J., Lepping, R.P.,

Linker, J.A., Mikic, Z., Steinberg, J.T., von Steiger, R., Wang, Y.-M., Wimmer-Schweingruber, R.F.,

1998, “Spatial structure of the solar wind and comparisons with solar data and models”, J. Geophys.

Res., 103, 14 587–14 600.

ADS: http://adsabs.harvard.edu/abs/1998JGR...10314587N Neupert, W.M., Pizzo, V., 1974, “Solar coronal holes as sources of recurrent geomagnetic disturbances”, J.

Geophys. Res., 79, 3701–3709.

ADS: http://adsabs.harvard.edu/abs/1974JGR....79.3701N Newkirk, G., 1967, “Structure of the Solar Corona”, Ann. Rev. Astron. Astrophys., 5, 213–266.

ADS: http://adsabs.harvard.edu/abs/1967ARA&A...5..213N

Newkirk, G., Harvey, J., 1968, “Coronal Polar Plumes”, Solar Phys., 3, 321–343.

ADS: http://adsabs.harvard.edu/abs/1968SoPh....3..321N

Ng, C.S., Bhattacharjee, A., 2008, “A Constrained Tectonics Model for Coronal Heating”, Astrophys. J.,

675, 899–905.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...675..899N

48


---


Noci, G., 1973, “Energy Budget in Coronal Holes”, Solar Phys., 28, 403–407.

ADS: http://adsabs.harvard.edu/abs/1973SoPh...28..403N

Noci, G., Kohl, J.L., Withbroe, G.L., 1987, “Solar wind diagnostics from Doppler-enhanced scattering”,

Astrophys. J., 315, 706–715.

ADS: http://adsabs.harvard.edu/abs/1987ApJ...315..706N Noci, G., Kohl, J.L., Antonucci, E., Tondello, G., Huber, M.C.E., Fineschi, S., Gardner, L.D., Naletto,

G., Nicolosi, P., Raymond, J.C., Romoli, M., Spadaro, D., Siegmund, O.H.W., Benna, C., Ciaravella,

A., Giordano, S., Michels, J., Modigliani, A., Panasyuk, A., Pernechele, C., Poletto, G., Smith, P.L.,

Strachan, L., 1997, “First results from UVCS/SOHO”, Adv. Space Res., 20, 2219–2230.

ADS: http://adsabs.harvard.edu/abs/1997AdSpR..20.2219N Nolte, J.T., Krieger, A.S., Timothy, A.F., Gold, R.E., Roelof, E.C., Vaiana, G., Lazarus, A.J., Sullivan, J.D.,

McIntosh, P.S., 1976, “Coronal holes as sources of solar wind”, Solar Phys., 46, 303–322.

ADS: http://adsabs.harvard.edu/abs/1976SoPh...46..303N Ofman, L., 2005, “MHD Waves and Heating in Coronal Holes”, Space Sci. Rev., 120, 67–94.

ADS: http://adsabs.harvard.edu/abs/2005SSRv..120...67O

Ofman, L., Nakariakov, V.M., DeForest, C.E., 1999, “Slow Magnetosonic Waves in Coronal Plumes”,

Astrophys. J., 514, 441–447.

ADS: http://adsabs.harvard.edu/abs/1999ApJ...514..441O Ofman, L., Romoli, M., Poletto, G., Noci, G., Kohl, J.L., 2000, “UVCS WLC Observations of Compres-

sional Waves in the South Polar Coronal Hole”, Astrophys. J., 529, 592–598.

ADS: http://adsabs.harvard.edu/abs/2000ApJ...529..592O Oughton, S., Dmitruk, P., Matthaeus, W.H., 2004, “Reduced magnetohydrodynamics and parallel spectral

transfer”, Phys. Plasmas, 11, 2214–2225.

ADS: http://adsabs.harvard.edu/abs/2004PhPl...11.2214O Oughton, S., Dmitruk, P., Matthaeus, W.H., 2006, “A two-component phenomenology for homogeneous

magnetohydrodynamic turbulence”, Phys. Rev. Lett., 13, 042306.

ADS: http://adsabs.harvard.edu/abs/2006PhPl...13d2306O Pagel, A.C., Crooker, N.U., Zurbuchen, T.H., Gosling, J.T., 2004, “Correlation of solar wind entropy and

oxygen ion charge state ratio”, J. Geophys. Res., 109, A01 113.

ADS: http://adsabs.harvard.edu/abs/2004JGRA..10901113P Parashar, T.N., Shay, M.A., Cassak, P.A., Matthaeus, W.H., 2009, “Kinetic dissipation and anisotropic

heating in a turbulent collisionless plasma”, Phys. Plasmas, 16, 032310.

ADS: http://adsabs.harvard.edu/abs/2009PhPl...16c2310P Parhi, S., Suess, S.T., Sulkanen, M., 1999, “Can Kelvin-Helmholtz instabilities of jet-like structures and

plumes cause solar wind fluctuations at 1 AU?”, J. Geophys. Res., 104, 14 781–14 788.

ADS: http://adsabs.harvard.edu/abs/1999JGR...10414781P Pariat, E., Antiochos, S.K., DeVore, C.R., 2009, “A model for solar polar jets”, Astrophys. J., 691, 61–74.

ADS: http://adsabs.harvard.edu/abs/2009ApJ...691...61P

Parker, E.N., 1958a, “Dynamics of the interplanetary gas and magnetic fields”, Astrophys. J., 128, 664–676.

ADS: http://adsabs.harvard.edu/abs/1958ApJ...128..664P

Parker, E.N., 1958b, “Suprathermal particle generation in the solar corona”, Astrophys. J., 128, 677–685.

ADS: http://adsabs.harvard.edu/abs/1958ApJ...128..677P

49


---


Parker, E.N., 1991, “Heating solar coronal holes”, Astrophys. J., 372, 719–727.

ADS: http://adsabs.harvard.edu/abs/1991ApJ...372..719P

Parnell, C.E., 2007, “3D magnetic reconnection, flares and coronal heating”, Mem. Soc. Astron. Italiana,

78, 229–235.

ADS: http://adsabs.harvard.edu/abs/2007MmSAI..78..229P Pasachoff, J.M., Rušin, V., Druckmüller, M., Saniga, M., 2007, “Fine Structures in the White-Light Solar

Corona at the 2006 Eclipse”, Astrophys. J., 665, 824–829.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...665..824P Peter, H., Judge, P.G., 1999, “On the Doppler Shifts of Solar Ultraviolet Emission Lines”, Astrophys. J.,

522, 1148–1166.

ADS: http://adsabs.harvard.edu/abs/1999ApJ...522.1148P Pevtsov, A.A., Fisher, G.H., Acton, L.W., Longcope, D.W., Johns-Krull, C.M., Kankelborg, C.C., Metcalf,

T.R., 2003, “The Relationship Between X-Ray Radiance and Magnetic Flux”, Astrophys. J., 598, 1387–

1391.

ADS: http://adsabs.harvard.edu/abs/2003ApJ...598.1387P

Piddington, J.H., 1972, “A model of the quiet solar atmosphere”, Solar Phys., 27, 402–419.

ADS: http://adsabs.harvard.edu/abs/1972SoPh...27..402P

Pierrard, V., Lamy, H., 2003, “The effects of the velocity filtration mechanism on the minor ions of the

corona”, Solar Phys., 216, 47–58.

ADS: http://adsabs.harvard.edu/abs/2003SoPh..216...47P Pierrard, V., Lamy, H., Lemaire, J., 2004, “Exospheric distributions of minor ions in the solar wind”, J.

Geophys. Res., 109, A02 118.

ADS: http://adsabs.harvard.edu/abs/2004JGRA..10902118P

Pinto, R., Grappin, R., Wang, Y.-M., Léorat, J., 2009, “Time-dependent hydrodynamical simulations of

slow solar wind, coronal inflows, and polar plumes”, Astron. Astrophys., 497, 537–543.

ADS: http://adsabs.harvard.edu/abs/2009A&A...497..537P Pneuman, G.W., 1968, “Some General Properties of Helmeted Coronal Structures”, Solar Phys., 3, 578–

597.

ADS: http://adsabs.harvard.edu/abs/1968SoPh....3..578P Pneuman, G.W., 1973, “The Solar Wind and the Temperature-Density Structure of the Solar Corona”, Solar

Phys., 28, 247–262.

ADS: http://adsabs.harvard.edu/abs/1973SoPh...28..247P Pneuman, G.W., 1980, “The physical structure of coronal holes: Influence of magnetic fields and coronal

heating”, Astron. Astrophys., 81, 161–166.

ADS: http://adsabs.harvard.edu/abs/1980A&A....81..161P Podesta, J.J., Bhattacharjee, A., 2009, “Theory of incompressible MHD turbulence with cross-helicity”,

Phys. Rev. Lett., submitted

Poduval, B., Zhao, X.P., 2004, “Discrepancies in the prediction of solar wind using potential field source

surface model: An investigation of possible sources”, J. Geophys. Res., 109, A08 102.

ADS: http://adsabs.harvard.edu/abs/2004JGRA..10908102P

50


---


Poletto, G., Suess, S.T., Biesecker, D.A., Esser, R., Gloeckler, G., Ko, Y.-K., Zurbuchen, T.H., 2002, “Low-

latitude solar wind during the Fall 1998 SOHO-Ulysses quadrature”, J. Geophys. Res., 107, 1300.

ADS: http://adsabs.harvard.edu/abs/2002JGRA..107.1300P Priest, E.R., Forbes, T.G., 2000, Magnetic Reconnection: MHD Theory and Applications, Cambridge Uni-

versity Press, New York

Priest, E.R., Heyvaerts, J.F., Title, A.M., 2002, “A Flux-Tube Tectonics Model for Solar Coronal Heating

Driven by the Magnetic Carpet”, Astrophys. J., 576, 533–551.

ADS: http://adsabs.harvard.edu/abs/2002ApJ...576..533P Ralchenko, Y., Feldman, U., Doschek, G.A., 2007, “Is There a High-Energy Particle Population in the Quiet

Solar Corona?”, Astrophys. J., 659, 1682–1692.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...659.1682R Raouafi, N.-E., Solanki, S.K., 2004, “Effect of the electron density stratification on off-limb O VI line

profiles: How large is the velocity distribution anisotropy in the solar corona?”, Astron. Astrophys., 427,

725–733.

ADS: http://adsabs.harvard.edu/abs/2004A&A...427..725R

Raouafi, N.-E., Solanki, S.K., 2006, “Sensitivity of solar off-limb line profiles to electron density stratifica-

tion and the velocity distribution anisotropy”, Astron. Astrophys., 445, 735–745.

ADS: http://adsabs.harvard.edu/abs/2006A&A...445..735R Raouafi, N.-E., Harvey, J.W., Solanki, S.K., 2007, “Properties of Solar Polar Coronal Plumes Constrained

by Ultraviolet Coronagraph Spectrometer Data”, Astrophys. J., 658, 643–656.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...658..643R Raouafi, N.-E., Petrie, G.J.D., Norton, A.A., Henney, C.J., Solanki, S.K., 2008, “Evidence for Polar Jets as

Precursors of Polar Plume Formation”, Astrophys. J. Lett., 682, L137–L140.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...682L.137R Rappazzo, A.F., Velli, M., Einaudi, G., Dahlburg, R. B., 2008, “Nonlinear Dynamics of the Parker Scenario

for Coronal Heating”, Astrophys. J., 677, 1348–1366.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...677.1348R Reisenfeld, D.B., McComas, D.J., Steinberg, J.T., 1999, “Evidence of a solar origin for pressure balance

structures in the high-latitude solar wind”, Geophys. Res. Lett., 26, 1805–1808.

ADS: http://adsabs.harvard.edu/abs/1999GeoRL..26.1805R Reisenfeld, D.B., Gary, S.P., Gosling, J.T., Steinberg, J.T., McComas, D.J., Goldstein, B.E., Neugebauer,

M., 2001, “Helium energetics in the high-latitude solar wind: Ulysses observations”, J. Geophys. Res.,

106, 5693–5708.

ADS: http://adsabs.harvard.edu/abs/2001JGR...106.5693R

Riley, P., Linker, J.A., Mikić, Z., 2001, “An empirically-driven global MHD model of the solar corona and

inner heliosphere”, J. Geophys. Res., 106, 15 889–15 902.

ADS: http://adsabs.harvard.edu/abs/2001JGR...10615889R Roberts, B., 2000, “Waves and Oscillations in the Corona”, Solar Phys., 193, 139–152.

ADS: http://adsabs.harvard.edu/abs/2000SoPh..193..139R

Romoli, M., Frazin, R.A., Kohl, J.L., Gardner, L.D., Cranmer, S.R., Reardon, K., Fineschi, S., 2002, “In-

flight Calibration of the UVCS White Light Channel”, in The Radiometric Calibration of SOHO, (Eds.)

Pauluhn, A., Huber, M.C.E., von Steiger, R., vol. SR-002 of ISSI Scientific Report, pp. 181–201, ESA

Publications Division, Noordwijk

51


---


Rosner, R., Tucker, W.H., Vaiana, G.S., 1978, “Dynamics of the quiescent solar corona”, Astrophys. J., 220,

643–665.

ADS: http://adsabs.harvard.edu/abs/1978ApJ...220..643R Roussev, I.I., Gombosi, T.I., Sokolov, I.V., Velli, M., Manchester, W., DeZeeuw, D.L., Liewer, P., Tóth, G.,

Luhmann, J., 2003, “A Three-dimensional Model of the Solar Wind Incorporating Solar Magnetogram

Observations”, Astrophys. J. Lett., 595, L57–L61.

ADS: http://adsabs.harvard.edu/abs/2003ApJ...595L..57R

Rowlands, J., Shapiro, V.D., Shevchenko, V.I., 1966, “Quasilinear theory of plasma cyclotron instability”,

Sov. Phys. JETP, 23, 651–660

Rust, D.M., 1983, “Coronal disturbances and their terrestrial effects”, Space Sci. Rev., 34, 21–36.

ADS: http://adsabs.harvard.edu/abs/1983SSRv...34...21R

Ryutova, M., Habbal, S., Woo, R., Tarbell, T., 2001, “Photospheric Network as the Energy Source for the

quiet-Sun corona”, Solar Phys., 200, 213–234.

ADS: http://adsabs.harvard.edu/abs/2001SoPh..200..213R Saito, K., 1958, “Polar Rays of the Solar Corona”, Pub. Astron. Soc. Japan, 10, 49–78.

ADS: http://adsabs.harvard.edu/abs/1958PASJ...10...49S

Sakao, T., Kano, R., Narukage, N., Kotoku, J., Bando, T., DeLuca, E.E., Lundquist, L.L., Tsuneta, S.,

Harra, L.K., Katsukawa, Y., Kubo, M., Hara, H., Matsuzaki, K., Shimojo, M., Bookbinder, J.A., Golub,

L., Korreck, K.E., Su, Y., Shibasaki, K., Shimizu, T., Nakatani, I., 2007, “Continuous Plasma Outflows

from the Edge of a Solar Active Region as a Possible Source of Solar Wind”, Science, 318, 1585–1588.

ADS: http://adsabs.harvard.edu/abs/2007Sci...318.1585S Sanz-Forcada, J., Dupree, A.K., 2008, “Active cool stars and He I 10830 Å: The coronal connection”,

Astron. Astrophys., 488, 715–721.

ADS: http://adsabs.harvard.edu/abs/2008A&A...488..715S Schatten, K.H., Wilcox, J.M., Ness, N.F., 1969, “A model of interplanetary and coronal magnetic fields”,

Solar Phys., 6, 442–455.

ADS: http://adsabs.harvard.edu/abs/1969SoPh....6..442S Scholl, I.F., Habbal, S.R., 2008, “Automatic Detection and Classification of Coronal Holes and Filaments

Based on EUV and Magnetogram Observations of the Solar Disk”, Solar Phys., 248, 425–439.

ADS: http://adsabs.harvard.edu/abs/2008SoPh..248..425S Schrijver, C.J., Title, A.M., 2003, “The Magnetic Connection between the Solar Photosphere and the

Corona”, Astrophys. J. Lett., 597, L165–L168.

ADS: http://adsabs.harvard.edu/abs/2003ApJ...597L.165S Schrijver, C.J., Title, A.M., van Ballegooijen, A.A., Hagenaar, H.J., Shine, R.A., 1997, “Sustaining the

Quiet Photospheric Network: The Balance of Flux Emergence, Fragmentation, Merging, and Cancella-

tion”, Astrophys. J., 487, 424–436.

ADS: http://adsabs.harvard.edu/abs/1997ApJ...487..424S

Schwadron, N.A., McComas, D.J., 2003, “Solar wind scaling law”, Astrophys. J., 599, 1395–1403.

ADS: http://adsabs.harvard.edu/abs/2003ApJ...599.1395S

Schwadron, N.A., McComas, D.J., 2008, “The Solar Wind Power from Magnetic Flux”, Astrophys. J. Lett.,

686, L33–L36.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...686L..33S

52


---


Schwadron, N.A., McComas, D.J., DeForest, C., 2006, “Relationship between Solar Wind and Coronal

Heating: Scaling Laws from Solar X-Rays”, Astrophys. J., 642, 1173–1176.

ADS: http://adsabs.harvard.edu/abs/2006ApJ...642.1173S Schwartz, S.J., Feldman, W.C., Gary, S.P., 1981, “The source of proton anisotropy in the high-speed solar

wind”, J. Geophys. Res., 86, 541–546.

ADS: http://adsabs.harvard.edu/abs/1981JGR....86..541S Schwenn, R., 2006, “Solar Wind Sources and Their Variations Over the Solar Cycle”, Space Sci. Rev., 124,

51–76.

ADS: http://adsabs.harvard.edu/abs/2006SSRv..124...51S Scudder, J.D., 1992a, “Why all stars should posses circumstellar temperature inversions”, Astrophys. J.,

398, 319–349.

ADS: http://adsabs.harvard.edu/abs/1992ApJ...398..319S Scudder, J.D., 1992b, “On the causes of temperature change in inhomogenous low-density astrophysical

plasmas”, Astrophys. J., 398, 299–318.

ADS: http://adsabs.harvard.edu/abs/1992ApJ...398..299S Scudder, J.D., 1994, “Ion and electron suprathermal tail strengths in the transition region: Support for the

velocity filtration model of the corona”, Astrophys. J., 427, 446–452.

ADS: http://adsabs.harvard.edu/abs/1994ApJ...427..446S Seely, J.F., Feldman, U., Schühle, U., Wilhelm, K., Curdt, W., Lemaire, P., 1997, “Turbulent Velocities and

Ion Temperatures in the Solar Corona Obtained from SUMER Line Widths”, Astrophys. J. Lett., 484,

L87–L90.

ADS: http://adsabs.harvard.edu/abs/1997ApJ...484L..87S

Serviss, G.P., 1909, Curiosities of the Sky: A Popular Presentation of the Great Riddles and Mysteries of

Astronomy, Harper & Brothers, New York

Shebalin, J.V., Matthaeus, W.H., Montgomery, D., 1983, “Anisotropy in MHD turbulence due to a mean

magnetic field”, J. Plasma Phys., 29, 525–547.

ADS: http://adsabs.harvard.edu/abs/1983JPlPh..29..525S Sheeley Jr, N.R., Wang, Y.-M., Hawley, S H., Brueckner, G.E., Dere, K.P., Howard, R.A., Koomen, M.J.,

Korendyke, C.M., Michels, D.J., Paswaters, S.E., Socker, D.G., St. Cyr, O.C., Wang, D., Lamy, P.L.,

Llebaria, A., Schwenn, R., Simnett, G.M., Plunkett, S., Biesecker, D.A., 1997, “Measurements of Flow

Speeds in the Corona between 2 and 30 R⊙ ”, Astrophys. J., 484, 472–478.

ADS: http://adsabs.harvard.edu/abs/1997ApJ...484..472S Shibata, K., Nitta, N., Strong, K.T., Matsumoto, R., Yokoyama, T., Hirayama, T., Hudson, H., Ogawara, Y.,

1994, “A gigantic coronal jet ejected from a compact active region in a coronal hole”, Astrophys. J. Lett.,

431, L51–L53.

ADS: http://adsabs.harvard.edu/abs/1994ApJ...431L..51S

Shimojo, M., Narukage, N., Kano, R., Sakao, T., Tsuneta, S., Shibasaki, K., Cirtain, J.W., Lundquist, L.L.,

Reeves, K., Savcheva, A., 2007, “Fine Structures of Solar X-Ray Jets Observed with the X-Ray Telescope

aboard Hinode”, Pub. Astron. Soc. Japan, 59, S745–S750.

ADS: http://adsabs.harvard.edu/abs/2007PASJ...59S.745S

Singh, N., Khazanov, G., 2004, “Numerical simulation of waves driven by plasma currents generated by

low-frequency Alfvén waves in a multi-ion plasma”, J. Geophys. Res., 109, A05 210.

ADS: http://adsabs.harvard.edu/abs/2004JGRA..10905210S

53


---


Singh, N., Khazanov, G., Mukhter, A., 2007, “Electrostatic wave generation and transverse ion acceleration

by Alfvénic wave components of broadband extremely low frequency turbulence”, J. Geophys. Res., 112,

A06 210.

ADS: http://adsabs.harvard.edu/abs/2007JGRA..11206210S

Sittler, E.C., Guhathakurta, M., 1999, “Semiempirical Two-dimensional MagnetoHydrodynamic Model of

the Solar Corona and Interplanetary Medium”, Astrophys. J., 523, 812–826.

ADS: http://adsabs.harvard.edu/abs/1999ApJ...523..812S Smith, C.W., Hamilton, K., Vasquez, B.J., Leamon, R.J., 2006, “Dependence of the Dissipation Range

Spectrum of Interplanetary Magnetic Fluctuationson the Rate of Energy Cascade”, Astrophys. J. Lett.,

645, L85–L88.

ADS: http://adsabs.harvard.edu/abs/2006ApJ...645L..85S

Spangler, S.R., 2002, “The Amplitude of Magnetohydrodynamic Turbulence in the Inner Solar Wind”,

Astrophys. J., 576, 997–1004.

ADS: http://adsabs.harvard.edu/abs/2002ApJ...576..997S Spruit, H.C., 1981, “Motion of magnetic flux tubes in the solar convection zone and chromosphere”, Astron.

Astrophys., 98, 155–160.

ADS: http://adsabs.harvard.edu/abs/1981A&A....98..155S

Spruit, H.C., 1984, “Interaction of Fluxtubes With Convection”, in Small-Scale Dynamical Processes in

Quiet Stellar Atmospheres, (Ed.) Keil, S.L., 25–29 July 1983, Sunspot, New Mexico, p. 249, National

Solar Observatory, Sunspot, NM.

ADS: http://adsabs.harvard.edu/abs/1984ssdp.conf..249S

Stoddard, L.G., Carson, D.G., Saito, K., 1966, “Polar Rays of the Solar Corona Observed at the 1963

Eclipse”, Astrophys. J., 145, 796–799.

ADS: http://adsabs.harvard.edu/abs/1966ApJ...145..796S Strachan, L., Kohl, J.L., Weiser, H., Withbroe, G.L., Munro, R.H., 1993, “A Doppler dimming determina-

tion of coronal outflow velocity”, Astrophys. J., 412, 410–420.

ADS: http://adsabs.harvard.edu/abs/1993ApJ...412..410S Strachan, L., Suleiman, R., Panasyuk, A.V., Biesecker, D.A., Kohl, J.L., 2002, “Empirical densities, kinetic

temperatures, and outflow velocities in the equatorial streamer belt at solar minimum”, Astrophys. J.,

571, 1008–1014.

ADS: http://adsabs.harvard.edu/abs/2002ApJ...571.1008S

Strauss, H.R., 1976, “Nonlinear, three-dimensional magnetohydrodynamics of noncircular tokamaks”,

Phys. Fluids, 19, 134–140.

ADS: http://adsabs.harvard.edu/abs/1976PhFl...19..134S Sturrock, P.A., Roald, C.B., Wolfson, R., 1999, “Chromospheric Magnetic Reconnection and its Implication

for Coronal Heating”, Astrophys. J. Lett., 524, L75–L78.

ADS: http://adsabs.harvard.edu/abs/1999ApJ...524L..75S Suess, S. T., 1979, “Models of coronal hole flows”, Space Sci. Rev., 23, 159–200.

ADS: http://adsabs.harvard.edu/abs/1979SSRv...23..159S

Susino, R., Ventura, R., Spadaro, D., Vourlidas, A., Landi, E., 2008, “Physical parameters along the bound-

aries of a mid-latitude streamer and in its adjacent regions”, Astron. Astrophys., 488, 303–310.

ADS: http://adsabs.harvard.edu/abs/2008A&A...488..303S

54


---


Suzuki, T.K., 2006, “Forecasting Solar Wind Speeds”, Astrophys. J. Lett., 640, L75–L78.

ADS: http://adsabs.harvard.edu/abs/2006ApJ...640L..75S

Suzuki, T.K., Inutsuka, S.-I., 2006, “Solar winds driven by nonlinear low-frequency Alfvén waves from the

photosphere: Parametric study for fast/slow winds and disappearance of solar winds”, J. Geophys. Res.,

111, A06 101.

ADS: http://adsabs.harvard.edu/abs/2006JGRA..11106101S

Suzuki, T.K., Lazarian, A., Beresnyak, A., 2007, “Cascading of Fast-Mode Balanced and Imbalanced Tur-

bulence”, Astrophys. J., 662, 1033–1042.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...662.1033S Tanskanen, E.I., Slavin, J.A., Tanskanen, A.J, Viljanen, A., Pulkkinen, T.I., Koskinen, H.E.J., Pulkkinen,

A., Eastwood, J., 2005, “Magnetospheric substorms are strongly modulated by interplanetary high-speed

streams”, Geophys. Res. Lett., 32, L16 104.

ADS: http://adsabs.harvard.edu/abs/2005GeoRL..3216104T

Tappin, S.J., Simnett, G.M., Lyons, M.A., 1999, “A determination of the outflow speeds in the lower solar

wind”, Astron. Astrophys., 350, 302–309.

ADS: http://adsabs.harvard.edu/abs/1999A&A...350..302T Telloni, D., Antonucci, E., Bruno, R., D’Amicis, R., 2009, “Persistent and Self-Similar Large-Scale Density

Fluctuations in the Solar Corona”, Astrophys. J., 693, 1022–1028.

ADS: http://adsabs.harvard.edu/abs/2009ApJ...693.1022T Teplitskaya, R.B., Turova, I.P., Ozhogina, O.A., 2007, “The Lower Chromosphere in a Coronal Hole”,

Solar Phys., 243, 143–161.

ADS: http://adsabs.harvard.edu/abs/2007SoPh..243..143T Teriaca, L., Poletto, G., Romoli, M., Biesecker, D.A., 2003, “The nascent solar wind: Origin and accelera-

tion”, Astrophys. J., 588, 566–577.

ADS: http://adsabs.harvard.edu/abs/2003ApJ...588..566T Thieme, K.M., Marsch, E., Schwenn, R., 1990, “Spatial structures in high-speed streams as signatures of

fine structures in coronal holes”, Ann. Geophys., 8, 713–723.

ADS: http://adsabs.harvard.edu/abs/1990AnGeo...8..713T Thompson, B.J., Cliver, E.W., Nitta, N., Delannée, C., Delaboudinière, J.-P., 2000, “Coronal dimmings and

energetic CMEs in April-May 1998”, Geophys. Res. Lett., 27, 1431–1434.

ADS: http://adsabs.harvard.edu/abs/2000GeoRL..27.1431T Timothy, A.F., Krieger, A.S., Vaiana, G.S., 1975, “The structure and evolution of coronal holes”, Solar

Phys., 42, 135–156.

ADS: http://adsabs.harvard.edu/abs/1975SoPh...42..135T Title, A.M., Schrijver, C.J., 1998, “The Sun’s Magnetic Carpet”, in Proceedings of the 10th Cambridge

Workshop on Cool Stars, Stellar Systems, and the Sun, (Eds.) Donahue, R.A., Bookbinder, J.A., 15–19

July 1997, Cambridge, Massachusetts, vol. 154 of ASP Conf. Proc., pp. 345–358, Astronomical Society

of the Pacific, San Francisco.

ADS: http://adsabs.harvard.edu/abs/1998ASPC..154..345T Tomczyk, S., McIntosh, S.W., 2009, “Time-Distance Seismology of the Solar Corona with CoMP”, Astro-

phys. J., 697, 1384–1391.

ADS: http://adsabs.harvard.edu/abs/2009ApJ...697.1384T

55


---


Tomczyk, S., McIntosh, S.W., Keil, S.L., Judge, P.G., Schad, T., Seeley, D.H., Edmondson, J., 2007,

“Alfvén waves in the solar corona”, Science, 317, 1192–1196.

ADS: http://adsabs.harvard.edu/abs/2007Sci...317.1192T Tóth, G., Sokolov, I.V., Gombosi, T.I., Chesney, D.R., Clauer, C.R., De Zeeuw, D.L., Hansen, K.C., Kane,

K.J., Manchester, W.B., Oehmke, R.C., Powell, K.G., Ridley, A.J., Roussev, I.I., Stout, Q.F., Volberg, O.,

Wolf, R.A., Sazykin, S., Chan, A., Yu, B., Kóta, J., 2005, “Space Weather Modeling Framework: A new

tool for the space science community”, J. Geophys. Res., 110, A12 226.

ADS: http://adsabs.harvard.edu/abs/2005JGRA..11012226T Tousey, R., Sandlin, G.D., Purcell, J.D., 1968, “On Some Aspects of XUV Spectroheliograms”, in Structure

and Development of Solar Active Regions, (Ed.) Kiepenheuer, K.O., Proceedings of IAU Symp. 35, 4–8

September 1967, Budapest, Hungary, pp. 411–419, D. Reidel, Dordrecht.

ADS: http://adsabs.harvard.edu/abs/1968IAUS...35..411T

Tsuneta, S., Ichimoto, K., Katsukawa, Y., Lites, B.W., Matsuzaki, K., Nagata, S., Orozco Suárez, D.,

Shimizu, T., Shimojo, M., Shine, R.A., Suematsu, Y., Suzuki, T.K., Tarbell, T.D., Title, A.M., 2008,

“The Magnetic Landscape of the Sun’s Polar Region”, Astrophys. J., 688, 1374–1381.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...688.1374T

Tu, C.-Y., Marsch, E., 1994, “On the nature of compressive fluctuations in the solar wind”, J. Geophys.

Res., 99, 21 481–21 509.

ADS: http://adsabs.harvard.edu/abs/1994JGR....9921481T Tu, C.-Y., Marsch, E., 1995, “MHD Structures, Waves and Turbulence in the Solar Wind: Observations and

Theories”, Space Sci. Rev., 73, 1–210.

ADS: http://adsabs.harvard.edu/abs/1995SSRv...73....1T Tu, C.-Y., Marsch, E., 1997, “Two-fluid model for heating of the solar corona and acceleration of the solar

wind by high-frequency Alfvén waves”, Solar Phys., 171, 363–391.

ADS: http://adsabs.harvard.edu/abs/1997SoPh..171..363T Tu, C.-Y., Marsch, E., 2001, “On cyclotron wave heating and acceleration of solar wind ions in the outer

corona”, J. Geophys. Res., 106, 8233–8252.

ADS: http://adsabs.harvard.edu/abs/2001JGR...106.8233T Tu, C.-Y., Marsch, E., Wilhelm, K., Curdt, W., 1998, “Ion Temperatures in a Solar Polar Coronal Hole

Observed by SUMER on SOHO”, Astrophys. J., 503, 475–482.

ADS: http://adsabs.harvard.edu/abs/1998ApJ...503..475T Tu, C.-Y., Zhou, C., Marsch, E., Xia, L.-D., Zhao, L., Wang, J.-X., Wilhelm, K., 2005, “Solar wind origin

in coronal funnels”, Science, 308, 519–523.

ADS: http://adsabs.harvard.edu/abs/2005Sci...308..519T Usmanov, A.V., Goldstein, M.L., 2006, “A three-dimensional MHD solar wind model with pickup protons”,

J. Geophys. Res., 111, A07 101.

ADS: http://adsabs.harvard.edu/abs/2006JGRA..11107101U van Ballegooijen, A.A., 1994, “Energy release in stellar magnetospheres”, Space Sci. Rev., 68, 299–307.

ADS: http://adsabs.harvard.edu/abs/1994SSRv...68..299V

van de Hulst, H.C., 1950, “The electron density of the solar corona”, Bull. Astron. Inst. Netherlands, 11,

135–150.

ADS: http://adsabs.harvard.edu/abs/1950BAN....11..135V

56


---


Vaquero, J.M., 2003, “The Solar Corona in the Eclipse of 24 June 1778”, Solar Phys., 216, 41–45.

ADS: http://adsabs.harvard.edu/abs/2003SoPh..216...41V

Vasquez, B.J., Hollweg, J.V., 1996, “Formation of arc-shaped Alfvén waves and rotational discontinuities

from oblique linearly polarized wave trains”, J. Geophys. Res., 101, 13,527–13,540.

ADS: http://adsabs.harvard.edu/abs/1996JGR...10113527V Vasquez, B.J., Hollweg, J.V., 1998, “Formation of spherically polarized Alfvén waves and imbedded rota-

tional discontinuities from a small number of entirely oblique waves”, J. Geophys. Res., 103, 335–347.

ADS: http://adsabs.harvard.edu/abs/1998JGR...103..335V Verdini, A., Velli, M., 2007, “Alfvén waves and turbulence in the solar atmosphere and solar wind”, Astro-

phys. J., 662, 669–676.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...662..669V Verdini, A., Velli, M., Buchlin, E., 2009, “Reflection Driven MHD Turbulence in the Solar Atmosphere and

Wind”, Earth, Moon, & Planets, 104, 121–125.

ADS: http://adsabs.harvard.edu/abs/2009EM&P..104..121V Voitenko, Y.M., Goossens, M., 2002, “Excitation of high-frequency Alfvén waves by plasma outflows from

coronal reconnection events”, Solar Phys., 206, 285–313.

ADS: http://adsabs.harvard.edu/abs/2002SoPh..206..285V Voitenko, Y.M., Goossens, M., 2003, “Kinetic excitation mechanisms for ion-cyclotron kinetic Alfvén

waves in Sun-Earth connection”, Space Sci. Rev., 107, 387–401.

ADS: http://adsabs.harvard.edu/abs/2003SSRv..107..387V Voitenko, Y.M., Goossens, M., 2004, “Cross-Field Heating of Coronal Ions by Low-Frequency Kinetic

Alfvén Waves”, Astrophys. J. Lett., 605, L149–L152.

ADS: http://adsabs.harvard.edu/abs/2004ApJ...605L.149V

von Steiger, R., Wimmer-Schweingruber, R.F., Geiss, J., Gloeckler, G., 1995, “Abundance variations in the

solar wind”, Adv. Space Res., 15, 3–12.

ADS: http://adsabs.harvard.edu/abs/1995AdSpR..15Q...3V Vranjes, J., Poedts, S., 2008, “Growing drift-cyclotron modes in the hot solar atmosphere”, Astron. Astro-

phys., 482, 653–656.

ADS: http://adsabs.harvard.edu/abs/2008A&A...482..653V Vršnak, B., Temmer, M., Veronig, A.M., 2007, “Coronal Holes and Solar Wind High-Speed Streams: I.

Forecasting the Solar Wind Parameters”, Solar Phys., 240, 315–330.

ADS: http://adsabs.harvard.edu/abs/2007SoPh..240..315V Waldmeier, M., 1955, “Ergenbnisse der Zürcher Sonnenfinsternisexpedition 1954: 1. Vorläufige Photome-

trie der Korona, Mit 7 Textabbildungen”, Zeit. Astrophysik, 36, 275–292.

ADS: http://adsabs.harvard.edu/abs/1955ZA.....36..275W Waldmeier, M., 1956, “Synoptische Karten der Sonnenkorona”, Zeit. Astrophysik, 38, 219–236.

ADS: http://adsabs.harvard.edu/abs/1956ZA.....38..219W

Waldmeier, M., 1957, Die Sonnenkorona, vol. 2, Birkhäuser, Basel Waldmeier, M., 1975, “The coronal hole at the 7 March 1970 solar eclipse”, Solar Phys., 40, 351–358.

ADS: http://adsabs.harvard.edu/abs/1975SoPh...40..351W

57


---


Waldmeier, M., 1981, “Cyclic variations of the polar coronal hole”, Solar Phys., 70, 251–258.

ADS: http://adsabs.harvard.edu/abs/1981SoPh...70..251W

Wang, C.B., Wu, C.S., 2009, “Pseudoheating of protons in the presence of Alfvénic turbulence”, Phys.

Plasmas, 16, 020 703.

ADS: http://adsabs.harvard.edu/abs/2009PhPl...16b0703W Wang, P.K., Siscoe, G.L., 1980, “Ancient Chinese Observations of Physical Phenomena Attending Solar

Eclipses”, Solar Phys., 66, 187–193.

ADS: http://adsabs.harvard.edu/abs/1980SoPh...66..187W Wang, Y.-M., 1994, “Polar plumes and the solar wind”, Astrophys. J. Lett., 435, L153–L156.

ADS: http://adsabs.harvard.edu/abs/1994ApJ...435L.153W

Wang, Y.-M., 1998, “Network Activity and the Evaporative Formation of Polar Plumes”, Astrophys. J. Lett.,

501, L145–L148.

ADS: http://adsabs.harvard.edu/abs/1998ApJ...501L.145W Wang, Y.-M., 2009, “Coronal holes and open magnetic flux”, Space Sci. Rev., 144, 383–399.

ADS: http://adsabs.harvard.edu/abs/2009SSRv..144..383W

Wang, Y.-M., Sheeley Jr, N.R., 1990, “Solar wind speed and coronal flux-tube expansion”, Astrophys. J.,

355, 726–732.

ADS: http://adsabs.harvard.edu/abs/1990ApJ...355..726W Wang, Y.-M., Sheeley Jr, N.R., 1991, “Why fast solar wind originates from slowly expanding coronal flux

tubes”, Astrophys. J. Lett., 372, L45–L48.

ADS: http://adsabs.harvard.edu/abs/1991ApJ...372L..45W Wang, Y.-M., Sheeley Jr, N.R., 2006, “Sources of the Solar Wind at Ulysses during 1990–2006”, Astrophys.

J., 653, 708–718.

ADS: http://adsabs.harvard.edu/abs/2006ApJ...653..708W Wang, Y.-M., Hawley, S.H., Sheeley Jr, N.R., 1996, “The magnetic nature of coronal holes”, Science, 271,

464–469.

ADS: http://adsabs.harvard.edu/abs/1996Sci...271..464W Wang, Y.-M., Sheeley Jr, N.R., Socker, D.G., Howard, R.A., Brueckner, G.E., Michels, D.J., Moses, D.,

St. Cyr, O.C., Llebaria, A., Delaboudinière, J.-P., 1998, “Observations of Correlated White-Light and

Extreme-Ultraviolet Jets from Polar Coronal Holes”, Astrophys. J., 508, 899–907.

ADS: http://adsabs.harvard.edu/abs/1998ApJ...508..899W

Wang, Y.-M., Sheeley Jr, N.R., Socker, D.G., Howard, R.A., Rich, N.B., 2000, “The dynamical nature of

coronal streamers”, J. Geophys. Res., 105, 25 133–25 142.

ADS: http://adsabs.harvard.edu/abs/2000JGR...10525133W Wang, Y.-M., Biersteker, J.B., Sheeley Jr, N.R., Koutchmy, S., Mouette, J., Druckmüller, M., 2007, “The

Solar Eclipse of 2006 and the Origin of Raylike Features in the White-Light Corona”, Astrophys. J., 660,

882–892.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...660..882W

Wang, Y.-M., Ko, Y.-K., Grappin, R., 2009, “Slow Solar Wind from Open Regions with Strong Low-

Coronal Heating”, Astrophys. J., 691, 760–769.

ADS: http://adsabs.harvard.edu/abs/2009ApJ...691..760W

58


---


Warren, H.P., Mariska, J.T., Wilhelm, K., Lemaire, P., 1997, “Doppler Shifts and Nonthermal Broadening

in the Quiet Solar Transition Region: O VI”, Astrophys. J. Lett., 484, L91–L94.

ADS: http://adsabs.harvard.edu/abs/1997ApJ...484L..91W Wilcox, J.M., 1968, “The Interplanetary Magnetic Field. Solar Origin and Terrestrial Effects”, Space Sci.

Rev., 8, 258–328.

ADS: http://adsabs.harvard.edu/abs/1968SSRv....8..258W Wilhelm, K., 2006, “Solar coronal-hole plasma densities and temperatures”, Astron. Astrophys., 455, 697–

708.

ADS: http://adsabs.harvard.edu/abs/2006A&A...455..697W Wilhelm, K., Curdt, W., Marsch, E., Schühle, U., Lemaire, P., Gabriel, A., Vial, J.-C., Grewing, M., Huber,

M.C.E., Jordan, S.D., Poland, A.I., Thomas, R.J., Kühne, M., Timothy, J.G., Hassler, D.M., Siegmund,

O.H.W., 1995, “SUMER: Solar Ultraviolet Measurements of Emitted Radiation”, Solar Phys., 162, 189–

231.

ADS: http://adsabs.harvard.edu/abs/1995SoPh..162..189W Wilhelm, K., Dammasch, I.E., Marsch, E., Hassler, D.M., 2000, “On the source regions of the fast solar

wind in polar coronal holes”, Astron. Astrophys., 353, 749–756.

ADS: http://adsabs.harvard.edu/abs/2000A&A...353..749W

Wilhelm, K., Dwivedi, B.N., Marsch, E., Feldman, U., 2004, “Observations of the Sun at Vacuum-

Ultraviolet Wavelengths from Space, I: Concepts and Instrumentation”, Space Sci. Rev., 111, 415–480.

ADS: http://adsabs.harvard.edu/abs/2004SSRv..111..415W Wilhelm, K., Marsch, E., Dwivedi, B.N., Feldman, U., 2007, “Observations of the Sun at Vacuum-

Ultraviolet Wavelengths from Space, II: Results and Interpretations”, Space Sci. Rev., 133, 103–179.

ADS: http://adsabs.harvard.edu/abs/2007SSRv..133..103W Withbroe, G.L., 1988, “The temperature structure, mass, and energy flow in the corona and inner solar

wind”, Astrophys. J., 325, 442–467.

ADS: http://adsabs.harvard.edu/abs/1988ApJ...325..442W Withbroe, G.L., Kohl, J.L., Weiser, H., Munro, R.H., 1982, “Probing the solar wind acceleration region

using spectroscopic techniques”, Space Sci. Rev., 33, 17–52.

ADS: http://adsabs.harvard.edu/abs/1982SSRv...33...17W Woo, R., 2005, “Relating White-Light Coronal Images to Magnetic Fields and Plasma Flow”, Solar Phys.,

231, 71–85.

ADS: http://adsabs.harvard.edu/abs/2005SoPh..231...71W Woo, R., 2006, “Ultra-fine-Scale Filamentary Structures in the Outer Corona and the Solar Magnetic Field”,

Astrophys. J. Lett., 639, L95–L98.

ADS: http://adsabs.harvard.edu/abs/2006ApJ...639L..95W Woo, R., Druckmüllerová, H., 2008, “Solar Eclipse Images and the Solar Wind”, Astrophys. J. Lett., 678,

L149–L152.

ADS: http://adsabs.harvard.edu/abs/2008ApJ...678L.149W Woo, R., Habbal, S.R., Howard, R.A., Korendyke, C.M., 1999, “Extension of the Polar Coronal Hole

Boundary into Interplanetary Space”, Astrophys. J., 513, 961–968.

ADS: http://adsabs.harvard.edu/abs/1999ApJ...513..961W

59


---


Woo, R., Habbal, S.R., Feldman, U., 2004, “Role of Closed Magnetic Fields in Solar Wind Flow”, Astro-

phys. J., 612, 1171–1174.

ADS: http://adsabs.harvard.edu/abs/2004ApJ...612.1171W Wood, B.E., 2004, “Astrospheres and Solar-like Stellar Winds”, Living Rev. Solar Phys., 1, lrsp-2004-2.

URL (cited on 1 July 2009):

http://www.livingreviews.org/lrsp-2004-2 Wood, B.E., Karovska, M., Cook, J.W., Howard, R.A., Brueckner, G.E., 1999, “Kinematic Measurements

of Polar Jets Observed by the Large-Angle Spectrometric Coronagraph”, Astrophys. J., 523, 444–449.

ADS: http://adsabs.harvard.edu/abs/1999ApJ...523..444W Wu, C.S., Yoon, P.H., 2007, “Proton heating via nonresonant scattering off intrinsic Alfvénic turbulence”,

Phys. Rev. Lett., 99, 075001.

ADS: http://adsabs.harvard.edu/abs/2007PhRvL..99g5001W Wu, D.J., Yang, L., 2006, “Anisotropic and mass-dependent energization of heavy ions by kinetic Alfvén

waves”, Astron. Astrophys., 452, L7–L10.

ADS: http://adsabs.harvard.edu/abs/2006A&A...452L...7W Wu, D.J., Yang, L., 2007, “Nonlinear interaction of minor heavy ions with kinetic Alfvén waves and their

anisotropic energization in coronal holes”, Astrophys. J., 659, 1693–1701.

ADS: http://adsabs.harvard.edu/abs/2007ApJ...659.1693W Yamauchi, Y., Suess, S.T., Sakurai, T., 2002, “Relation between Pressure Balance Structures and polar

plumes from Ulysses high latitude observations”, Geophys. Res. Lett., 29, 1383.

ADS: http://adsabs.harvard.edu/abs/2002GeoRL..29j..21Y Yang, L.-H., Jiang, Y.-C., Ren, D.-B., 2009, “Formation of Transient Coronal Holes during Eruption of a

Quiescent Filament and its Overlying Sigmoid”, Chinese J. Astron. Astrophys., accepted

Yoon, P.H., Fang, T.-M., 2008, “Parallel cascade of Alfvén waves”, Plasma Phys. Cont. Fusion, 50, 085007.

ADS: http://adsabs.harvard.edu/abs/2008PPCF...50h5007Y

Zangrilli, L., Nicolosi, P., Poletto, G., Noci, G., Romoli, M., Kohl, J.L., 1999, “Latitudinal properties of the

Lyman alpha and O VI profiles in the extended solar corona”, Astron. Astrophys., 342, 592–600.

ADS: http://adsabs.harvard.edu/abs/1999A&A...342..592Z Zhang, J., Woch, J., Solanki, S.K., von Steiger, R., Forsyth, R., 2003, “Interplanetary and solar surface

properties of coronal holes observed during solar maximum”, J. Geophys. Res., 108, 1144.

ADS: http://adsabs.harvard.edu/abs/2003JGRA..108.1144Z Zhang, J., Richardson, I.G., Webb, D.F., Gopalswamy, N., Huttunen, E., Kasper, J.C., Nitta, N.V.,

Poomvises, W., Thompson, B.J., Wu, C.-C., Yashiro, S., Zhukov, A.N., 2007, “Solar and interplane-

tary sources of major geomagnetic storms (Dst ≤ –100 nT) during 1996–2005”, J. Geophys. Res., 112,

A10 102.

ADS: http://adsabs.harvard.edu/abs/2007JGRA..11210102Z Zhang, T.X., 2003, “Preferential heating of particles by H-cyclotron waves generated by a global magneto-

hydrodynamic mode in solar coronal holes”, Astrophys. J. Lett., 597, L69–L72.

ADS: http://adsabs.harvard.edu/abs/2003ApJ...597L..69Z Zhou, Y., Matthaeus, W.H., 1990, “Transport and turbulence modeling of solar wind fluctuations”, J. Geo-

phys. Res., 95, 10 291–10 311.

ADS: http://adsabs.harvard.edu/abs/1990JGR....9510291Z

60


---


Zirin, H., 1975, “The helium chromosphere, coronal holes, and stellar X-rays”, Astrophys. J. Lett., 199,

L63–L66.

ADS: http://adsabs.harvard.edu/abs/1975ApJ...199L..63Z Zirker, J.B. (Ed.), 1977, Coronal Holes and High-speed Wind Streams, Colorado Assoc. Univ. Press, Boul-

der

Zurbuchen, T.H., Fisk, L.A., Gloeckler, G., von Steiger, R., 2002, “The solar wind composition throughout

the solar cycle: A continuum of dynamic states”, Geophys. Res. Lett., 29, 1352.

ADS: http://adsabs.harvard.edu/abs/2002GeoRL..29i..66Z

61


---

