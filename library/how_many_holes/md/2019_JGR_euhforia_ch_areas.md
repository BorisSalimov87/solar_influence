manuscript submitted to *JGR: Space Physics*

## Reconstructing coronal hole areas with EUHFORIA and adapted WSA model: optimising the model

parameters

E. Asvestari¹
*;*2, S. G. Heinemann¹, M. Temmer¹, J. Pomoell², E. Kilpua², J. Magdalenic³, S. Poedts⁴

1 Institute of Physics, University of Graz, Universitatsplatz 5, 8010 Graz, Austria 2 Department of Physics, University of Helsinki, P.O. Box 64, 00014 Helsinki, Finland 3 Solar-Terrestrial Centre of Excellence-SIDC, Royal Observatory of Belgium, 1180 Brussels, Belgium 4 Centre for mathematical Plasma Astrophysics (CmPA), KU Leuven, 3001 Leuven, Belgium

### Key Points:

We assess the capability of the PFSS+SCS models adopted by EUHFORIA in re- constructing CH areas. The heights of the source surface and the inner boundary of the SCS model im- pact the results. Lower values for these two heights improved the results.

# arXiv:1907.03337v1 [astro-ph.SR] 7 Jul 2019

Corresponding author: Eleanna Asvestari, eleanna.asvestari@helsinki.fi

{1{

Abstract The adopted WSA model embedded in EUHFORIA (EUropean Heliospheric FORecast- ing Information Asset) is compared to EUV observations. According to the standard paradigm coronal holes are sources of open ux thus we use remote sensing EUV observations and catch (Collection of Analysis Tools for Coronal Holes) to extract CH areas and com- pare them to the open ux areas modelled by EUHFORIA. From the adopted WSA model we employ only the Potential Field Source Surface (PFSS) model for the inner corona and the Schatten Current Sheet (SCS) model for the outer (PFSS+SCS). The height, *R*ss, of the outer boundary of the PFSS, known as the source surface, and the height, *R*i, of the inner boundary of the SCS are important parameters aecting the modelled CH areas. We investigate the impact the two model parameters can have in the mod- elled results. We vary *R*sswithin the interval [1.4, 3.2]*R* with a step of 0.1*R*, and *R*i within the interval [1.3, 2.8]*R* with the same step, and the condition that *R*i*< R*ss. This way we have a set of 184 initial parameters to the model and we assess the model results for all these possible height pairs. We conclude that the default heights used so far fail in modelling accurately CH areas and lower heights need to be considered.

### 1 Introduction

The ambient Solar Wind (SW) and the frozen-in open magnetic eld sculpt the medium through which Coronal Mass Ejections (CMEs) and Solar Energetic Particles (SEPs) prop- agate. Consequently, modelling the solar wind with high accuracy is a signicant com- ponent towards more reliable space weather forecasts. Fast SW and open magnetic eld are primarily associated with Coronal Holes (CHs) (Levine et al., 1977; Wang et al., 1996; Schwenn, 2006a, 2006b), which in X-ray and extreme-ultraviolet (EUV) imaging obser- vations can be identied as dark structures in the solar corona. Their dark appearance at these wavelengths is a result of having signicantly lower density and temperature com- pared to their surroundings. Although a plethora of both empirical and intricate mag- netohydrodynamic (MHD) models exist, due to its simplicity and comparability to com- putationally expensive MHD ones (Riley et al., 2006; MacNeice et al., 2018), the semi- empirical Wang-Sheeley-Arge (WSA) model (Arge & Pizzo, 2000) is the model most com- monly employed for estimating the solar wind ow close to the Sun. It’s magnetic eld model comprises the Potential Field Source Surface (PFSS) (Altschuler & Newkirk, 1969; Schatten et al., 1969) and the Schatten Current Sheet (SCS) (Schatten, 1971) models to extract the solar wind speed and the magnetic eld in the corona. And then by us- ing a 1D kinematic scheme attempts to predict the solar wind speed at Earth.

Being an empirical model, the WSA consists of a parametrisation including sev- eral free parameters, which throughout the decades have been tted and re-tted to con- form in{situ observations of the solar wind plasma at 1AU. One such parameter is the height of the outer boundary of the PFSS model, known as the source surface. In the traditional WSA model it serves as the inner boundary to the SCS model (Wang & Shee- ley, 1990, 1992; Arge & Pizzo, 2000). The source surface and its distance from the Sun, Rss, divides the corona into two zones; the inner and outer. Field lines piercing through the source surface are considered as open, while those forming closed loops below it are identied as belonging to closed magnetic structures. Open eld lines are stretched out and away in the Heliosphere by the solar wind forming the Interplanetary Magnetic Field (IMF) (e.g., Wang & Sheeley, 2003). The PFSS does not account for dynamic eects that are especially important at the top of streamers (e.g., the high closed loops Arge et al.,

2002). Due to the association of open eld to CHs, the areas on the source surface that are dened by concentration of open eld lines map down to the low corona to CHs, i.e. each eld line that is open is rooted in the low corona to (one or more) CHs. The loca- tion/height of *R*ssdetermines strongly the total area of open eld regions rooted in the low corona. Lowering *R*sswill result in more eld lines being open, and subsequently in larger areas of CHs. On the contrary, increasing it will reduce the number of open eld
{2{

lines and thus shrinking CH areas. This is visualised in panel (a) of Figure 1, where chang- ing the source surface from height *a* to *b* and *c* expands the areas of open ux. Qual- itatively some eld lines that were forming closed loops for the case of a source surface at height *a* are crossing through the source surface placed at height *b* and therefore are not considered closed anymore. Decreasing the height even lower to height *c* will result in increasing the number of closed loops that are becoming open, and therefore, in fur- ther growing of the open ux areas.

Since fast solar wind and open magnetic eld are related to CHs, for the WSA model to successfully reconstruct the in-situ measured solar wind properties and the open mag- netic ux, it should model the size and geometry of CHs as accurately as possible. The dependence of the latter on the source surface height makes the choice of *R*ssa deni- tive element in the model’s success.

(a) (b)
Figure 1. (a) Schematic representation of the impact of the source surface height in the open

and closed eld line assignment. Lines a (thin blue line), b (thin magenta line) and c (thin green line) illustrate three possible positions for the source surface. The lower it is placed the more eld lines are considered as open. To visualise this we added the thicker lines at the lower part of the image, with representative colours, which show how the area the open eld lines map down to grows the lower the source surface is placed. (b) An illustration depicting the coronal domain divided into the inner and outer corona by the source surface (grey circle). The red dotted circle represent the inner boundary of the SCS model which approximates the magnetic eld in the outer corona.

Selecting the optimal source surface height has been a long-standing debate. Ear- lier studies (e.g., Altschuler & Newkirk, 1969) indicated that the source surface is best placed at 2.5*R* (*R* = 1 solar radius). This value has been adopted by many as the canon- ical height; however, a range of values from 1.6*R* to 3.25*R* have been used (e.g., Ar- den et al., 2014). Criteria for the choice of these values have been (i) the sector struc- ture of the Heliospheric Current Sheet (HCS) (Hoeksema et al., 1982, 1983; Hoeksema & Scherrer, 1986), (ii) in-situ and remote observations of the HCS by Ulysses (Phillips et al., 1994; Wang & Sheeley, 1995) and during total solar eclipses (Schatten et al., 1969), (iii) the interplanetary magnetic eld polarity (Hoeksema et al., 1983), (iv) the coronal hole boundaries and (v) the Interplanetary Magnetic Field (IMF) strength (e.g., Lee et al., 2011). While plenty of studies were restricted to and/or concluded the use of a sin- gular value for *R*ss(Altschuler & Newkirk, 1969; Hoeksema et al., 1983; Arge & Pizzo, 2000; McGregor et al., 2008; Wang, 2009; Riley et al., 2015; Linker et al., 2017), others have been suggesting a solar cycle dependant source surface height (e.g., Lee et al., 2011; Arden et al., 2014), a concept known as the "breathing" source surface (termed by Ar-

{3{

den et al., 2014). In addition to that concept, the idea of a non-spherically shaped source surface has also been proposed (e.g., Levine et al., 1977; Schulz, 1997, 2008).

Aiming to eliminate a known discontinuity in the WSA model, namely kinks in the eld lines occurring at the transition from the low{coronal PFSS to the high{coronal SCS domain, McGregor et al. (2008) re-positioned the inner boundary of the SCS model at a radius *R*ilower than the source surface (*R*i*< R*ss). This concept is illustrated in Fig- ure 1 panel b, where the red dashed curve encircling the Sun represents the new inner boundary of the SCS model, and the grey solid curve is the source surface placed at height *R*ss. In establishing the optimal pair of [*R*i*; R*ss] heights for their new adaptation of the WSA model McGregor et al. (2008) aimed for conservation of the absolute total mag- netic ux between the one from the original WSA model and that from their updated version. The purpose of that was to facilitate the comparison between the two models, original and improved WSA. The pair they deduced in their study, is [2.3, 2.6]*R* for *R*i and *R*ssrespectively.

EUHFORIA (EUropean Heliospheric FORecasting Information Asset) is a novel heliospheric wind and CME evolution model (Pomoell & Poedts, 2018) consisting of two main building blocks, the coronal model and the heliospheric full MHD model. The coro- nal model aims to reconstruct the solar wind plasma and the open ux conditions in the upper corona at 21.5*R*, which serve as boundary conditions to the heliospheric model. It implements for that purpose the WSA model, with the McGregor et al. (2008) improve- ments (for more details read Pomoell & Poedts, 2018). The default [*R*i*; R*ss] pair of heights is the one proposed by McGregor et al. (2008). In a comprehensive study of modelling the background solar wind with EUHFORIA using the adopted WSA model and default heights (Hinterreiter et al., to be submitted, in preparation) it became evident that the capability of the model to predict a high-speed stream at Earth is often quite low, with predicted high speed streams either shifted in time, having lower than expected ampli- tude in the solar wind speed proles or being overall absent. Similar results have been reported in other physics-based reconstructions of the ambient solar wind (Owens et al., 2008; Lee et al., 2009; Jian et al., 2011; Gressl et al., 2014). The novelty of our study is the assessment of the PFSS+SCS capability to reconstruct CH areas with accuracy, knowing the relation between CHS and high speed streams.

In the model the source surface and the SCS inner boundary positions are adjustable parameters. Considering the freedom in the choice of the source surface height, already brought forward by other studies discussed above, we focused rstly in qualitatively as- sessing the default values of [*R*i*; R*ss], and subsequently in investigating the possibility of other height choices. To do that, we selected a sample of 15 CHs located around the central meridian of the solar disk as viewed from Earth, but at dierent latitudes (see section 2.2). Using catch (Collection of Analysis Tools for Coronal Holes) (Heinemann et al., 2019, in preparation) we extracted the boundaries of these CHs based on their ap- pearance in EUV ltergrams at 193 A (section 2.3). We reconstructed their areas with EUHFORIA, by varying the paired values for the heights of the source surface and the inner boundary of the SCS model, in order to nd optimal values that produce a bet- ter match between modelled and observed CH areas (section 2.4). A quantitative anal- ysis of the results was performed by dening two parameters, the coverage and the con- nected pixels of open ux associated to the CH (both parameters are analytically described in section 3).

{4{

From this study we conclude that the PFSS+SCS part of the adopted WSA model for the default heights of [2.3, 2.6]*R* does not properly reconstruct CH areas. Lower- ing the heights [*R*i*; R*ss] improved the model results, i.e. open eld lines are rooted to areas in the lower corona that better represented the CHs observed in EUV images. How- ever, it also led in the presence of open eld lines that mapped down to the corona at areas lying outside the CH boundaries dened via observations. This is an undesirable modelling eect and we attempted to identify optimal height pair candidates by select- ing those who lead to a modelling result that has improved CH area reconstruction with- out expanding the CH area beyond the expected boundaries.

Figure 2. EUV ltergrams at 193 A depicting the selected CHs in chronological order. The

red curves mapping out the boundaries of the CHs are the optimal ones dened using catch.

{5{

### 2 Data and Methodologies

2.1 Observations To compute the solar wind and magnetic eld in the corona the WSA model re-
quires a magnetogram as input. A variety of magnetograms are available; however, they are obtained at dierent observatories, using dierent instruments, and constructed fol- lowing various distinct techniques. Therefore, they display quantitative dierences among each other (Riley et al., 2014). Aiming in a coherent output and to avoid any eects on the modelled results due to disparities between magnetograms from dierent sources we used exclusively magnetograms provided by the Global Oscillation Network Group (GONG) and developed with the Air Force Data Assimilative Photospheric ux Transport (ADAPT) model. These are synchronic magnetograms, meaning they are developed such as to re- semble with high accuracy the magnetic eld of the solar surface on a particular time. A detailed description of the ADAPT model can be found in Arge et al. (2010) and Hickmann et al. (2015), while the GONG-ADAPT database from which magnetograms were acquired is: ftp://gong.nso.edu/adapt/maps/gong/.

For extracting the CH boundaries we used EUV observations during 2012 - 2017 from the Atmospheric Imaging Assembly (AIA: Lemen et al., 2012) on board the Solar Dynamic Observatory (SDO: Pesnell et al., 2012). For this study we utilized the full disk coronal images (1024 1024) at a wavelength of 193 A, which are made available by the Joint Science Operation Center (JSOC). Although, it is argued that CHs appear dif- ferently when observed at dierent wavelengths, i.e. varying boundaries, the 193 A l- ter is most commonly used. The response function of this lter is most sensitive in the temperature range of quiet sun and CH regions resulting in a high contrast. Using these data, we extract the CH area and its boundary in a manner described in section 2.3.

2.2 Selected Coronal Holes The 15 selected CHs are shown in chronological order in Figure 2. As mentioned
earlier, all CHs have longitudinal position of centre of mass (CoM) located along or within 10 of the central meridian of the Sun. The latitudinal position of their CoM, however, varies from low to high. Limiting the sample to CHs located only along the central merid- ional zone provides the opportunity to focus our assessment on the possible impact of the CH latitudinal position in modelling their areas. In addition, the sample covers the extended maximum, declining, and early minimum phases of solar cycle 24, from 2012 to 2017, enabling the investigation of potential solar activity eects in reconstructing CHs and thus in the choice of the source surface height, an idea that has been suggested be- fore (Lee et al., 2011; Arden et al., 2014).

Out of the 15 CHs, 11 are latitudinally and 3 longitudinally elongated, while one is rather small and bears a more round appearance. Regarding their CoM latitude, 5 and 3 CHs are low latitude ones positioned in the north and south hemisphere respectively, while 5 and 2 CHs are mid latitude ones in north and south hemisphere accordingly. Due to known weaknesses on magnetic eld and EUV observations in polar regions (i.e. line- of-site eects) no polar CHs were selected for this study; however, the CH on the 2017- 01-03 is clearly connected to a polar CH, and is an exception to our sample. In this par- ticular case we do consider the polar part that is visible in the EUV image, acknowledg- ing the impact this will have on the result. The CH on 2016-12-20 appears to be asso- ciated to a polar one as well. A faint channeling between the CH and the polar one is visible in the EUV images. Nevertheless, we assess it individually as its boundaries can be dened and are separated from those of the polar CH. The sample also consists of CHs exhibiting dierent level of patchiness that is dened by the presence within the CH of large areas with a dipole magnetic eld conguration (i.e. 2017-01-03), or due to the CH consisting of a cluster of small dark regions (i.e. 2013-03-27).

{6{

Table 1. CH characteristics based on remote sensing observations and catch extractions,

where CoM is Centre of Mass

|No|Date-time|CoM|latitude|CoM|longitude|Area|Mean intensity|
|---|---|---|---|---|---|---|---|
|||||||10||
||[UTC]||[deg]||[deg]|[10 km²|] [DN]|
|1|20120113T12:00||5.01||10.07|2.34 0.12|36.31 0.86|
|2|20120603T18:00||13.04||0.91|9.69 0.33|31.29 0.62|
|3|20120609T18:00||34.97||0.18|2.02 0.16|44.60 1.36|
|4|20130123T12:00||-44.45||4.70|6.03 0.16|27.79 0.62|
|5|20130327T06:00||16.71||4.93|3.37 0.42|38.28 1.02|
|6|20130523T18:00||38.61||3.18|6.91 0.36|29.30 0.81|
|7|20130530T06:01||1.69||2.76|8.07 0.24|26.68 0.56|
|8|20131212T05:59||36.52||3.75|17.16 0.88|38.59 1.17|
|9|20140118T17:58||34.53||6.24|6.34 0.34|35.83 1.17|
|10|20140306T12:00||27.46||3.23|6.71 0.43|38.80 1.09|
|11|20140624T18:00||-6.74||1.10|1.95 0.06|29.45 0.57|
|12|20140724T12:10||-3.53||2.21|2.16 0.05|25.70 0.46|
|13|20161220T12:10||-13.86||0.92|10.55 0.46|22.31 0.54|
|14|20161228T12:00||-4.77||1.12|4.84 0.16|25.58 0.45|
|15|20170103T00:00||-43.35||6.21|42.18 0.71|19.00 0.32|

### CoM: Centre of Mass

2.3 Extracting CH boundaries with CATCH The CH boundaries were extracted using catch (Heinemann et al., 2019, in prepa-
ration) employing EUV 193 A ltergrams from AIA/SDO. catch uses an intensity thresh- old method enhanced with a gradient modulation at the CH boundary to nd an opti- mal threshold for the extraction. For better quantifying the uncertainties in the PFSS+SCS computed open magnetic eld when comparing to the coronal remote sensing observa- tions, in addition to the optimal CH boundary we also dene lower and upper bounds for each CH. The lower and upper bounds present a signicantly over- and underesti- mated threshold for the extraction.

2.4 Reconstructing CH areas with EUHFORIA The reconstruction of open ux areas was done using EUHFORIA. As already de-
scribed in the introduction, EUHFORIA consists of two main building blocks, with the corona model being one of them. It employs the adaptation of the WSA model with the scheme suggested by McGregor et al. (2008), which comprises two sub-models, the PFSS and the SCS. The rst computes the magnetic eld and plasma conditions in the lower corona, from 1*R* up to the source surface, at height *R*ss. And the latter solves the mag- netic eld and plasma conditions in the outer corona, from *R*i*< R*ssup to 21.5*R*. Al- though, the PFSS model solution extends to the source surface, it forces the magnetic eld there to be purely radial. This conguration is causing unrealistic eld line kinks at the source surface in the magnetic eld solution of the SCS model when its inner bound- ary is taken to be the source surface (McGregor et al., 2008). This is the reason why we select as the inner boundary conditions to the SCS model a solution of the PFSS at a surface *R*ibelow the source surface where the magnetic eld has all components. For each of the selected CHs we run the coronal model of EUHFORIA for a large sample of [*R*i, *R*ss] heights. To dene the height pairs we started with *R*itaking the value of 1.3*R* up to 2.8*R* with a step of 0.1*R*, and for each *R*iwe varied *R*ssfrom 1.4*R* to 3.2*R* with the same step. ADAPT magnetograms, at date{time same as that of the EUV images

{7{

analysed, were used as input to EUHFORIA which then produced maps of the open and closed magnetic regions for the specied input heights *R*iand *R*ss.

To create these open-closed ux maps the solar surface is divided in a regular mesh consisting of pixels covering 2x2 degrees per pixel. For each pixel the procedure assigns a eld line and traces it from the solar surface upwards towards the source surface. If the tracked eld line is curved below the source surface and can be traced back down to the solar surface it is assigned as a closed one. Per contra, if the traced eld line pierces through the source surface it is accredited as an open one. Examples of open-closed eld areas are given in Figure 3, where dark blue and red colours represent areas of open ux, with positive and negative polarity respectively, while light blue and orange areas are correspondingly closed ux areas. The light green contours are the optimal CH bound- aries derived from EUV observations using catch, as described in the previous section. The results presented in this gure are the output of the model run for the default pair of heights, [2.3, 2.6]*R*. To better visualise the modelled CH area and the over-plotted EUV based boundaries, especially in the cases of very small CHs, we only plot in Fig- ure 3 the front side of the Sun (Earth view). In addition, for CHs that do not extend to polar regions, high latitudes of northern and southern hemisphere are excluded from the images.

### 3 Results

3.1 CH reconstruction using the default model boundary heights The examples in Figure 3 display maps based on the default pairs of heights [2.3,
2.6]*R* used as default values in EUHFORIA. These values are the ones concluded in McGregor et al. (2008). It is clear from this gure that, for the majority of the CHs, the model runs based on the default heights [2.3, 2.6]*R* fail in reconstructing well the area and geometry as compared to the EUV extraction. Not only are the CHs modelled thin- ner and overall smaller, but also for some cases (i.e. 2012-06-09, 2013-05-23, 2014-01-18) the CHs appear to be shifted. For the CH of 2014-06-24 the model is unsuccessful in mod- elling open ux both within the expected boundaries and in the surrounding area. This CH seems to be invisible for the PFSS+SCS models in the adopted WSA model. A CH that appears to be well modelled by EUHFORIA is the one on 2017-01-03, which is a southern polar CH with a large extension that reaches to low northern hemisphere lat- itudes. It is worth pointing out, however, that the CH boundaries extracted with catch are only for the part of the CH that is visible from Earth’s line-of-sight. This explains why also in the EUHFORIA output open/closed eld map we do not focus on longitudes beyond 90 degrees. In order to quantify how successful the model is in reconstructing coronal hole ar- eas we dene the coverage parameter, *cov*, which is given by:
<u>Nopen</u> *cov* = 100[%] (1) *Ntotal* where *Nopen*is the number of open ux pixels contained within the optimal catch bound- aries (green contour), and *Ntotal*is the total number of pixels enclosed by that same bound- ary (open and closed ux pixels). Low coverage indicates not only that the area size of the CH is not correctly modelled but also that the CH could possibly be modelled shifted in space. High coverage suggests that both area size and location are possibly well cap- tured by the model reconstruction of the CH. The coverage for the model results using the default source surface and SCS inner boundary heights, [2.3, 2.6]*R*, is given in the right panel of Figure 4 as green coloured circles. The x-axis is the nominal number of the CHs when they are accounted in chronological order (column 1 of table 1). It can be seen that for 13 out of the 15 CHs we studied the model gives a coverage below 60%, with the majority of CHs ranking below 30% coverage. This is a clear indication that the model under the default setup does not properly model the CH areas.

{8{

2012-01-13 11:59:00 60° 40° 20° 0° -20° -40° Heliographic Latitude [deg] -60° 285° 315° 345° 15° 45° 75° Heliographic Longitude [deg] 2013-01-23 11:59:00 60° 40° 20° 0° -20° -40° Heliographic Latitude [deg] -60° 285° 315° 345° 15° 45° 75° Heliographic Longitude [deg] 2013-05-29 23:59:00 60° 40° 20° 0° -20° -40° Heliographic Latitude [deg] -60° 285° 315° 345° 15° 45° 75° Heliographic Longitude [deg] 2014-03-06 11:59:00 60° 40° 20° 0° -20° -40° Heliographic Latitude [deg] -60° 285° 315° 345° 15° 45° 75° Heliographic Longitude [deg] 2016-12-20 12:00:00 60° 40° 20° 0° -20° -40° Heliographic Latitude [deg] -60° 285° 315° 345° 15° 45° 75° Heliographic Longitude [deg]

2012-06-03 18:00:00 60° 40° 20° 0° -20° -40° Heliographic Latitude [deg] -60° 285° 315° 345° 15° 45° 75° Heliographic Longitude [deg] 2013-03-27 05:59:00 60° 40° 20° 0° -20° -40° Heliographic Latitude [deg] -60° 285° 315° 345° 15° 45° 75° Heliographic Longitude [deg] 2013-12-12 05:59:00 60° 40° 20° 0° -20° -40° Heliographic Latitude [deg] -60° 285° 315° 345° 15° 45° 75° Heliographic Longitude [deg] 2014-06-24 15:59:00 60° 40° 20° 0° -20° -40° Heliographic Latitude [deg] -60° 285° 315° 345° 15° 45° 75° Heliographic Longitude [deg] 2016-12-28 12:00:00 60° 40° 20° 0° -20° -40° Heliographic Latitude [deg] -60° 285° 315° 345° 15° 45° 75° Heliographic Longitude [deg]

2012-06-09 17:59:00 60° 40° 20° 0° -20° -40° Heliographic Latitude [deg] -60° 285° 315° 345° 15° 45° 75° Heliographic Longitude [deg] 2013-05-23 17:59:00 60° 40° 20° 0° -20° -40° Heliographic Latitude [deg] -60° 285° 315° 345° 15° 45° 75° Heliographic Longitude [deg] 2014-01-18 17:59:00 60° 40° 20° 0° -20° -40° Heliographic Latitude [deg] -60° 285° 315° 345° 15° 45° 75° Heliographic Longitude [deg] 2014-07-24 11:59:00 60° 40° 20° 0° -20° -40° Heliographic Latitude [deg] -60° 285° 315° 345° 15° 45° 75° Heliographic Longitude [deg] 2017-01-03 00:00:00 40° 20° 0° -20° -40° -60° Heliographic Latitude [deg] -80° 270° 300° 330° 0° 15° 45° 75° Heliographic Longitude [deg]

{9{

Figure 3. Model generated maps of open-closed eld regions based on magnetic eld recon-

structions by the adopted WSA model in EUHFORIA. Dark blue and red regions represent open eld areas of positive and negative polarity respectively, while cyan and orange are accordingly positive and negative closed eld areas. The green outlines overplotted on the maps are the EUV dened optimal boundaries of the CHs as extracted with catch. Although, the model generates the map for the entire solar surface we plotted here a fraction of the map aiming to improve the clarity of the CH areas and the overplotted boundaries.

We also investigated the possibility of comparing the modelled CH areas to the ones dened by the smaller and larger area boundaries obtained from the EUV images using catch. An example of how these boundaries dier from each other is shown in the left panel of Figure 4. In yellow we show the smaller area boundaries and in magenta the larger area boundaries. For most CHs the dierences between the areas dened by the three dierent boundaries (small, optimal and large) is not that substantial. The cov- erage estimated for these is shown in corresponding colours in the right panel of the same gure. Although, smaller area boundaries, as expected, improve the coverage percent- age for the majority of the CHs, for some this improvement is not signicant (i.e. 2013- 01-23, 2013-05-23, 2014-03-06, 2014-06-24). For three CHs (i.e. 2012-01-13, 2012-06-09, 2013-03-27) the coverage worsens with the smaller boundaries. An explanation to this is that open ux pixels are lying outside the smaller area boundaries. This concludes that there is no systematic improvement if smaller area boundaries were to be obtained from the EUV observations when a smaller threshold is considered. In a similar manner, larger area boundaries do not worsen the result for all CHs.

Figure 4. The left panel is an example (CH No7) of how the dierent boundaries extracted

with catch can dier from each other. The colour scheme for open-closed ux of positive and negative polarity is similar to that in Figure 3. With green colour we illustrate the optimal CH boundary extracted with catch, while magenta and yellow coloured boundaries represent the ones obtained using an under- and overestimated thresholds, as described in section 2.3. The right panel shows the coverage achieved by the model when run for the default pair of heights, [2.3, 2.6]*R*, and when the three dierent boundaries (optimal, smaller and larger) are considered for the analysis. The face colours of the circles represent the colour of the boundary based on which the calculations were carried out.

3.2 CH characteristics and their eect The open closed ux maps given in Figure 3 and the coverage shown in Figure 4
indicate that the model performs better for some CHs comparing to others when the model runs are setup using the default pair of heights. In order to exclude the possibility of the model showing preference in better modelling CHs bearing particular features we assess how the coverage relates to CH characteristics. The elongation, latitudinal position of CoM, patchiness, area size, mean intensity are apparent features of a CH that are of in- terest to this study.

The elongation of a CH can have an eect to the modelled results due to the way the selected magnetograms are constructed. Even though dynamical processes are ap- plied to them, synchronic ADAPT magnetograms best represent the magnetic eld on the Sun along the central meridian as viewed from Earth. This suggests that CHs which are latitudinally elongated and lie within the central meridional zone can be possibly bet-

{10{

ter modelled when selecting a magnetogram from the date the CH was located there. Thus a longitudinally elongated CH might not be as accurate modelled at its full length. So when studying a CH on a particular moment can also have an impact to the modelled output based on that perspective.

CH mean intensity and area are parameters extracted using catch, as described in the section 2.3. The mean intensity is automatically computed with catch based on the threshold used for extracting the CH boundaries. It is expected that active regions in the vicinity of a CH will have an impact on its conguration, which is also imprinted on magnetograms, and thus has the potential to aect the modelled CH areas. The sam- ple’s average mean intensity is 31.3 DN, and only 6 out of the 15 CHs studied have mean intensity above that value. The size of a CH is expected to aect the width/duration of a high speed stream as well as its speed and open ux, and thus is a parameter we in- vestigate (Nolte et al., 1976; Vrnak et al., 2007; Rotter et al., 2012; Hofmeister et al., 2018). In terms of the area the CH sample consists of both small and large CHs, with the biggest on 2017-01-03 extending from polar to solar equatorial latitudes. The sample mean is 8*:* 7*x* 10 10 *km²* and 4 CHs have area above this value.

[2.6 - 2.3] Rs [2.6 - 2.3] Rs [2.6 - 2.3] Rs 70 70 70 60 60 60 50 50 50 40 40 40 30 30 30 Co erage (%) 20 Coverage (%) 20 Coverage (%) 20 10 10 10 0 0 0 −40 −20 0 20 40 20 25 30 35 40 45 0 10 20 10 30 2 40 Centre of Mass Latitude [deg] Mean Intensity[DN] Area [10 km]

Figure 5. Scatter plots showing the impact on the coverage that the CH characteristics such

as the centre of mass latitude, the mean intensity and the CH area have (left, middle and right panel respectively). The presented results are based on running the model for the default pair of heights [2.3, 2.6]*R* and indicate that neither CoM latitude, mean intensity or area had any eect in the performance of the model results. The red box encircles the south polar CH with the long extension to equatorial latitudes.

In Figure 5, the left panel presents the coverage with respect to the CoM latitude. From the level of scatter in the points it is clear that the latitudinal position of the CH does not aect the performance of the modelled result. The same applies for the other two parameters shown in the middle panel (Mean Intensity) and the right most panel (Area). For the case of large CHs we have only one point so the relation between cov- erage and area remains inconclusive. We also checked whether the visual characteristics of elongation and patchiness of a CH have any eect. No such conclusion could be made; however, the number of CHs is too low for the result to be compelling (for details see Asvestari et al., submitted, in preparation). We also accounted for the possibility of a coupling of dierent parameters, e.g. area or intensity and CoM latitude, which could have an eect in the modelled results. But even for this scenario no trend is apparent with respect to the coverage. One conclusion that could be made is that all CHs located in the south hemisphere of the Sun have low Mean Intensity, while those in the north- ern have high. This can possibly be a solar cycle related eect, since we studied CHs from one SC only (SC24), and indeed, from 2013-2015 southern hemisphere clearly dominated both in the number and in the area size of sunspots (Li et al., 2019) (see also sunspot number information at [http://www.sidc.be/silso/ssngraphics](http://www.sidc.be/silso/ssngraphics)). Our sample size is

{11{

rather small for an unambiguous conclusion to be made, so a more detailed analysis of a larger CH sample is necessary.

3.3 Assessing for systematic shifting and solar cycle trends Maps of open-closed ux indicated the possibility of shifting of the modelled CH
areas with respect to the expected location. To assess this we investigated the likelihood of a systematic shifting. All directions (eastward/westward and northward/southward) were investigated. In addition, we considered both a 2 and a 4 degree shift in each di- rection. From this analysis no systematic eect could be identied. The role of CH char- acteristics, such as mean intensity, elongation, size, CoM latitude, and hemispheric po- sition, in shifting eects was evaluated independently (Asvestari et al., submitted, in prepa- ration). Regardless of whether the sample is assessed as a whole or divided in groups based on the CH characteristics the conclusion for possible shifting remained negative for all cases.

In earlier studies (Lee et al., 2011; Arden et al., 2014) the concept of a solar cy- cle dependent source surface height has been suggested, i.e. varying within the course of the solar cycle, as well as, from one solar cycle to another. We investigated this prospect at rst for the whole CH sample and then by separating CHs to groups based on their apparent characteristics mentioned also in the shifting investigation. We found no so- lar cycle trends when assessing the result for the default heights, but also for our full set of [*R*i, *R*ss] heights and discussed below (for details see Asvestari et al., submitted, in preparation). We note that the number of considered CHs is rather small and therefore, no conclusive results can be drawn about the systematic shift. In addition, the period over which the sample extends does not cover a complete solar cycle, so to understand solar cycle eects on the modelling output it is important for such a study to consider a sample that spans over the entire solar cycle.

2014-06-24 15:59:00 2014-06-24 15:59:00 60° 60° 40° 40° 20° 20° 0° 0° -20°-20° -40°-40°

Heliographic Latitude [deg] -60° Heliographic Latitude [deg] -60° 285° 315° 345° 15° 45° 75° 285° 315° 345° 15° 45° 75°

|285°|315° 345°|15° 45°|75°|285°|315° 345°|15° 45°|75°|
|---|---|---|---|---|---|---|---|
||Heliographic Longitude [deg]||||Heliographic Longitude [deg]|||

Figure 6. Maps of open-closed ux generated for the same CH by two dierent model runs.

The one on the left resulted by EUHFORIA running for the default pair of heights [2.3, 2.6]*R*, while the one on the right for the pair [1.3, 1.8]*R*. It is clear that the CH is not present in the model result on the left, but is present and well captured by the run setup based on lower heights. This example highlights the impact the heights of the source surface and the inner boundary of the SCS model have in the modelling result.

3.4 Finding the optimum paired values for [*R*i, *R*ss] After running the model for all 184 pairs of [*R*i, *R*ss] heights, it was made evident
that lowering the source surface height signicantly improved the modelled CHs. One very clear example is that of 2014-06-24, shown in Figure 6. This particular CH was in-

{12{

visible in the open-closed ux maps created with the boundaries placed at the default pair of heights. As can be seen from the right panel in Figure 6 the model nicely maps the CH area when a lower pair of heights is considered. We specically compare the de- fault heights output to this one because the source surface height of 1.8*R* has been sug- gested by other studies as a better choice for particular periods and has been used in ear- lier studies for comparison purposes (e.g., Lee et al., 2011).

Figure 7. Collective results of model runs based on all the 184 pairs of heights for the source

surface and the inner boundary of the SCS model. Each panel presents the results for one CH, and they are placed in chronological order. The x-axis is the source surface height and the colour bar is the height of the inner boundary of the SCS model increasing from dark to bright colours. The y-axis shows the coverage. As can be seen, for the majority of CHs best coverage is achieved for lower height values for the inner boundary of the SCS model.

Figure 7 is a collective plot for the coverage resulting from the model runs for each

of the 184 height pairs and the 15 CHs. Each panel represents the results for a partic-

{13{

ular CH, while the x-axis is the source surface height, the y-axis the coverage and the colour map the height of the inner boundary of the SCS model, *R*i. The striking feature in this gure is that for the vast majority of the CHs reducing *R*isignicantly improves the modelled coverage. For some cases the coverage even rises from 0 to almost 100%. Overall, a lower source surface height has the same eect; however, for a xed low value *R*ia decrease in the source surface height does not necessarily have a high impact. The large CH that consisted of the southern polar one and its long extension to equatorial latitudes was very well modelled by EUHFORIA run with the default values. Lowering the values of the pair of heights below the default ones did result in improvement of the coverage; however as it was already high the improvement was not signicant (within 10%). The CH on 2013-03-27 is a very patchy CH that is not well modelled by EUH- FORIA’s adaptation of the WSA. The coverage is below 60% regardless of the selected pair of heights considered for running EUHFORIA. Another patchy CH, but signicantly less patchy than that on 2013-03-27, is the CH on 2016-12-20. This CH is a bit better modelled when lower values of the pair of heights are considered, but the coverage re- mained below 70%. Reconstruction of these strongly (2013-03-27) and moderately (2016- 12-20) patchy CHs suggest that the model might have diculty in reconstructing patchy CHs. It will be interesting for this to be investigated further by considering a larger sam- ple of patchy CHs. Also, it will be interesting to assess possible impact in modelling high speed streams originating from these CHs.

Even though, there is a clear indication that a pair of lower heights will result in a signicantly improved coverage for all CHs not a single pair could be specied as the ideal one. In addition, lowering the two heights results in opening more ux to the he- liosphere, not only within the CH areas, but also outside. This is illustrated in Figure 6 where the modelled CH area extends beyond the EUV dened boundaries. This fea- ture is present in all CH cases and rises the question of how low one can place the two heights, [*R*i, *R*ss], in order to best model the coronal hole area, but without overestimat- ing the open ux outside the EUV dened CH boundaries. To answer that question we consider pixels of open ux that lie outside the EUV dened CH boundaries but have the same polarity as the CH and are connected to the open ux pixels enclosed by the EUV dened CH boundaries, i.e., neighbouring pixels. To identify these areas, we ap- ply the region growth method by selecting seed pixels within the CH area that are as- signed as open eld. We calculated the total number of connected open ux pixels, *N*total, and divided them to those that lie within the boundaries, *N*in, and those that lie out- side, *N*out. From these we dene the percentage of connected area within the boundary, *CA*inwhich is given by:

<u>Nin</u> *CAin*= 100[%] (2) *Ntotal*

In Figure 8 we plot this parameter as a function of the coverage. We can see that for the majority of the CHs both parameters at rst increase but then the system reaches a point where the percentage of connected area that lies within the boundaries starts de- creasing. This implies that, although, open ux pixels grow the majority lies outside the EUV dened boundaries. If ux was opening only inside the boundaries then the curves would be approximately linear. This does not happen though and a saturation point is reached from which further decreasing of the two heights opens more ux outside the boundaries than inside. Following the standard paradigm that the primary source of open ux are CH areas we can conclude that too low heights lead to nonphysical results due to cutting actually closed loops. This is an important nding since it limits how low the two heights can be. From the same gure one can notice that for some CHs there is a double saturation limit.

These saturation limits identied in Figure 8 can be used in order to constrain the possible pairs of boundary heights to those that provide an improved result both in cov-

{14{

80 2012-01-13 80 2012-06-03 100 2012-06-09 [2.8, 2.9] 60 70 75 [2.7, 2.8] [2.6, 2.7] 40 60 50 [2.5, 2.6] 20 25 50 [2.4, 2.5] 0 0 0 10 20 30 60 70 80 90 20 40 60 80 100 2013-01-23 55 2013-03-27 80 2013-05-23 [2.3, 2.4]

60 50 60 [2.2, 2.3]

40 45 40 [2.1, 2.2] 40 20 20 65 70 75 18 20 22 24 26 30 35 40 45 [2.0, 2.1] dii a 80 2013-05-29 60 2013-12-12 2014-01-18 rr a 60 [1.9, 2.0] sol 60 50 in 40 40 ts 40 eigh coverage(%) 30 20 [1.8, 1.9] h] *ss* 20

2077.5 *R*
25 30 35 80.0 82.5 85.0 87.5 30 40 50 *R*, *i* 90 [1.7, 1.8] [ 2014-03-06 80 2014-06-24 2014-07-24 80 60 80 60 [1.6, 1.7] 40 70 40 20 0 60

20.0 22.5 25.0 27.5 0 20 40 60 80 6 8 10 [1.5, 1.6]
2016-12-20 2016-12-28 90 2017-01-03 60 60

40 80 [1.4, 1.5] 40 20 20 70 0 40 50 60 0 25 50 75 57.5 60.0 62.5 65.0 67.5 [1.3, 1.4] percentage of connected area within boundary

Figure 8. Each panel depicts how, for a particular CH, coverage and *CA*in change when EU-

HFORIA runs are set up based on dierent pair of heights [*R*i, *R*ss]. For most CHs a saturation limit is reached beyond which the amount of open ux pixels lying inside the expected from EUV observations area is signicantly lower than those lying outside.

erage and *CA*in. We dene two criteria with the rst being that the coverage parame- ter needs to be above 60% and the second is that *CA*inshould lay no less than 5% from the saturation limit. Although, for most CHs the coverage is above 70%, for four of them (i.e. 2013-03-27, 2013-12-12, 2016-12-20 and 2016-12-28) the maximum coverage is well below that value, which is the reason for this 60% limit. Especially for the CH on 2013- 03-27 the coverage parameter is below 55%, thus, a special limit of minimum 50% cov- erage is applied. For 8 out of the 15 CHs the value of *CA*inis below 50%. To this we in- clude the CH on 2012-06-09 for which the high values of *CA*inare only for when the cov- erage is below 10% which indicates that the number of open ux pixels is extremely low. A *CA*in*<* 50% is the result of having more open ux lying outside the CH area dened by the EUV boundaries for all the model runs performed. For some of the CH a secondary saturation limit can be identied less than 10% from the rst one, which, however, re-

{15{

sults in better coverage without aecting greatly *CA*in. For those cases we do consider the second saturation limit for the *CA*inin investigating the optimal [*R*i, *R*ss] pair. Af- ter analysing the results for each CH we collected the pairs of heights that justify the criteria posed. The table is presented in Figure 9. The colour map indicate the number of CHs for which the pair tted the criteria. Although, all the height pairs fulll the cri- teria for at least one CH, some appear as good candidates more frequently. As can be seen in the table low heights of the SCS model inner boundary (below 1.5*R*) are bet- ter options for successfully reconstructing CH areas (*cov >* 60%), while the selection of the source surface height varies more strongly. Although, for the CH sample studied here these heights gave better results in terms of the coverage, it is important to high- light that there still can be open ux growth outside the expected from observations CH areas. So the use of the heights need to be done with caution.

Figure 9. Collective table of all 184 pair of heights for which the model was tested. The

colour in each shell indicates that this pair of heights produced good results both in coverage and *CA*in for a certain number of CHs, as indicated in the colour map. The most successful pairs of heights, i.e., the ones that were successful for more CHs are collected on the top left corner of the table where lower height values can be found.

### 4 Conclusion and Discussion

As already discussed in other works (e.g., Arden et al., 2014; Linker et al., 2017; Wallace et al., 2019) discrepancies exist between in situ measured at 1AU and model com- puted open ux using the PFSS model, and subsequently the WSA model. Consider- ing the standard paradigm that CHs are primary sources of open ux (Mackay & Yeates, 2012; Linker et al., 2017), testing whether CHs are properly modelled is a logical step. Linker et al. (2017) highlighted the importance for the model output to match CHs ob- served in EUV emission. They used automatically detected CHs to quantitatively make

{16{

comparisons between the PFSS model output and CHs areas. Earlier, Lowder et al. (2014) thoroughly computed open ux based on automatically detected CHs and compared the result to the PFSS estimations. For the period Linker et al. (2017) investigated, plac- ing the source surface height at 2.5*R*ssresulted in signicantly underestimated open eld area and ux. They also concluded that lowering the source surface, although improved the open ux value, it overestimates the areas of open ux.

In this work we presented a collective study assessing the capability of the PFSS+SCS part of the adopted WSA model by EUHFORIA forecasting tool in modelling CH ar- eas. Although, values between 1.6 to 3.25 solar radii are considered allowed for the source surface height, a commonly used value is 2.5*R* (e.g., Arge & Pizzo, 2000; Riley et al., 2015; Wallace et al., 2019). On the other hand, McGregor et al. (2008) concluded that for the modied WSA model which they presented, and which is also adopted in EU- HFORIA, the optimal heights of the source surface and the SCS model inner boundary are [2.3, 2.6]*R*, which we considered as the default pair of heights. Other studies sug- gested an even lower or higher source surface height (Phillips et al., 1994; Lee et al., 2011) or even a solar cycle varying source surface (Arden et al., 2014). We considered 184 pairs of heights aiming to investigate whether the modelled result can be improved. We se- lected 15 CHs having CoM latitude within the central meridional zone of the Sun, and a variety of morphology dened by their elongation, area size, intensity and level of com- pactness. Using EUHFORIA we reconstructed the CH area based on model runs for the 184 pairs. The modelled areas were compared to those derived with catch using EUV imaging observations.

Our main result is that the default heights employed so far, [2.3, 2.6]*R*, fail to model the expected CH areas and/or their locations, with coverage below 60%. This suggests that CH areas are not properly modelled using the default setup. This might provide some explanation for the discrepancy between the open ux output by the WSA model and that measured in-situ at Earth (Riley et al., 2015; Linker et al., 2017; Wallace et al.,

2019). In some cases even the whole CH was missed. Our analysis clearly shows that lower heights (*R*ibelow 1.5*R* and *R*ssbelow 2.3*R*) lead to an improved coverage (*cov >* 60%) of the areas dened by the EUV extracted boundaries; however, it strongly results in opening ux outside those boundaries as well, which is opposing the standard paradigm for the sources of open eld. This last point is in agreement with Linker et al. (2017) re- sult, i.e. that lowering the heights lead to overestimating open ux regions. Assuming that the standard paradigm for open ux origin is correct, this raises the question of how low the source surface height can be placed in order to properly model CH areas and at the same time not model excess open ux areas outside the EUV dened boundaries. Considering modelling the solar wind speed at 1AU it will be very interesting to see the eect of the modelled open ux areas outside the EUV dened boundaries can have. Our analysis also shows that it is rather the height of the inner boundary of the SCS model and not of the source surface that has a stronger eect on the modelled result. We also deduced that low values of this boundary lead to better results in terms or CH area re- construction. It is noteworthy that this result is based on analysing a CH sample from only one solar cycle and considers CHs located in the central meridional zone. Increas- ing the size of the sample and also extending it over a larger period of time can poten- tially lead to dierent height selection. Although, following dierent techniques Lowder et al. (2014); Linker et al. (2017); Wallace et al. (2019) over-plotted automatically detected CHs on synoptic magnetic maps but still resulted in underestimated open ux. According to Linker et al. (2017) the re- sult could only be improved by considering areas larger than the detected CHs, leading them to the conclusion that either synoptic maps underestimate the solar magnetic ux or that CHs are not the sole source of open ux. In addition, there are studies that chal- lenge the certainty that the open ux from in-situ measurements should be an exact match to that modelled close to the Sun, arguing that there might be other processes/factors
{17{

aecting it, as suggested for example in Lockwood et al. (2009), where they found that the excess open ux between models and in situ measurements can be explained by kine- matic eects of variations of the solar wind speed. Thus, opening the question of whether one to one comparison is a sensible approach.

Lee et al. (2011); Arden et al. (2014) investigated the possibility of a solar cycle varying source surface height and concluded that a lower source surface height during solar minimum periods is required. We investigated this possibility but we identied no solar cycle trends in the success of the model in reconstructing CH areas; however, cap- turing the whole cycle could improve the results. In addition, we investigated a possi- ble latitude dependence; however, the latitudinal position of the CH did not have any eect on the modelled results. These are interesting results which, however, need to be considered with care due to rather small sample size. A more detailed analysis, consid- ering a larger number of CHs, spanning over more than one solar cycle and over all so- lar cycle phases, and having more variety in their latitudinal positions, can potentially lead to a dierent outcome.

An interesting remark is that for the CH on 2014-07-24 a channeling to a polar CH was present regardless of the selected pair of heights. This was also appearing for other CHs in the sample when lower heights were selected for the source surface and the in- ner boundary of the SCS model. The idea of CHs being linked to polar ones via narrow passages in the photosphere has been discussed in e.g., Antiochos et al. (2007, 2011). It will be interesting to investigate this aspect on a larger sample of CHs.

It is necessary to mention that the outcome of this study, and other similar stud- ies before it, is focused on how the two free parameters involved in the PFSS+SCS, and subsequently in the WSA model, can aect the modelled results. Saying that we aim to bring forward that the missing open ux in the model outputs might likewise require ne tuning of the other free parameters involved in the model, an idea also discussed in Wallace et al. (2019). Future work should also focus on improving the statistics and also on dif- ferent aspects of the model outcomes, i.e. CH areas, open ux at Earth, velocity of high speed streams, and current sheet position.

Acknowledgments

E.A. would like to acknowledge the nancial support by the Finnish Academy of Science and Letters via the Postdoc Pool funding. S.G.H. and M.T. acknowledge the support by the FFG/ASAP Program under grant No. 859729 (SWAMI). EUHFORIA is devel- oped as a joint eort between the University of Helsinki and KU Leuven. The valida- tion of solar wind and CME modeling with EUHFORIA is being performed within the BRAIN-be project CCSOM (Constraining CMEs and Shocks by Observations and Mod- elling throughout the inner heliosphere; [http://www.sidc.be/ccsom/](http://www.sidc.be/ccsom/)). References Altschuler, M. D., & Newkirk, G. (1969, September). Magnetic Fields and the Structure of the Solar Corona. I: Methods of Calculating Coronal Fields. *Solar* *Physics*, *9*, 131{149. doi: 10.1007/BF00145734 Antiochos, S. K., DeVore, C. R., Karpen, J. T., & Miki, Z. (2007, December). Struc- ture and Dynamics of the Sun’s Open Magnetic Field. *The Astrophysical Jour-* *nal*, *671*(1), 936. doi: 10.1086/522489 Antiochos, S. K., Miki, Z., Titov, V. S., Lionello, R., & Linker, J. A. (2011, April). A Model for the Sources of the Slow Solar Wind. *The Astrophysical Journal*, *731*(2), 112. doi: 10.1088/0004-637X/731/2/112 Arden, W. M., Norton, A. A., & Sun, X. (2014, March). A "breathing" source surface for cycles 23 and 24. *Journal of Geophysical Research (Space Physics)*,
{18{

*119*(3), 1476. doi: 10.1002/2013JA019464 Arge, C. N., Henney, C. J., Koller, J., Compeau, C. R., Young, S., MacKenzie, D.,... Harvey, J. W. (2010, March). Air Force Data Assimilative Photospheric Flux Transport (ADAPT) Model. *Twelfth International Solar Wind Confer-* *ence*, *1216*, 343{346. doi: 10.1063/1.3395870 Arge, C. N., Hildner, E., Pizzo, V. J., & Harvey, J. W. (2002, October). Two solar cycles of nonincreasing magnetic ux. *Journal of Geophysical Research (Space* *Physics)*, *107*, 1319. doi: 10.1029/2001JA000503 Arge, C. N., & Pizzo, V. J. (2000, May). Improvement in the prediction of solar wind conditions using near-real time solar magnetic eld updates. *Journal of* *Geophysical Research*, *105*, 10465{10480. doi: 10.1029/1999JA000262 Asvestari, E., Heinemann, S. G., Temmer, M., Pomoell, J., Kilpua, E., Magdalenic,

J., & Poedts, S. (submitted). The impact of coronal hole characteristics and solar cycle activity in reconstructing coronal holes with euhforia. *10th Young* *Researchers Meeting*.
Gressl, C., Veronig, A. M., Temmer, M., Odstril, D., Linker, J. A., Miki, Z., & Riley,

P. (2014, May). Comparative Study of MHD Modeling of the Background Solar Wind. *Solar Physics*, *289*(5), 1783. doi: 10.1007/s11207-013-0421-6
Heinemann, S. G., Temmer, M., Heinemann, N., Dissauer, K., Samara, E., Jercic,

V., Hofmeister, S.,... Veronig, A. M. (2019, Jul). Coronal Hole Sta- tistical Analysis and Catalogue covering the SDO-era. *arXiv e-prints*, arXiv:1907.01990.
Hickmann, K. S., Godinez, H. C., Henney, C. J., & Arge, C. N. (2015, April). Data Assimilation in the ADAPT Photospheric Flux Transport Model. *Solar* *Physics*, *290*, 1105{1118. doi: 10.1007/s11207-015-0666-3 Hinterreiter, J., Magdalenic, J., Temmer, M., Verbeke, C., Jerabaj, I. C., Samara,

E.,... Isavnin, A. (to be submitted). Testing the background solar wind modelled by euhforia. *Solar Physics*.
Hoeksema, J. T., & Scherrer, P. H. (1986, May). An atlas of photospheric mag- netic eld observations and computed coronal magnetic elds: 1976-1985. *So-* *lar Physics*, *105*, 205{211. doi: 10.1007/BF00156388 Hoeksema, J. T., Wilcox, J. M., & Scherrer, P. H. (1982, December). Structure of the heliospheric current sheet in the early portion of sunspot cycle 21. *Journal* *of Geophysical Research*, *87*, 10331{10338. doi: 10.1029/JA087iA12p10331 Hoeksema, J. T., Wilcox, J. M., & Scherrer, P. H. (1983, December). The structure of the heliospheric current sheet - 1978-1982. *Journal of Geophysical Research*, *88*, 9910{9918. doi: 10.1029/JA088iA12p09910 Hofmeister, S. J., Veronig, A., Temmer, M., Vennerstrom, S., Heber, B., & Vr- nak, B. (2018, March). The Dependence of the Peak Velocity of High- Speed Solar Wind Streams as Measured in the Ecliptic by ACE and the STEREO satellites on the Area and Co-latitude of Their Solar Source Coronal Holes. *Journal of Geophysical Research (Space Physics)*, *123*(3), 1738. doi:

10.1002/2017JA024586
Jian, L. K., Russell, C. T., Luhmann, J. G., MacNeice, P. J., Odstrcil, D., Riley,

P.,... Steinberg, J. T. (2011, October). Comparison of Observations at ACE and Ulysses with Enlil Model Results: Stream Interaction Regions During Carrington Rotations 2016 - 2018. *Solar Physics*, *273*(1), 179. doi:
10.1007/s11207-011-9858-7
Lee, C. O., Luhmann, J. G., Hoeksema, J. T., Sun, X., Arge, C. N., & de Pa- ter, I. (2011, April). Coronal Field Opens at Lower Height During the Solar Cycles 22 and 23 Minimum Periods: IMF Comparison Suggests the

Source Surface Should Be Lowered. *Solar Physics*, *269*, 367{388. doi:

10.1007/s11207-010-9699-9
Lee, C. O., Luhmann, J. G., Odstrcil, D., MacNeice, P. J., de Pater, I., Riley, P., & Arge, C. N. (2009, January). The Solar Wind at 1 AU During the Declining

{19{

Phase of Solar Cycle 23: Comparison of 3d Numerical Model Results with Observations. *Solar Physics*, *254*(1), 155. doi: 10.1007/s11207-008-9280-y Lemen, J. R., Title, A. M., Akin, D. J., Boerner, P. F., Chou, C., Drake, J. F.,... Waltham, N. (2012, January). The Atmospheric Imaging Assembly (AIA) on the Solar Dynamics Observatory (SDO). *Solar Physics*, *275*, 17{40. doi:

10.1007/s11207-011-9776-8
Levine, R. H., Altschuler, M. D., & Harvey, J. W. (1977, March). Solar sources of the interplanetary magnetic eld and solar wind. *Journal of Geophysical Re-* *search*, *82*, 1061{1065. doi: 10.1029/JA082i007p01061 Li, F. Y., Xiang, N. B., Xie, J. L., & Xu, J. C. (2019, March). The Present Spe- cial Solar Cycle 24: Casting a Shadow over Periodicity of the North-South Hemispherical Asymmetry. *The Astrophysical Journal*, *873*(2), 121. doi:

10.3847/1538-4357/ab06bf
Linker, J. A., Caplan, R. M., Downs, C., Riley, P., Mikic, Z., Lionello, R.,... Owens, M. J. (2017, October). The Open Flux Problem. *The Astrophysi-* *cal Journal*, *848*, 70. doi: 10.3847/1538-4357/aa8a70 Lockwood, M., Owens, M., & Rouillard, A. P. (2009, November). Excess open solar magnetic ux from satellite data: 2. A survey of kinematic eects. *Journal of Geophysical Research (Space Physics)*, *114*(A11), A11104. doi:

10.1029/2009JA014450
Lowder, C., Qiu, J., Leamon, R., & Liu, Y. (2014, March). Measurements of EUV Coronal Holes and Open Magnetic Flux. *The Astrophysical Journal*, *783*(2),

142. doi: 10.1088/0004-637X/783/2/142
Mackay, D. H., & Yeates, A. R. (2012, November). The Sun’s Global Photospheric and Coronal Magnetic Fields: Observations and Models. *Living Reviews in So-* *lar Physics*, *9*(1), 6. doi: 10.12942/lrsp-2012-6 MacNeice, P., Jian, L. K., Antiochos, S. K., Arge, C. N., Bussy-Virat, C. D., DeRosa, M. L.,... Sokolov, I. (2018, November). Assessing the Quality of Models of the Ambient Solar Wind. *Space Weather*, *16*, 1644{1667. doi:

10.1029/2018SW002040
McGregor, S. L., Hughes, W. J., Arge, C. N., & Owens, M. J. (2008, August). Analysis of the magnetic eld discontinuity at the potential eld source surface and Schatten Current Sheet interface in the Wang-Sheeley-Arge model. *Journal of Geophysical Research (Space Physics)*, *113*, A08112. doi:

10.1029/2007JA012330
Nolte, J. T., Krieger, A. S., Timothy, A. F., Gold, R. E., Roelof, E. C., Vaiana, G.,... McIntosh, P. S. (1976, February). Coronal holes as sources of solar wind. *Solar Physics*, *46*(2), 303. doi: 10.1007/BF00149859 Owens, M. J., Spence, H. E., McGregor, S., Hughes, W. J., Quinn, J. M., Arge,

C. N.,... Odstrcil, D. (2008, August). Metrics for solar wind predic- tion models: Comparison of empirical, hybrid, and physics-based schemes with 8 years of L1 observations. *Space Weather*, *6*(8), S08001. doi:
10.1029/2007SW000380
Pesnell, W. D., Thompson, B. J., & Chamberlin, P. C. (2012, January). The Solar Dynamics Observatory (SDO). *Solar Physics*, *275*(1-2), 3. doi: 10.1007/s11207 -011-9841-3 Phillips, J. L., Balogh, A., Bame, S. J., Goldstein, B. E., Gosling, J. T., Hoeksema,

J. T.,... Wang, Y.-M. (1994, June). Ulysses at 50 south: constant immersion in the high-speed solar wind. *Geophysical Research Letters*, *21*(12), 1105. doi:
10.1029/94GL01065
Pomoell, J., & Poedts, S. (2018, June). EUHFORIA: European heliospheric forecast- ing information asset. *Journal of Space Weather and Space Climate*, *8*, A35. doi: 10.1051/swsc/2018020 Riley, P., Linker, J. A., & Arge, C. N. (2015, March). On the role played by mag- netic expansion factor in the prediction of solar wind speed. *Space Weather*,

{20{

*13*, 154{169. doi: 10.1002/2014SW001144 Riley, P., Linker, J. A., Miki, Z., Lionello, R., Ledvina, S. A., & Luhmann, J. G. (2006, December). A Comparison between Global Solar Magnetohydrodynamic and Potential Field Source Surface Model Results. *The Astrophysical Journal*, *653*, 1510{1516. doi: 10.1086/508565 Rotter, T., Veronig, A. M., Temmer, M., & Vrnak, B. (2012, December). Relation Between Coronal Hole Areas on the Sun and the Solar Wind Parameters at 1 AU. *Solar Physics*, *281*(2), 793. doi: 10.1007/s11207-012-0101-y Schatten, K. H. (1971). Current sheet magnetic model for the solar corona. *Cos-* *mic Electrodynamics*, *2*, 232{245. Retrieved 2019-05-09, from [http://adsabs](http://adsabs) .harvard.edu/abs/1971CosEl...2..232S Schatten, K. H., Wilcox, J. M., & Ness, N. F. (1969, March). A model of interplan- etary and coronal magnetic elds. *Solar Physics*, *6*, 442{455. doi: 10.1007/ BF00146478 Schulz, M. (1997, November). Non-spherical source-surface model of the heliosphere: a scalar formulation. *Annales Geophysicae*, *15*, 1379{1387. doi: 10.1007/ s00585-997-1379-1 Schulz, M. (2008, May). Non-Spherical Source-Surface Model of the Corona and He- liosphere for a Quadrupolar Main Field of the Sun. *AGU Spring Meeting Ab-* *stracts*, *44*, SH44A{04. Schwenn, R. (2006a, June). Solar Wind Sources and Their Variations Over the Solar Cycle. *Space Science Reviews*, *124*(1-4), 51. doi: 10.1007/s11214-006-9099-5 Schwenn, R. (2006b, August). Space Weather: The Solar Perspective. *Living Re-* *views in Solar Physics*, *3*(1), 2. doi: 10.12942/lrsp-2006-2 Vrnak, B., Temmer, M., & Veronig, A. M. (2007, February). Coronal Holes and So- lar Wind High-Speed Streams: I. Forecasting the Solar Wind Parameters. *So-* *lar Physics*, *240*(2), 315. doi: 10.1007/s11207-007-0285-8 Wallace, S., Arge, C. N., Pattichis, M., Hock-Mysliwiec, R. A., & Henney, C. J. (2019, February). Estimating Total Open Heliospheric Magnetic Flux. *Solar* *Physics*, *294*, 19. doi: 10.1007/s11207-019-1402-1 Wang, Y.-M. (2009, April). Coronal Holes and Open Magnetic Flux. *Space Science* *Reviews*, *144*(1-4), 383. doi: 10.1007/s11214-008-9434-0 Wang, Y.-M., Hawley, S. H., & Sheeley, N. R., Jr. (1996, January). The Magnetic Nature of Coronal Holes. *Science*, *271*, 464{469. doi: 10.1126/science.271.5248

.464
Wang, Y.-M., & Sheeley, N. R., Jr. (1990, June). Solar wind speed and coronal ux- tube expansion. *The Astrophysical Journal*, *355*. doi: 10.1086/168805 Wang, Y.-M., & Sheeley, N. R., Jr. (1992, June). On potential eld models of the so- lar corona. *The Astrophysical Journal*, *392*, 310{319. doi: 10.1086/171430 Wang, Y.-M., & Sheeley, N. R., Jr. (1995, July). Solar Implications of ULYSSES Interplanetary Field Measurements. *The Astrophysical Journal Letters*, *447*, L143. doi: 10.1086/309578 Wang, Y.-M., & Sheeley, N. R., Jr. (2003, December). On the Topological Evolution of the Coronal Magnetic Field During the Solar Cycle. *The Astrophysical Jour-* *nal*, *599*, 1404{1417. doi: 10.1086/379348

{21{
