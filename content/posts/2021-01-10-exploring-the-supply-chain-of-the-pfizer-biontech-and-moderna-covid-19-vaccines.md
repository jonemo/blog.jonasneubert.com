---
date: "2021-01-10T00:00:00Z"
published: true
tags:
- vaccines
title: Exploring the Supply Chain of the Pfizer/BioNTech and Moderna COVID-19 vaccines
---

_Sections of this post were co-authored by [Cornelia Scheitz](https://www.linkedin.com/in/cornelia-scheitz/)._
_Noah Leidinger created a [German translation](https://www.noahleidinger.com/unlisted/covid19)._
_Piotr Kwapin created a [Polish translation](https://wpunkt.org/analiza-lancucha-dostaw-szczepionek-pfizer-biontech-i-moderna-przeciwko-covid-19/)._
_Last updated on February 7, 2021._

Bert Hubert’s excellent and widely shared article about [Reverse Engineering the source code of the Pfizer-BioNTech SARS-CoV-2 Vaccine](https://berthub.eu/articles/posts/reverse-engineering-source-code-of-the-biontech-pfizer-vaccine/) is all it took to turn hundreds of software engineers and other Silicon Valley types into armchair vaccine experts overnight! Jokes aside, the article explains the 4284 base long mRNA inside the Pfizer-BioNTech’s COVID-19 vaccine for those who are more familiar with software than molecular biology.

Bert’s article is primarily about the biology of the vaccine, how it relates to the virus and how it works in the human body, but there’s this one sentence about vaccine production:

> At the very beginning of the vaccine production process, someone uploaded this code to a DNA printer (yes), which then converted the bytes on disk to actual DNA molecules.

Next to it is a picture of a [CodexDNA BioXP](https://codexdna.com/products/bioxp-system/) device that is advertised as producing “custom DNA fragments of up to 7,000 base pairs”. Could this be the next [distributed manufacturing revolution](https://en.wikipedia.org/wiki/Makers:_The_New_Industrial_Revolution)? This time with DNA printers making COVID-19 vaccines in our garages instead of 3D printers and plastic widgets?

I'll start with the bad news: Nobody will be making an mRNA vaccine in their garage any time soon.

The following text is a collection of notes I wrote down while exploring the process for manufacturing and distributing the two new vaccines that have appeared all over the news and in more and more people’s arms over the recent weeks. I started reading about mRNA but quickly found myself on tangents about glass vials and temperature tracking devices.

This text was written over a week worth of evenings in early January 2021. It covers the two vaccines authorized for distribution in the United States at the time of writing: One by Pfizer-BioNTech and one by Moderna. Several other mRNA-based COVID-19 vaccines [are in various stages of clinical trials](https://www.nytimes.com/interactive/2020/science/coronavirus-vaccine-tracker.html) and are likely similar to those covered here in some ways and different in others.

It is unlikely that I got everything right. Corrections and suggestions are welcome, please email jn@jonasneubert.com.

{{< figure
  src="/assets/2021/2021-01-10-moderna-vaccine-in-fridge.jpg"
  title="Source/attribution: U.S. Navy Photo by Elaine Heirigs, NHC/NMRTC Lemoore public affairs/Released, https://www.flickr.com/photos/navymedicine/50755819886/"
>}}


## Ingredients List

The list of ingredients, or “bill of materials” in engineering parlance, is a good starting point for understanding the supply chain of any product. The ingredient lists for both Pfizer-BioNTech and Moderna’s vaccines are public and have been widely reported.

The Pfizer-BioNTech vaccine is also known under its code name “BNT162b2”, its registered trademark “Comirnaty”, and its international non-proprietary name “Tozinameran”. The list of ingredients can be found in information material available on the various country-specific product websites on [www.cvdvaccine.com](https://www.cvdvaccine.com) or government websites like that of the [UK’s MHRA](https://www.gov.uk/government/publications/regulatory-approval-of-pfizer-biontech-vaccine-for-covid-19/information-for-healthcare-professionals-on-pfizerbiontech-covid-19-vaccine). There’s also a [Wikipedia page](https://en.wikipedia.org/wiki/Tozinameran#Manufacturing).

The Moderna vaccine is also known as “mRNA-1273”, but appears to lack a brand name other than “Moderna COVID-19 Vaccine” which is what it says on the product label. The list of ingredients can be found on the [EUA factsheet on Moderna’s website](https://www.modernatx.com/covid19vaccine-eua/), or in these [FDA meeting notes](https://www.fda.gov/media/144434/download ). It, too, has a [Wikipedia entry](https://en.wikipedia.org/wiki/MRNA-1273).

The two vaccines share some ingredients but not all. The following table is my attempt to sort the available information and compare the two.


<table>
  <tr>
   <td>
   </td>
   <td>Pfizer-BioNTech
   </td>
   <td>Moderna
   </td>
  </tr>
  <tr>
   <td colspan="3" ><strong><span style="text-decoration:underline;">Active Ingredient</span></strong>
   </td>
  </tr>
  <tr>
   <td>Comirnaty mRNA
   </td>
   <td>✔
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>mRNA-1273 mRNA
   </td>
   <td>
   </td>
   <td>✔
   </td>
  </tr>
  <tr>
   <td colspan="3" ><strong><span style="text-decoration:underline;">Lipids</span></strong>
   </td>
  </tr>
  <tr>
   <td>Cholesterol
   </td>
   <td>✔
   </td>
   <td>✔
   </td>
  </tr>
  <tr>
   <td>1,2-distearoyl-sn-glycero-3-phosphocholine (DSPC)
   </td>
   <td>✔
   </td>
   <td>✔
   </td>
  </tr>
  <tr>
   <td>((4-hydroxybutyl)azanediyl)bis(hexane-6,1-diyl)bis(2- hexyldecanoate) (ALC-3015)
   </td>
   <td>✔
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>2-[(polyethylene glycol)-2000]-N,N-ditetradecylacetamide (ALC-0159)
   </td>
   <td>✔
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>Lipid SM-102
   </td>
   <td>
   </td>
   <td>✔
   </td>
  </tr>
  <tr>
   <td>1,2-dimyristoyl-rac-glycero-3-methoxypolyethylene glycol-2000 (PEG2000-DMG)
   </td>
   <td>
   </td>
   <td>✔
   </td>
  </tr>
  <tr>
   <td colspan="3" ><strong><span style="text-decoration:underline;">Buffer</span></strong>
   </td>
  </tr>
  <tr>
   <td>potassium chloride
   </td>
   <td>✔
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>monobasic potassium phosphate
   </td>
   <td>✔
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>sodium chloride
   </td>
   <td>✔
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>dibasic sodium phosphate dihydrate
   </td>
   <td>✔
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>tromethamine (tris(hydroxymethyl)aminomethane)
   </td>
   <td>
   </td>
   <td>✔
   </td>
  </tr>
  <tr>
   <td>tromethamine hydrochloride
   </td>
   <td>
   </td>
   <td>✔
   </td>
  </tr>
  <tr>
   <td>acetic acid
   </td>
   <td>
   </td>
   <td>✔
   </td>
  </tr>
  <tr>
   <td>sodium acetate
   </td>
   <td>
   </td>
   <td>✔
   </td>
  </tr>
  <tr>
   <td>water
   </td>
   <td>✔
   </td>
   <td>✔
   </td>
  </tr>
  <tr>
   <td colspan="3" ><strong><span style="text-decoration:underline;">Other</span></strong>
   </td>
  </tr>
  <tr>
   <td>sucrose
   </td>
   <td>✔
   </td>
   <td>✔
   </td>
  </tr>
</table>


In addition to what’s in the vaccine vial, Pfizer-BioNTech needs to be diluted with sodium chloride solution shortly before use (more about that below). The Moderna vaccine does not require such a “DIY assembly” step.

Now that we know all the ingredients, let’s go shopping.

Disclaimer: Please don’t perform chemistry or create pharmaceuticals unless you have the appropriate safety training and equipment. I include links to online shops below, but note that they sell “for research use only” and will verify your affiliation with a research organization before taking your business.


## mRNA

To make RNA, you start by making DNA. This makes sense if you know the [central dogma of molecular biology](https://en.wikipedia.org/wiki/Central_dogma_of_molecular_biology) which, for the purposes of this article, can be simplified to “DNA makes RNA, RNA makes protein”.  Making DNA is a known, stable process in 3 steps:

**Step 1: Create.** Synthesize a small number of copies of the desired DNA, somehow. There are vendors for this sort of thing, for example [Twist Bioscience](https://twistbioscience.com/) just down the street from my apartment when I lived in San Francisco and [Integrated DNA Technologies](https://www.idtdna.com) in Coralville, Iowa.

**Step 2: Copy.**



1. Surround this DNA into a [cloning vector](https://en.wikipedia.org/wiki/Cloning_vector) DNA fragment and insert the result into innocent [E. coli bacteria](https://en.wikipedia.org/wiki/Escherichia_coli) by means of [electroporation](https://en.wikipedia.org/wiki/Electroporation), i.e. zapping them. E. coli is a tiny organism that comes with all machinery necessary for creating copies of a given sequence of DNA.
2. Put those bacteria into a stainless steel growth chamber full of nutrients and let them multiply for four days.
3. Drain the vat, kill the bacteria, and [extract the DNA](https://en.wikipedia.org/wiki/DNA_extraction). Depending on growth chamber volume, steps 2.1 to 2.3 may take one week or longer.

**Step 3: Verify.** Perform several tests to confirm that the DNA you got is the DNA you wanted. There’s no need for me to explain how testing for the presence of specific DNA sequences works, y’all learned that nine months ago when you did your reading about how COVID-19 tests work.

This yields grams of DNA and what is needed are bags of mRNA. mRNA is the most discussed ingredient of the vaccine for three reasons:



1. mRNA is the active ingredient of the vaccine.
2. It is the first time an mRNA vaccine has been approved and is now produced at scale.
3. The skills to produce mRNA at scale and the associated supply chain are new.[^1]
The conversion process from DNA to mRNA in living cells is well understood. However, performing it in a factory and at scale and resulting in RNA with a long shelf life is still an area of development. The DNA gets combined with



* [nucleotides](https://en.wikipedia.org/wiki/Nucleotide), the raw building blocks for the mRNA,
* RNA [polymerase](https://en.wikipedia.org/wiki/Polymerase), the enzyme that read DNA and transcribe it to mRNA,
* and enzymes that protect the mRNA (see below).[^2]
As Bert points out in [his article](https://berthub.eu/articles/posts/reverse-engineering-source-code-of-the-biontech-pfizer-vaccine/ ), to ensure the immune system does not attack the foreign mRNA, every [uracil](https://en.wikipedia.org/wiki/Uracil) (the letter U in the RNA sequence) is replaced by 1-methyl-3’-pseudouridylyl (canonical name is N1-Methylpseudouridine). Note that pseudouridylyl is phonetically similar to the more common pseudouridine, but chemically quite different thanks to the addition of a [methyl group](https://en.wikipedia.org/wiki/Methyl_group).[^3] 1-methyl-3’-pseudouridylyl can be purchased from [TriLink](https://www.trilinkbiotech.com/n1-methylpseudouridine-5-triphosphate.html) and [JenaBiosciences](https://www.jenabioscience.com/nucleotides-nucleosides/nucleotides-by-structure/analogs-and-derivatives-of/natural-rna-nucleobases/nu-890-n1-methylpseudo-utp), for example, but both BioNTech and Moderna likely license the molecule from the University of Pennsylvania[^4] and produce it themselves.

The pseudouridylyl replacement is a neat little trick to fly under the radar of the immune system. However, more work is needed to make the mRNA work as a vaccine. mRNA is not very stable, and is especially prone to damage at the ends. If you lose the first and last word of a sentence its meaning may be lost entirely. The same can happen here and the vaccine would not work anymore.

To protect the “beginning” of the mRNA statement, a [5’ cap](https://en.wikipedia.org/wiki/Five-prime_cap) is added. This can be done co-transcriptionally, in the same process step as when the rest of the mRNA is assembled, or post-transcriptionally, in a separate process step. To do so co-transcriptionally, a 5’ cap [analog](https://en.wikipedia.org/wiki/Functional_analog_(chemistry)) is added to the reaction mixture and incorporated by the polymerase when it reads a specific initiator sequence. There is only one vendor for this analog: [TriLink](https://www.trilinkbiotech.com/cleancap-reagent-ag-3-ome.html) and its partner [tebu-bio](https://www.tebu-bio.com/) for the European market. Post-transcriptionally it can be done using a mRNA cap 2′-O-methyltransferase and the vaccinia capping enzyme (VCE).[^5] The co-transcriptional method is generally more suitable for industrial processes as there is no need for an additional post-purification and it is faster since it works in one step. In their [July 2020 investor update](https://investors.biontech.de/static-files/7b74cd9e-b944-4a87-8d71-97feef5a3f7a) BioNTech refers to usings TriLink’s trinucleotide cap and hence this is likely part of the production method of the approved vaccine. Ultimately, the cap analogue or the VCE can drive cost and present bottlenecks if production is not increased accordingly.[^6]

To protect the end of the mRNA we add a [poly(A) tail](https://en.wikipedia.org/wiki/Polyadenylation) to the message either by encoding it in the DNA template or using a Poly(A)Polymerase. Both [BioNTech](https://biontech.de/how-we-translate/mrna-therapeutics) and Moderna are using the faster and convenient DNA template approach.

All ingredients of the vaccine besides the mRNA are “[excipients](https://en.wikipedia.org/wiki/Excipient)”, substances whose purpose is somehow related to getting the vaccine from the factory into a human cell.


## Lipids

Lipids are fatty molecules. Each of the two vaccines contains four types of lipid: Cholesterol, phosphatidylcholine, an ionizable cationic lipid, and PEGylated phospholipds. In the finished vaccine, the lipids will form a capsule around the mRNA to protect the mRNA from the hostile environment until it arrives inside a human cell. The assembly of mRNA and lipids is called the [lipid nanoparticle](https://en.wikipedia.org/wiki/Solid_lipid_nanoparticle) (LNP), but in this section we focus on where the lipid bulk ingredients come from.

Both Pfizer-BioNTech and Moderna use the same structural components which are already approved in many drugs.



* **DSPC**, full name [Distearoylphosphatidylcholine](https://en.wikipedia.org/wiki/Distearoylphosphatidylcholine) or 1,2-distearoyl-sn-glycero-3-phosphocholine, is a key component of the lipid bilayer that protects the mRNA.
* **Cholesterol** is natural to the human body. In the vaccine it is used to achieve optimal liposome formation and structure.

The other two lipid ingredients will be used to optimize the LNP for its cargo and the delivery[^7] and are novel or uncommon in drug formulation.

**Cationic**, or positively charged, lipids bind to and help stabilize the negatively charged mRNA during assembly. Once inside the cell, the cell’s different pH environment triggers the release of mRNA



* Pfizer-BioNTech uses [ALC-3015](https://en.wikipedia.org/wiki/ALC-0315) patented by Acuitas Therapeutics, Inc.[^8] and it is the most abundant lipid in the mix[^9].


* Moderna has a proprietary molecule called Lipid SM-102. Or maybe it isn’t that proprietary, because it might be covered by a patent owned by Arbutus Biopharma.[^10] Moderna’s [Phase 3 Clinical Study Protocol](https://www.modernatx.com/sites/default/files/mRNA-1273-P301-Protocol.pdf) defines it as “heptadecan-9-yl 8-((2-hydroxyethyl) (6-oxo-6-(undecyloxy)hexyl)amino)octanoate” and calls it a “proprietary ionizable lipid.” In 2018, Moderna researchers published [a Cell paper](https://www.cell.com/molecular-therapy-family/molecular-therapy/pdfExtended/S1525-0016(18)30118-7) proposing 10 new lipids, of which SM-102 is number 8, according to [this tweet](https://twitter.com/1stClef/status/1306653592691113986). The paper has a “synthesis” section and supplementary materials which somebody more knowledgeable about such things than I might be able to reproduce. Everyone else will have to purchase it, for example from [Organix Inc at $5,000/100mg](https://organixinc.com/lipids/atx001-crrdc-b9dnh-phs3e) (update: the original link stopped working, [here is a snapshot](https://web.archive.org/web/20210119220956/https://organixinc.com/lipids/atx001-crrdc-b9dnh-phs3e) from January 19, 2021).
**PEGylated phospholipids** help stabilize the LNP and protect it from early detection by our immune system. It ensures the LNP and thus the mRNA can reach its target.



* Pfizer-BioNTech uses [ALC-0159](https://en.wikipedia.org/wiki/ALC-0159).
* Moderna uses DMG-PEG 2000 or “1-monomethoxypolyethyleneglycol-2,3-dimyristylglycerol” with polyethylene glycol with average molecular weight 2000. This can be purchased, for example from [Sigma Aldrich](http://www.sigmaaldrich.com/catalog/product/avanti/880151p).

The formulation of the LNPs is key to the vaccine and efficiency. The specific combination of lipids is most probably what gives the Moderna nanoparticles the ability to protect the mRNA from degradation at higher temperatures (more about temperature requirements below).


## Buffer

Controlling the pH level of the vaccine is important because too high or too low values could destroy the active ingredient. The term “buffer solution” describes a substance that keeps the pH value of a solution (nearly) constant.

**PBS** ([phosphate-buffered saline](https://en.wikipedia.org/wiki/Phosphate-buffered_saline)) is a commonly used buffer that is made of dibasic sodium phosphate dihydrate, potassium chloride, monobasic potassium phosphate, and sodium chloride. Check the ingredients list of Pfizer-BioNTech again and you’ll notice that those are all on there.

The combination of **tromethamine** and **tromethamine hydrochloride**, listed as Moderna ingredients, is more commonly known as “[tris buffer](https://en.wikipedia.org/wiki/Tris#Buffering_features)”. **Sodium acetate** combined with **acetic acid** is [another buffer](https://en.wikipedia.org/wiki/Sodium_acetate#Buffer_solution) and also a Moderna ingredient.

All three types of buffer are very common and return Google Scholar result counts in the hundred thousands or millions. PBS is a general purpose work horse, tris and sodium acetate are a bit more specific for buffering nucleic acids. Supply is abundant and cost negligible compared to the other ingredients. Scientists who need tris buffer in their lab would purchase Tris Base (e.g. from [Sigma Aldrich](https://www.sigmaaldrich.com/catalog/product/roche/trisro?lang=en&region=US&cm_sp=Insite-_-caSrpResults_srpRecs_srpModel_tris*-_-srpRecs3-1)) to mix with water and adjust the pH with HCl[^11]. For larger quantities, you would work with [a contract manufacturer](https://www.biospectra.us/tromethamine-tris).


## Sugar

**Sucrose** is the molecule that makes up table sugar, the stuff made from sugar cane or sugar beets. Its purpose in the vaccine is to protect the other components from sustaining damage during frozen storage. In both vaccines it is by far the biggest non-water component by weight, for example at 87 mg/mL in Moderna’s. I wonder if this means that the vaccine tastes sweet.

Finally, add water and stir. Just kidding, don’t stir: The instructions for Pfizer-BioNTech specify quickly rotating the vial upside down and back ten times as the protocol for mixing. And don’t worry, you won’t destroy the LNP’s by doing that.

Next up, let’s look at how these ingredients come together into the final product at an industrial scale.


## Manufacturing Operations

Both Pfizer-BioNTech and Moderna have two largely independent supply chains in Europe and the United States. This makes sense in order to maximize utilization of available manufacturing capacity and to add resilience through redundancy. [Bloomberg’s Supply Lines newsletter](https://www.bloomberg.com/news/articles/2020-07-25/the-supply-chain-to-save-the-world-is-unprepared-for-a-vaccine) points out that it also appeases certain “protectionist governments intent on hobbling international cooperation by exerting sovereignty over supply chains.” In fact, “America exports virtually nothing out of its borders” (says German chancellor Merkel)[^12] and supply agreements with manufacturers specifically prohibit sending vaccine from Europe to the US, for example Moderna’s contract with Lonza[^13].

Following the active ingredient from beginning (DNA synthesis) to end (fill-and-finish into vials) takes on the order of weeks. For example, Moderna’s first ever batch of the COVID-19 vaccine was sent off to the National Institutes of Health (NIH) for phase 1 clinical trials 42 days after the design of the vaccine was completed.[^14] (The final 14 of those 42 days were spent waiting for the fixed-length sterility test experiment to complete.) On February 7, 2021, USA Today reported that Pfizer plans to cut the average start-to-finish time for a batch from 110 days to 60 days.[^15]

A note about the relationship between BioNTech and Pfizer: BioNTech is the original developer of several COVID-19 vaccine candidates. In March 2020, BioNTech announced a collaboration with Pfizer that involves jointly pursuing clinical trials for the candidates, development of the final vaccine, and all other remaining steps towards global distribution including manufacturing, distribution, finances, and marketing.[^16] Pfizer owns marketing and distribution rights for all but three countries in the world.[^17] Those three exceptions are: Germany and Turkey where BioNTech themselves markets and distributes, and China where [Shanghai Fosun Pharma](https://en.wikipedia.org/wiki/Fosun_Pharma) holds the marketing rights.[^18] Pfizer and BioNTech share gross profits generated outside of China 50:50.[^19]

Fun fact: BioNTech’s headquarter’s street address is “An der Goldgrube 12” which literally translates to “At the Goldmine 12”.

The following sections step through the production process step-by-step. Note that Moderna performs the steps from DNA production, RNA production, and LNP assembly under the same roof at all its locations while Pfizer performs the steps at places that are geographically quite distributed.


## DNA Production

Pfizer’s US supply chain starts in St Louis, MO, where somewhere in their [250k sqft laboratory and manufacturing space](https://www.pfizer.com/science/research-development/centers/mo_st_louis) there are E. coli bacteria hard at work cloning DNA plasmids, following the general process described above. The resulting DNA is “purified through a series of chromatographic and filtration steps.”[^20] [This Washington Post article](https://www.washingtonpost.com/health/2020/11/17/coronavirus-vaccine-manufacturing/) describes Pfizer’s process more prosaically than I ever could and is going to be referenced several times in this section and the next. For each batch, this process takes 16 days, with goals to speed it up to 9 days.[^21]

For each batch, if the quality control passes, the resulting one gram of frozen linearized DNA is shipped to the next facility. This is the transport step for which Pfizer reportedly used the company jet or helicopter at times (according to the [WaPo](https://www.washingtonpost.com/health/2020/11/17/coronavirus-vaccine-manufacturing/) article).

Moderna has operated a “two-storey, football-pitch-sized manufacturing plant” in Norwood, Massachusetts, since 2018. This is where, reportedly, the mRNA for all of Moderna’s previous clinical trials of other vaccines has been produced.[^22] Additionally, Moderna works with Swiss contract manufacturing company [Lonza](https://www.lonza.com).[^23] Lonza constructed four identical new production lines between signing the agreement with Moderna in May 2020 and January 2021.[^24] One of these lines is in Portsmouth, New Hampshire, and started production in July. Three were installed in a formerly empty building near Lonza’s headquarters in Visp, Switzerland, and were reported as pending startup [on December 29, 2020](https://new.rro.ch/story/lonza-startet-produktion-von-coronaimpfstoff/12958).

As of January 2021, each Lonza-operated line is forecast to produce 100,000 doses per year, and Moderna’s own Norwood site 200,000 doses.[^25] I would use these (and all other) production forecasts only to compare between sites and assume a large margin of error in absolute terms.

[Moderna’s contract with Lonza](https://www.sec.gov/Archives/edgar/data/1682852/000168285220000023/lonzamodernagltafullye.htm) specifies that vaccine doses produced at the Visp site in Switzerland or anywhere else outside the United States will never be shipped to the United States.


## mRNA Production

In order to turn grams of DNA into, literally, bags of mRNA, the DNA is combined with nucleotides and polymerase, as described in the section about ingredients a few sections ago. In practical terms, this will involve inserting all three components (plus supporting materials such as water) into a [bioreactor](https://en.wikipedia.org/wiki/Bioreactor) where the transcription reaction can happen. Process developers for this step decide which ingredients get added to the bioreactor at what feed rates (and which ones to have in the reactor from the start), details of the agitation (shaking or stirring?) and similar parameters. Traditionally, bioreactors take the form of stainless steel tanks with ports for inlets, outlets, and sensors. [Single-use bioreactors](https://en.wikipedia.org/wiki/Single-use_bioreactor) are getting increasingly popular for benefits such as zero risk of cross-batch contamination. After the reaction has occurred, removal of leftover raw ingredients and purification happens, and then we are left with pure mRNA. This is the finalized, active ingredient–the first item from our ingredients list.

In the case of Pfizer, the DNA from St. Louis is shipped to another Pfizer location in Andover, Massachusetts, or to BioNTech in Germany to be converted to mRNA. The photo in [this February 7 USA Today article](https://www.usatoday.com/story/news/health/2021/02/07/pfizer-expects-cut-covid-19-vaccine-production-time-almost-50/4423251001/) allegedly shows “the mRNA production suite” in Andover but leaves some questions including: Would it work better if you plug it in? And where are the multiple “lines” mentioned in the article?

The aforementioned Washington Post article mentions that the resulting mRNA is frozen in bags “the size of a large shopping bag.”[^26] It seems like a reasonable guess that these bags are actually the single-use bioreactors which the mRNA was made in. The French-headquartered company [Sartorius Stedim Biotech](https://www.sartorius.com/en/company/about-sartorius-stedim-biotech-sa) is a supplier of BioNTech[^27] and advertises their [Flexsafe RM Bags](https://www.sartorius.com/en/products/fermentation-bioreactors/single-use-bioreactors/biostat-rm-flexsafe-rm) (available in volumes up to 200 liters) for use in vaccine production, so it’s a reasonable guess that Pfizer’s bags are something along those lines.

The purification and final concentration for BioNTech-produced mRNAs is done by [Rentschler Biopharma](https://www.rentschler-biopharma.com/) in Laupheim, Germany.[^28] Rentschler has a subsidiary in Milford, Massachusetts, but the press release specifically only mentions work for BioNTech in Laupheim and not for Pfizer in Milford. Pfizer and Lonza may perform both steps in-house (in Andover, Portsmouth, and Visp) or maybe I just didn’t find announcements about their respective partnerships.

mRNA production has never been done at the volume required for the COVID-19 vaccines. As a result, it is considered risky from a supply chain perspective. On the materials side, some of the enzymes needed to cap the mRNA have limited availability.[^29] On the infrastructure side, until a few months ago the specialized facilities and workers required only handled small research workloads.[^30]


## Lipids Production

Pfizer sources all four lipids from UK-headquartered [Croda International](https://www.croda.com). The [news release](https://www.croda.com/en-gb/news/2020/11/pfizer-croda) implies that the recently acquired subsidiary [Avanti Polar Lipids](https://avantilipids.com), located in Alabaster, Alabama, would handle the production. All lipids for the Pfizer/BioNTech production come from the US[^31], whether they all come from Alabama is not clear to me.

Moderna sources all lipids from the German-headquartered company [CordenPharma](https://www.cordenpharma.com).[^32] One facility in Boulder, Colorado, which was recently expanded and can now produce 400kg per batch[^33], and two facilities in [Liestal, Switzerland](https://www.cordenpharma.com/facilities/liestal/), and [Chenôve, France](https://www.cordenpharma.com/facilities/chenove/), are set up to produce the lipids required by Moderna.


## Lipid Nanoparticle (LNP) Assembly

Welcome to the bottleneck of mRNA vaccine production! This is where the mRNA and lipids (see previous sections) get combined. The number of people in the world who know how to get lipids and mRNA to combine into a lipid nanoparticle (LNP) might be in the low hundreds. And the machines to do it might not be machines at all but one-off lab bench setups like the one in this [Wall Street Journal article](https://www.wsj.com/articles/if-one-leading-coronavirus-vaccine-works-thank-this-tiny-firm-in-rural-austria-11604664001).

The problem at hand is this: How do you get the four lipids and the mRNA to combine in such a way that they form the protective sphere of the LNP, in a reproducible way? You can’t just combine all parts in your Vitamix and run the smoothie program. Well, you could, but it’s going to give you a weird smoothie and not mRNA-filled lipid nanoparticles. What is of the essence is precise control of molecule sizes, precise control of flow rates, and probably precise control of many other parameters.

[Pfizer’s vaccine infographic](https://pfe-pfizercom-d8-prod.s3.amazonaws.com/Vaccines_Infographic5_July2020.pdf) from July 2020 explains LNP production as a “series of steps including impingement jet mixing and specialized mixing.” The choice of wording for the first type of mixing in that sentence is quite specific and leads to the company [Knauer](https://www.knauer.net) (located in Berlin, Germany, headcount 135) which announced in December 2020 that it expanded its business into impingement jet mixing for liquid nanoparticle production[^34] and is listed by BioNTech as a “COVID-19 vaccine partner.”[^35]

The “specialized mixing” in Pfizer’s fact sheet is most likely some microfluidics technique. This [Youtube video](https://www.youtube.com/watch?v=oNx21jHRTD4) shows a microfluidics-based device for LNP assembly produced by the company [Precision Nanosystems](https://www.precisionnanosystems.com/workflows/payloads/mrna) in Vancouver, Canada. There is no source to suggest that either Pfizer-BioNTech or Moderna use this specific device, but whatever they do use probably looks similar. The educational content on Precision Nanosystems’ website is also worth a watch if you want to know more about the process.

Vancouver, British Columbia, appears to be one center of expertise for LNPs in the world. In addition to the aforementioned Precision Nanotech, Vancouver is also home to Transferra Nanosciences and [Acuitas Therapeutics](https://acuitastx.com). Transferra was acquired by German chemistry mega-corp [Evonik](https://en.wikipedia.org/wiki/Evonik_Industries)[^36] in 2016 but seems to not be involved in any COVID-19 vaccine efforts. Acuitas, on the other hand, is one of the two companies credited with developing the LNP (and its assembly process) for the Pfizer-BioNTech vaccine.[^37] No mRNA is shipped to Vancouver, however; the process happens in-house at Pfizer’s and BioNTech’s sites. [The previously referenced Washington Post article](https://www.washingtonpost.com/health/2020/11/17/coronavirus-vaccine-manufacturing/) reports that in November 2020 the LNP production step in Kalamazoo was the bottleneck of the US supply chain.

Klosterneuburg outside Vienna, Austria, is the other global center of excellence for LNPs. That’s where the company [Polymun Scientific Immunbiologische Forschung GmbH](https://www.polymun.com) is located which is the subject of the aforementioned WSJ article. According to the article, technology transfer to scale up Polymun’s process in-house at Pfizer and/or BioNTech was happening as of November 2020. Polymun performs the production step of packaging mRNA in LNPs in Austria at least for the doses destined for Germany, and I suspect for all non-US destinations. At the end, they provide 80L of sterile mRNA-LNP mix to the fill-and-finish facility which will use this raw material to create ~1 million doses of vaccine.[^38]

Moderna has an in-house LNP production process[^39] and evidently not much contact with the media as I was not able to uncover any information. Most likely, contract manufacturer Lonza handles this step for Moderna.


## Formulation & Fill-and-finish

The sourcing of the LNPs that contain mRNA and lipids is covered above, the remaining ingredients are generic and abundant enough to not warrant their own section.

The remaining steps in the production of the vaccine itself are “formulation” where LNPs, buffers, and sucrose are combined, and “[fill-and-finish](https://en.wikipedia.org/wiki/Fill_and_finish)”, the pharma industry terminology for the filling into vials, labeling, and packaging. This sounds easy, but keep in mind that at this step of the process we are dealing with lipid nanoparticles that like to be kept frozen, and we all know that frozen liquids don’t mix well.

In the United States, Pfizer performs the final steps only in Kalamazoo, Michigan, where the company has an [80-building campus](https://www.pfizer.com/products/pfizer-global-supply/us-manufacturing-sites/kalamazoo). In Kalamazoo, there are two filling lines, one of which reaches 600 vials per minute. Kalamazoo is also the location of the “freezer farm” where Pfizer stored vaccines that had been produced before the EUA was granted that allowed their distribution.

In Europe, BioNTech and Pfizer operate their own plants and work with a growing number of contract manufacturers and other partners. On February 2nd, BioNTech released [this press release](https://investors.biontech.de/news-releases/news-release-details/statement-manufacturing) referencing 13 manufacturing partners, although it remains unclear how many of those are for the fill-and-finish step of the process. The following partners and locations have been publicly mentioned:



* Pfizer’s plant in Puurs, Belgium, was the first operational fill-and-finish site in Pfizer-BioNTech’s European network.
* BioNTech also has [its own production facilities](https://biontech.de/our-dna/locations) in Mainz and Idar-Oberstein. I found no source to confirm whether fill-and-finish operations are performed there.
* In September 2020 BioNTech acquired an active production facility (including 300 workers) from Novartis in Marburg, Germany, and announced that this would increase annual production by 750 million doses starting in February 2021.[^40]


* [Dermapharm](https://www.dermapharm.de) has a contract to fill-and-finish at its site in Brehna near Leipzig.[^41]


* Swiss company [Siegfried](https://www.siegfried.ch) plans to start production in Hameln, Germany, in mid-2021.[^42]


* The [Halle, Germany, site](https://www.baxterbiopharmasolutions.com/about-us/worldwide-facilities/halle.html) of US-based health care company [Baxter](https://www.baxter.com) has been doing trial runs since December 2020 and is slated to start production on February 5, 2021.[^43]


* On January 26, 2021, Sanofi announced its intention to fill-and-finish Pfizer-BioNTech vaccine at its site in Frankfurt, Germany, starting in August 2021.[^44]


* On January 29, 2021, Novartis announced a not-yet-signed deal with Pfizer-BioNTech which could result in a start of production of to-be-determined quantities in its Stein am Rhein, Switzerland, site in Q2 2021.[^45]
Moderna, having no international megacorp partner like Pfizer, [outsourced these same steps](https://investors.modernatx.com/news-releases/news-release-details/moderna-provides-covid-19-vaccine-supply-update) to contract manufacturer [Catalent](https://www.catalent.com) in the US[^46] and to [Laboratorios Farmacéuticos Rovi](https://rovi.es/en/) in Madrid, Spain, for all non-US demand[^47]. On December 30, 2020, Moderna signed an additional deal with Sweden-headquartered [Recipharm](https://www.recipharm.com) to perform fill-and-finish at Recipharm’s [facility in Monts, France](https://www.recipharm.com/france/monts), starting in “early 2021.”[^48]

Assorted details about the fill-and-finish process: BioNTech contract manufacturers install inspection machines by German manufacturer [Seidenader](https://www.seidenader.de). Catalent has posted short videos of its Moderna fill-and-finish line on Twitter [here](https://twitter.com/CatalentPharma/status/1344693064862937090) and [here](https://twitter.com/CatalentPharma/status/1351960182666846208).


## Packaging

Five 0.3mL doses of the Pfizer-BioNTech vaccine are combined into a single vial. News outlets report that vials are often overfilled and US and EU regulators encourage that extra doses be administered from a vial if possible.[^49][^50] 195 vials are stored on a tray and up to five trays are placed in a custom shipping box (which then holds 4,875 doses).[^51]

Moderna’s vaccine vials hold 10 doses of 0.5mL each. Moderna combines 10 vials into one carton and 12 cartons into a case. Up to 192 cases can be stacked on one shipping pallet (which would then hold 230,400 doses).[^52]


## Global Distribution

From the previous sections, we already know that the vaccine is inside the multi-dose vials for the entire distribution process from the fill-and-finish to the [point of use](https://en.wikipedia.org/wiki/Point_of_care). This is unlike many other products which are shipped from the manufacturer in bulk quantities and split up into saleable units closer to the point of sale/care.

Which manufacturing location a vaccine originates from is determined by which country the point of use is located in, with the primary distinction being United States versus non-US for both Pfizer-BioNTech and Moderna supply chains. It seems likely that the supply chains will branch or split further as more countries with relevant local industry authorize the use of the vaccines.

The remaining challenge is transport of the vaccine vials to all points of care, such as hospitals, vaccine centers, and pharmacies. While the manufacturing process described above is a highly complicated process that occurs in a few well-defined environments, the distribution process is moderately complicated and needs to occur in countless environments with highly varied environments. The remaining sections attempt to do this complex challenge justice by highlighting a few specific aspects of it.


## Temperature Requirements

Temperature requirements are a defining characteristic of vaccine distribution in general. Vaccines, like many biological products, need to be _cooled_ in order to not degrade. Both Pfizer-BioNTech’s and Moderna’s vaccine require _frozen_ storage.

The term [cold chain](https://en.wikipedia.org/wiki/Cold_chain) is used broadly to describe all components of supply chains that require temperature control at below ambient conditions. Curiously, there appears to not be a corresponding term like “hot chain” related to products that have minimum temperature requirements such as cooked foods and some adhesives.

The Pfizer-BioNTech vaccine requires “ultra-low temperature” during transport and storage. Depending on which news article you read, the maximum permissible temperature is anywhere between -60°C (-76°F) and -80°C (-112°F). These are, in fact, the temperature bounds specified for storage at the point of use. Once thawed, further chilled storage at 2°C (36°F) to 8°C (46°F) is specified as permissible for up to five days.[^53] An assortment of news sources corroborate that the range from -60°C to -80°C is also maintained for all RNA-containing substances throughout the supply chain with the exception of a 72-hour window during the final assembly and filling[^54].

On December 28, shipments of the Pfizer-BioNTech vaccine from a Pfizer plant in Belgium to various European countries were delayed due to a “problem in the loading and shipment process” that was, allegedly, related to temperature control problems.[^55] Earlier in December, shipments of Pfizer-BioNTech vaccine in the US were returned to Pfizer after they were found to be at -92°C, i.e. colder than the specified temperature range.[^56]

[Moderna’s instructions to healthcare providers](https://www.modernacovid19global.com/ca/storage-handling-dosage-admin.pdf) specify a storage temperature range of -15°C to -25°C and specifically call out that dry ice must not be used and storage temperatures must not reach below -40°C. Once thawed, chilled storage at 2°C (36°F) to 8°C (46°F) is specified as permissible for up to 30 days and at up to 25°C (77°F) for 12 hours.[^57]

While there are no doubt fundamental reasons for temperature requirements, it is possible that the specific temperature ranges and durations may be relaxed in future. Any stated requirement is always based on testing of the prescribed conditions. For example, a five day storage limit specification is usually based on a scientifically rigorous experiment in which vaccine vials are stored for five days and then evaluated. Naturally, the number of such experiments is limited by the available resources and evaluation of common storage scenarios takes priority. This explains why the specified temperature ranges match the temperature ranges of available cold storage technologies. For example 2°C to 8°C is a range that can be maintained by most standard refrigerators. If there were commonly available devices that maintain a 3.14°C to 9¾°C temperature range (there aren’t), you would likely see this temperature range on the storage specifications. Moderna has already once extended its shelf life specification and alludes to further improvements being possible.[^58]


## Operation Warp Speed

[Operation Warp Speed](https://www.hhs.gov/coronavirus/explaining-operation-warp-speed/index.html) (OWS) is an effort by numerous US government agencies to facilitate the development and distribution of 300 million doses of COVID-19 vaccine by January 2021. The predominant tools employed are monetary grants and centralized sourcing. The vaccine distribution process within the United States is largely driven by OWS. The following figure is a schematic of the process as of the time of writing when only the Pfizer-BioNTech and Moderna vaccines were authorized for distribution in the US.

{{< figure
  src="/assets/2021/2021-01-10-ows-vaccine-distribution-process.png"
  title="Operation Warp Speed vaccine distribution process. Source: U.S. Department of Health & Human Services, https://www.hhs.gov/coronavirus/explaining-operation-warp-speed/index.html"
>}}

There are notable differences between the path shown for the Pfizer-BioNTech and Moderna vaccines. Pfizer appears to bypass almost all distribution steps! Indeed, Pfizer chose to ship its vaccine directly from its factory to the point of use.[^59] This is due to two reasons:



1. Pfizer and OWS interact very much “at arms length”. Contrary to Moderna and makers of other vaccine candidates, Pfizer did not receive US government funds for the development of the vaccine. Instead, it only has a supply contract which is structured to minimize US government involvement.[^60]


2. OWS currently only has a distribution contract for refrigerated and -20C cold chains.[^61] Therefore, it does not support the needs of the Pfizer-BioNTech vaccine. Of course, that situation would likely be different if Pfizer had indicated a need for assistance with distribution.
It is likely that most vaccines authorized for distribution in the US in future will follow Moderna’s pattern and not Pfizer’s, given that the makers of many promising vaccine candidates already have a closer relationship with OWS than Pfizer does.

Of the companies named in the OWS figure above, you have probably heard about UPS and FedEx, but maybe not of McKesson. [McKesson](https://www.mckesson.com/About-McKesson/Coronavirus-Response/) is an S&P 500 company. [This landing page on McKesson’s website](https://www.mckesson.com/About-McKesson/Coronavirus-Response/) describes their “COVID-19 response” and includes photos of Moderna vaccine being handled inside of McKesson distribution centers. Side note, due to [current events](https://sanfrancisco.cbslocal.com/2020/12/11/silicon-valley-exodus-oracle-moves-headquarters-redwood-city-austin-texas/): McKesson was ahead of the curve and moved their headquarters from San Francisco to Irving, Texas, in 2018.[^62]

[UPS Cold Chain Solutions](https://www.ups.com/us/en/services/healthcare/cold-chain-solutions.page) and [FedEx Cold Chain Services](http://www.fedex.com/pt_english/shipping-services/industry-solutions/supplychain/coldchain.html) are the existing cold chain logistics offerings of UPS and Fedex.

I was unable to find any evidence for [the Dippin’ Dots cold chain](https://www.popsci.com/story/health/covid-vaccine-cold-chain-dippin-dots-ice-cream/) getting utilized for vaccine distribution.


## Distribution Outside the United States

Pfizer’s Kalamazoo, Michigan, facility only produces vaccine doses for the United States market. All other countries to which Pfizer distributes the Pfizer-BioNTech vaccine receive it from Puurs, Belgium. This includes Canada, even though Canada is geographically much closer to Michigan than Belgium.[^63]

In Canada, Moderna’s vaccine is distributed by FedEx and [Innomar Strategies](https://www.innomar-strategies.com) which is a subsidiary of [AmerisourceBergen](https://www.amerisourcebergen.com).[^64]

In Germany, BioNTech and Moderna are both responsible for shipping to 25 distribution centers from where authorities handle the “last mile” delivery.[^65] Each of the 16 German states independently coordinates the final leg of the journey. For example, the state of North Rhine-Westphalia has contracted out all transport as well as operation of its distribution centers to Swiss-headquartered logistics company [Kuehne+Nagel](https://home.kuehne-nagel.com/homepage). The video in [this tweet](https://twitter.com/Kuehne_Nagel/status/1343448715869249536) shows the interior of one of those distribution centers. The states of Baden-Württemberg and Lower Saxony chose DHL instead.[^66]

The same Kuehne+Nagel mentioned in the previous paragraph  also has the contract for distribution of Moderna’s vaccine from the manufacturing location in Spain to customers in “Europe, Asia, Middle East and Africa, and parts of the Americas”[^67] (excluding USA and Canada, presumably). Swiss tabloid Blick calculates that the vaccine travels almost 4,000km between being produced in Visp, Switzerland, and arriving back in Switzerland: First for fill-finish to Spain, then to the Kuehne+Nagel distribution center in Geel, Belgium, then back to Switzerland.[^68] Note that this contract is about the transport from factory to distribution centers, while the aforementioned contract in Germany is about the transport from distribution center to point of use. The service is advertised as [KN PharmaChain](https://home.kuehne-nagel.com/-/services/pharma-healthcare-logistics) and just got expanded to now include 230 locations all over the world in September 2020.[^69]

Pfizer intends to bypass government-operated distribution processes in all countries. Their dedicated website on [Manufacturing and Distributing the COVID-19 vaccine states](https://www.pfizer.com/products/coronavirus/manufacturing-and-distribution):

> We have developed detailed logistical plans and tools to support effective vaccine transport, storage and continuous temperature monitoring. Our distribution is built on a flexible just-in-time system which will ship the frozen vials to the point of vaccination. Our distribution approach will be to largely ship from our Kalamazoo and Puurs sites direct to the point of use (POU). However, we will also be using our existing distribution centers for the COVID-19 distribution in Pleasant Prairie, WI and in Karlsruhe, Germany.

This is well-aligned with Pfizer’s stated goal to start selling the vaccine to customers other than governments in the future.


## Freezers

Freezers play a big role in the vaccine distribution and most articles about mRNA vaccine distribution mention freezers. For the purpose of this article, two broad categories of freezer matter: Regular freezers are those with temperature setpoints around -20°C like the one in kitchens. Ultra-cold freezers (or [ULT freezers](https://en.wikipedia.org/wiki/ULT_freezer)) have setpoints near -80°C.

Pfizer’s “freezer farm” in Kalamazoo, Michigan, gained some notoriety in the media while the first production batches of vaccine were stored there before the Emergency Use Authorization by the FDA arrived. If you look closely at [the photo](https://www.npr.org/sections/health-shots/2020/11/24/938591815/pfizers-coronavirus-vaccine-supply-contract-excludes-many-taxpayer-protections ), you can see that Pfizer has [Thermo Scientific TSX](https://www.thermofisher.com/us/en/home/life-science/lab-equipment/cold-storage/lab-freezers/ultra-low-temperature-freezers-minus-80/premium-tsx-ult-freezers.html) freezers that have stickers saying “-80°C” but all the displays read “-69°C”. TSX freezers support temperature set-points between -50°C and -86°C which makes them versatile but probably quite expensive (you’ll have to call to get a quote). German 400-person company Binder in Tuttlingen also manufactures ultra-cold freezers and sells them at prices between €15k and €20k.[^70]

The availability of ultra-cold freezers varies substantially around the world. For example, the country of Peru contains an estimated 30 such freezers[^71], that’s less than the number visible in Pfizer’s “freezer farm” photo.


## Dry Ice and Phase Change Materials

When active cooling in freezers is not available, the alternative is passive cooling where the substance that is to be cooled is placed in an insulated container together with another cold material. Dry ice and phase change materials are the two noteworthy options for that other cold material.

[Dry ice](https://en.wikipedia.org/wiki/Dry_ice) is simply compressed CO<sub>2</sub> and sublimates at −78.5°C. Sublimation is a phase change from solid to gaseous (instead of solid-to-liquid more commonly seen in everyday life). Dry ice production can happen at ambient temperatures. Because dry ice literally vanishes into thin air as it heats up, dry ice containers can simply be refilled to maintain cold temperatures inside. These two properties make dry ice a good option for keeping things cold or ultra-cold in locations where no freezers are available.

Depending on who you ask, there is plenty of dry ice production capacity available[^72] or there isn’t[^73]. The key ingredient for dry ice is liquid CO<sub>2</sub> which has been in shorter than usual supply during 2020 because it is a byproduct of natural gas production, of which there has been less of due to the overall reduction in economic activity.[^74]

The rate of sublimation, measured by weight of dry ice lost per hour, is an advertised feature of shipping boxes that are designed for use with dry ice. Pfizer’s shipping boxes achieve previously unheard rates of only 1%, compared to common values of 2-3%, prompting Boeing to revise their guidance for dry ice transport on planes with expanded charts.[^75]

Regulatory limits exist for the amount of dry ice permitted on planes because releasing CO<sub>2</sub> into an enclosed space can have undesirable side effects such as confusion or unconsciousness for the people in said space. The US FAA has granted United Airlines, Pfizer’s preferred vaccine air carrier, permission to exceed the former limit five-fold[^76] but also shared some advice to airlines such as how to avoid suffocation from the released CO2 and how to account for sublimation-induced weight loss when calculating the plane’s center of mass[^77].

If you think of dry ice as analogous to Duracell batteries, then phase change materials (PCM) are the rechargeable batteries. PCMs are also used to keep insulated containers cold, but instead of sublimating they change phase to liquid state when warming. You might have seen PCMs if you receive food or grocery deliveries from companies like BlueApron or HelloFresh who include gel packs in their shipping boxes to keep the food fresh. Phase change materials are reusable which is great if you have access to a freezer to “recharge” them.


## Shipping Boxes

Moderna’s vaccine requires more commonly available -20°C freezing and can rely on locally available cold chain infrastructure more readily. Facilities for Pfizer-BioNTech’s -70°C needs are much less widespread which is probably why Pfizer developed a custom shipping box. This difference is also why Moderna’s vaccine can be palletized while Pfizer’s stackability is limited.

As mentioned above, Moderna’s vaccine distribution in the US is handled by the government through Operation Warp Speed (OWS). If you take a close look at any of the photos from inside McKesson distribution centers, for example the one in [this MarketWatch article](https://www.marketwatch.com/story/moderna-starts-shipping-its-covid-19-vaccine-in-u-s-01608498586), you will see the brand name Ecoflex96 on the cardboard boxes. Despite the McKesson branding on some of them, the box is manufactured by [Cold Chain Technologies](https://www.coldchaintech.com) who announced their partnership with OWS [here](https://www.coldchaintech.com/news-item/cold-chain-technologies-provides-critical-thermal-packaging-for-operation-warp-speeds-covid-19-vaccination-rollout/) and has a [dedicated landing page](https://www.coldchaintech.com/covid-19-we-are-ready-able/) with all products suitable for shipping vaccines. [This unboxing video](https://vimeo.com/492538884) shows how the outer shell of an Ecoflex96 box contains gel (PCM) packs surrounding an inner cardboard box.

Pfizer’s choice of shipping box is easily determined from the instructions to healthcare providers available on their [various country-specific websites](https://www.cvdvaccine-us.com/resources). The two options described are containers by [Softbox Thermal Packaging Systems](https://www.softboxsystems.com ), headquartered in the 2,451 population village Long Crendon, United Kingdom, and [Aerosafe](https://www.aerosafeglobal.com/news) in Rochester, New York. [Softbox’s Twitter account ](https://twitter.com/SoftboxSystems)(377 followers) contains lots of photos and videos of their box in action as part of the Pfizer vaccine distribution. (AeroSafe has even fewer Twitter followers, but Softbox is one of them!) The photos and video embedded in [this article by Swiss Tagesanzeiger](https://www.tagesanzeiger.ch/so-arbeitet-die-impfanterie-der-armee-659893509675) show the arrival and unpacking of an AeroSafe box at an army facility in Ittingen, Switzerland. Fully loaded with vaccine and dry ice the containers weigh up to 36.5kg (81lb).

The company va-Q-tec based in Würzburg, Germany, is a university spinoff that has commercialized an insulation technology consisting of phase change material in a vacuum-sealed bag named “vacuum insulation panels”.[^78] They then use these panels to construct containers in sizes ranging from shoe box to shipping container. 2,500 of the latter are available as rentals from the company’s network of 40 international stations.[^79] You can see the production of vacuum insulation panels and some of the containers in [this video](https://www.dw.com/en/made-in-germany-containers-set-to-deliver-vaccines/av-55878745) by Deutsche Welle.

va-Q-tec is a bit tight-lipped about who their vaccine distributing customers are, referring, for example, to “one of the largest pharmaceutical manufacturers” in this [press release](https://va-q-tec.com/en/news-en/va-q-tec-signs-extensive-heads-of-terms-agreement-on-provision-of-thermal-containers-for-global-covid-19-vaccine-distribution-with-top-international-pharmaceuticals-producer/). However, if you know what the boxes look like, you start seeing them everywhere: In the [previously mentioned video](https://twitter.com/Kuehne_Nagel/status/1343448715869249536) of a German distribution center, in [this article](https://www.stripes.com/news/pacific/moderna-coronavirus-vaccine-arrives-at-us-bases-in-japan-for-priority-inoculations-1.656496) about Moderna vaccines arriving at a US Air Force base in Japan, and [on Reuters](https://www.reuters.com/article/health-coronavirus-va-q-tec-idUSKBN2841KU) thanks to their stock price going up and to the right.


## Temperature Trackers

Monitoring the temperature of chilled or frozen wares while in transit through a cold chain is pretty common. This monitoring is either done offline with temperature trackers that are read upon arrival, or online with devices that send temperature readings to a central database. The latter is one of the not [not useful](https://twitter.com/internetofshit) applications of the internet of things (IoT).

The built-in tracking devices in Pfizer’s custom designed shipping containers have started making headlines because the first instances of the trackers reporting failure of the cold chain have occurred. For example, [this Deutsche Welle article](https://p.dw.com/p/3nGgF) quotes a spokesman for the Germany city of Lichtenfels stating that theirs recorded a temperature of 15°C in transit.

Pfizer uses two types of temperature trackers from [Controlant](https://controlant.com ) and [Sensitech](https://www.sensitech.com).[^80] The tracker supplied by Icelandic startup Controlant[^81] is an online tracker that also includes a GPS receiver[^82]. It has three LED indicators for cold chain integrity, network connectivity, and battery life. Controlant even had time to customize the design and included a Pfizer logo. The other device by Sensitech (part of US conglomerate [Carrier](https://www.corporate.carrier.com)) is the [TempTale Ultra](https://www.sensitech.com/en/media/TTUItra_LS_060820_Web_tcm35-80848.pdf) and is an offline logger with an LCD display as readout. The devices are embedded into the insulation part of Pfizer’s shipping box assembly.

It’s safe to assume that all steps of all distribution processes of both vaccines are somehow temperature monitored. For example, Moderna’s vaccine shipments through McKesson in the US contain an unspecified “digital temperature monitor” that allows recipients to validate cold chain compliance, apparently without any remote connectivity.[^83]


## Glass Vials

Both Pfizer-BioNTech’s and Moderna’s vaccine vials consist of the glass container holding the vaccine liquid and a rubber stopper.

Vials are not made out of any old glass because they must withstand mechanical shocks during transport as well as thermal shocks during freezing and thawing. For over a century, the material of choice for pharmaceutical vials has been [borosilicate glass](https://en.wikipedia.org/wiki/Borosilicate_glass). Valor Glass is a novel type of glass that has only been commercially available for a few years and could displace borosilicate glass due to its superior properties.

Shock resistance is not only prized in vaccine storage, which is why borosilicate glass has many other applications including kitchenware and as a substrate in electronics. The chemical element [boron](https://en.wikipedia.org/wiki/Boron) is the component that contributes the first half of the name “borosilicate” and the key properties of the glass. Turkey’s state owned company Eti Mine Works produced almost three quarters of the world’s supply, the remainder comes from [Rio Tinto Borax Mine](https://en.wikipedia.org/wiki/Rio_Tinto_Borax_Mine) in Boron, California.

A handful of manufacturers dominate the world production of borosilicate glass in the vaccine vial form factor.

[Schott AG](https://www.schott.com), headquartered in Mainz, Germany, was founded by the inventor of borosilicate glass and produces vials in Germany, India, Brazil, and, as of recently, in China.[^84] Schott claims that “three out of four COVID-19 vaccine projects rely on Schott vials” and mentions supplying Operation Warp Speed partners.[^85]

Fellow German glass vial maker [Gerresheimer AG](https://www.gerresheimer.com), produces borosilicate glass vials in China, India, USA, Mexico, France, and Poland. The company estimates that it will produce one billion additional vials over the next two years.[^86] I wasn't able to find information about any specific contracts, but [this case study](https://www.gerresheimer.com/en/news-events/corporate-news/show/gerresheimer-sets-foundation-for-profitable-growth-in-2019.html) about how Gerresheimer went about rapidly getting their IT systems up to snuff for a remote workforce provided some welcome diversion from vaccine-related reading.

[Stevanato Group](https://www.stevanatogroup.com/en/) in Padua, Italy, does not supply vials for the Pfizer-BioNTech and Moderna vaccines but supplies 100 million borosilicate glass vials to the [Coalition for Epidemic Preparedness Innovations](https://cepi.net) (CEPI) behind the [COVAX](https://cepi.net/COVAX/) initiative.[^87]

Other borosilicate glass manufacturers who may or may not currently supply borosilicate glass vials for COVID-19 vaccines are [Borosil](https://www.borosil.com/what-we-do/pharmaceutical-packaging/) in India and [Corning](https://www.corning.com/worldwide/en/products/pharmaceutical-technologies/valor-glass.html) in the USA (more about Corning below).

Just like COVID-19 catapulted mRNA vaccines from obscurity into high-volume commercial use, it also launched a glass research project into mass production: The company [Corning](https://www.corning.com/worldwide/en/products/pharmaceutical-technologies/valor-glass.html), a brand practically synonymous with all things glass in America, had been developing a new material they call “[Valor Glass](https://www.corning.com/worldwide/en/products/pharmaceutical-technologies/valor-glass.html)” since 2011.[^88] The glass does not contain boron (but instead alumina) and undergoes a surface treatment similar to Corning’s [Gorilla Glass](https://en.wikipedia.org/wiki/Gorilla_Glass) of smartphone screen fame. [This Hackaday post](https://hackaday.com/2020/12/28/the-high-tech-valor-glass-vials-used-to-deliver-the-coronavirus-vaccine/) has more details on the what and how of Valor Glass as well as embedded videos of crushed and shattered vaccine vials. In short: Valor Glass is 50 times stronger under compression and does not suffer from [delamination](https://www.corning.com/worldwide/en/products/pharmaceutical-technologies/pharma-technologies-delamination.html). In May 2020, Pfizer signed a supply agreement for Valor Glass[^89] and in June 2020 Operation Warp Speed provided funding to expand US-based manufacturing of Valor Glass[^90].

Now that both Gerresheimer and Corning have been introduced, let’s make things even more confusing: In 2015 Gerresheimer sold their pharmaceutical (borosilicate) glass tube production business to Corning. As a result, Corning now owns factories in Vineland, New Jersey, and Pisa, Italy. Gerresheimer continues to make borosilicate _vials_, and has a 10-year contract to purchase the tubes necessary for doing so from Corning. There’s more: As part of the deal, Corning and Gerresheimer created a 75/25 joint venture to “accelerate Corning innovations for the pharmaceutical glass packaging market.”[^91] That explains why Gerresheimer recently published [this press release](https://www.gerresheimer.com/en/news-events/corporate-news/show/corning-and-gerresheimer-collaborate-to-deliver-new-corning-valortm-glass-to-the-pharmaceutical-packa.html) announcing their increase in supply of Valor Glass together with Corning. Another fun fact about Corning and Gerresheimer: Both companies share their name with the towns they are located in, Corning in Upstate New York and the Gerresheim borough of Düsseldorf in Germany.

[SiO2 Materials Science](https://www.sio2ms.com) in Auburn, Alabama, is another recipient of OWS funds. The company produces a “plastic container with a microscopic, thin, undetectable to the naked eye, pure glass coating.” Since June 2020, the company has increased their staff by 5x and their production rate by 12x.[^92] In 1963, this same company was the first to manufacture the one-gallon plastic milk jug with a built-in handle and leak proof cap that you can still find in fridges all over America today.

As is true for all other vaccine ingredients and accessory components, the demand for COVID-19 vaccine vials needs to be met on top of the existing demand for all other types of vaccines. Despite the optimistic projections for vial production numbers by all vendors, it’s worth acknowledging that the current situation is a workaround. If glass vial supply was unlimited, manufacturers wouldn’t fill multiple doses into a single vial.[^93] In fact, there would be no vials at all because a preferred form factor for vaccine distribution is the prefilled syringe. In May 2020 the US DoD awarded a contract to [ApiJect Systems America](https://apiject.com) to develop a facility for producing 100 million prefilled syringes for distribution by year-end 2020.[^94] The same company now constructs a second, larger, prefilled syringe facility in Research Triangle Park, North Carolina, and calls it the “ApiJect Gigafactory”.[^95]


## Point of Use

{{< figure
  src="/assets/2021/2021-01-10-baltimore.jpg"
  title="A station at a vaccination clinic for Baltimore County frontline health workers on Wednesday, December 23, 2020. This clinic used the Moderna vaccine. Source/attribution: Baltimore County Government, https://www.flickr.com/photos/baltimorecounty/50753216127/"
>}}

{{< figure
  src="/assets/2021/2021-01-10-strasbourg.jpg"
  title="A vaccination station at the University Hospital in Strasbourg on January 8, 2021. The vaccine shown is Pfizer/BioNTech’s Comirnaty. The tray appears to contain four remaining prepared syringes and the empty vial they were drawn from. Source/attribution: © Claude Truong-Ngoc / Wikimedia Commons (CC-BY-SA-4.0)"
>}}

Depending on when and where you receive your vaccine, the “point of use” might be a doctor’s office, vaccine center, pharmacy, etc. Several resources are required for each injection of either vaccine:



* 1 syringe and needle suitable for the injection into the patient’s arm
* 1 antiseptic wipe/swab for cleaning the injection site on the patient’s arm
* 1 medical exam glove
* For disposal, a sharps container needs to be present. In the photo from Baltimore above a tupperware box fills in as the sharps container.

Additional materials are required for the Pfizer-BioNTech vaccine. Each vial needs to be diluted with 1.8mL of 0.9% NaCl (sodium chloride) shortly before use.[^96] The transfer of sodium chloride into the vaccine vial (and removal of corresponding volume of air) requires one sufficiently large syringe (Pfizer recommends 3mL or 5mL) and one corresponding needle _per vial_. Furthermore, anyone who deals with Pfizer’s shipping container needs appropriate protective equipment and safety training before handling dry ice.

In the United States the government supplies these supplies, as part of Operation Warp Speed (OWS). Kitting and delivery of Moderna (and all future OWS partners’ kits) is handled by OWS distribution partner McKesson.[^97] In this system, Moderna vaccine shipments are accompanied by the supplies required to administer them. As usual, Pfizer bypasses the government-operated supply chain and ships “mega kits” of supplies that contain enough materials to administer 1,000 doses as well as one set of gloves for handling dry ice. “Mega kits” arrive at the point of use separately from the vaccine.

The exact type and supplier of syringe in the kits varies, probably because of supply constraints. A key difference between syringe types is the amount of “dead volume” that remains in the syringe after pushing the plunger all the way. Every single-use syringe has some dead volume, simply because the plunger cannot possibly reach into the syringe needle. Some syringes are specifically advertised as “low dead-volume syringes” and have tens of microliters lower dead volume than those not advertised as such. Multiply that by five doses per vial for Pfizer-BioNTech or 10 doses per vial for Moderna, and you get a number in the same order of magnitude as a vaccination dose. This explains why some vaccination sites report finding extra doses in many vials: They are working with supply kits that contain low dead-volume syringes.[^98]

One of the more surprising shortages during the COVID-19 pandemic has been for rubber ([nitrile](https://en.wikipedia.org/wiki/Nitrile_rubber)) [gloves](https://en.wikipedia.org/wiki/Medical_glove). A combination of COVID-19 outbreaks affecting the glove producers in Malaysia[^99], floods and weather in Thailand and Vietnam, and increased demand due to COVID-19-related use are among the reasons for a shortage that lasted throughout 2020.[^100] In the United States, [Showa](https://www.showagroup.com/us/) in Fayette, Alabama, is the only domestic (but Japanese-owned) manufacturer of nitrile gloves and is currently doubling its production capacity.[^101]

Not listed on any bill of materials but very much required: A trained healthcare professional to prepare and administer each dose. The human component of healthcare has often been overlooked during this pandemic while the conversation focused on counting ventilators and ICU beds. Who is qualified and permitted to perform vaccine administration varies by country. My personal experience is that in the United States I have received vaccines from nurses and pharmacists and in Germany only from medical doctors.

Finally, a recipient for the vaccine is needed. While demand no doubt exists, bringing ready-to-administer vaccine doses and the same number of vaccine recipients into the same place at the same time is the final logistical challenge in the supply chain. The Pfizer-BioNTech vaccine’s short shelf life at room temperature combined with the inability to refreeze vials means that the number of doses to prepare for a session must be forecast many hours before the first vaccine recipient shows up.


## Information Material for Patients and Providers

Every pharmaceutical product is accompanied by some information materials. From prescription and over-the-counter medications, you might know the printed [directions for use](https://www.accessdata.fda.gov/scripts/cder/training/OTC/topic2/topic2/da_01_02_0090.htm) and other legally required [package inserts](https://en.wikipedia.org/wiki/Medication_package_insert). Vaccines are administered by a healthcare professional and require specific preparation steps (see above) demanding slightly different information materials.

For both the Pfizer-BioNTech and Moderna vaccines, I came across the following materials:



* Patient information sheets with information about active ingredients, side effects, etc.
* Patient FAQs addressing common questions in everyday language
* Guides on handling, storage, and opening of shipments for healthcare providers
* Reminder cards or similar printables to increase the likelihood that patients get the second dose, at all and at the right time
* Instructions on how to report “adverse events” to the appropriate local authorities ([e.g. the FDA](https://www.fda.gov/drugs/drug-approvals-and-databases/fda-adverse-event-reporting-system-faers)) and the provider.
* Video tutorials for healthcare providers

Additionally, Pfizer-BioNTech have:



* Safety information for handling dry ice
* Instructions for how to return shipping containers

The exact list and formats of materials must match the needs and regulations of every jurisdiction. For example, many countries require labels and printed materials to be included in a local language. Tracking tens of localized versions of vaccine packages from final filling (when the vial label is applied) to point of use would multiply the supply chain complexity and slow down the process. This has led to unusual accommodation such as the European Commission permitting English-only materials for all EU countries as long as a digital version of the localized materials is available for printing at the point of use.[^102]

BioNTech really benefits from working with Pfizer and is miles ahead of Moderna in terms of how many materials they have available: At the time of writing, Pfizer-BioNTech has 44 localized websites up, each with its own local domain name and local email addresses and so on. Some of the PDF file names look like “Hqrdtemplateclean_de” suggesting that they follow a playbook and have templates ready. Looking up some of the 44 domains suggests that they are using [Cloudflare](https://www.cloudflare.com) as registrar and hosting provider.

At time of writing, Moderna has local websites for Canada, Israel, and USA, hosted on AWS.


## Call Centers

Some situations and people will require additional advice, which is why each vaccine (and most other pharmaceutical products) have a phone hotline. For example, residents of Canada and the US can report side effects for the Moderna vaccine by calling 1-866-MODERNA (after notifying local authorities first). This number is currently registered to the company [Five 9](https://www.five9.com), which likely also staffs and operates the call center given that healthcare call centers are one of their offerings. Outsourcing your call center means that someone had to develop the scripts and knowledge base referenced by the phone agents–probably enough work for another full time staffer.

Pfizer-BioNTech again uses the benefit of Pfizer’s existing infrastructure and lists local number for many countries, including 28 different ones for European countries in [their German patient information leaflet](https://www.comirnatyeducation.de/files/Comirnaty_PIL_Germany.pdf) alone.


## Track & Trace

[Pharmaceutical crime](https://www.interpol.int/Crimes/Illicit-goods/Pharmaceutical-crime-operations) is big business and COVID-19 vaccines are probably an especially attractive target given how big the gap between supply and demand is. First reports of real vaccine doses being redirected out of the regular distribution for profit are appearing in the media, for example [in Florida](https://www.usatoday.com/story/news/2021/01/07/elder-care-center-morselife-under-investigation-giving-covid-vaccine-palm-beach-jet-set/6585387002/). The introduction of illicit vaccines, which may be entirely fake or diluted or otherwise tampered with, is also a risk but at the time of writing I couldn’t find any credible reports of that happening.

Many countries have regulations that aim to prevent pharmaceutical crimes through tracking and tracing of every lot of every unit. These are generally focused on the distribution of the finished product because this is where the biggest attack surface exists in the supply chain. In the United States, the [Drug Supply Chain and Security Act](https://www.fda.gov/drugs/drug-supply-chain-integrity/drug-supply-chain-security-act-dscsa) (DSCSA) demands that the smallest unit saleable unit of the product must carry a 2D data matrix code (similar to QR code). This code must encode a product identifier, serial number, batch number, and the expiry data. Verification of the serial number is prescribed for certain transactions such as returns. Companies like [Tracelink](https://www.tracelink.com) provide compliance with these regulations as a service. Side note: The predecessor to the DSCSA [was filibustered in the US Senate](https://en.wikipedia.org/wiki/Drug_Quality_and_Security_Act#Vitter_filibuster).

The smallest saleable unit for the vaccines covered in this article are the multi-dose vials. Despite my best search efforts I wasn’t able to find a photo of either Pfizer-BioNTech or Moderna vaccine vials that show a complete data matrix code. In fact, most stock photos show mockup vials that lack the required identifiers entirely. Moderna’s website shows a schematic of the vial label on their [tool for looking up expiry dates](https://www.modernatx.com/covid19vaccine-eua/providers/vial-lookup).

In addition to the codes on each vial, there are additional codes on the information materials. Those are not serialized and their purpose is to facilitate data entry into electronic medical records systems, e.g. when a nurse records a vaccine administration into a patient’s file. In the United States, [the CDC assigns product identifiers that must be printed as 1D or 2D codes onto the vaccine information statement](https://www.cdc.gov/vaccines/hcp/vis/barcodes.html) (VIS). The identifiers assigned to the Pfizer-BioNTech and Moderna vaccines are published [here](https://www.cdc.gov/vaccines/programs/iis/code-sets.html). Obviously, that means that the VIS can only be printed once the CDC has performed the assignment.

Sadly, no amount of tracing prevents sabotage such as the [intentional destruction of vaccines](https://www.reuters.com/article/us-health-coronavirus-usa-pharmacist-idUSKBN2961YF), (for which there is also no clear incentive).


## Conclusion

At the top of this article I rhetorically asked whether mRNA vaccines for COVID-19 might be the next “distributed manufacturing revolution” with RNA printers churning out vaccine in garages all over the world. There’s a bit of a punchline to this idea: Technically, the last step of the supply chain of these mRNA COVID-19 vaccines is the production of the spike protein. That’s what happens in the cells of your body after you receive the vaccine. _You_ are the globally distributed vaccine manufacturing revolution.

This investigation into the supply chain of the Pfizer-BioNTech and Moderna COVID-19 vaccines ends here. Of course, there are many more details and tangents to be explored, the [TED talk about making a toaster from scratch](http://www.ted.com/talks/thomas_thwaites_how_i_built_a_toaster_from_scratch) could really use a sequel. Please [send me an email](mailto:jn@jonasneubert.com) if you have suggestions for what to add or corrections for what is already there.


## Acknowledgements

Thanks to [Ted](https://twitter.com/tedder42), [Roman](https://hut.pm), [Noah](https://www.noahleidinger.com/en/about), [Keith](https://suddenlyathome.net), [Bill](http://eqvanalytics.com/moderna-vaccine-tracker.html), [Cameron](https://www.linkedin.com/in/cameron-robert-ferguson-597a2b145/), [Manny](https://twitter.com/Riboguy), [Mike](https://twitter.com/MikeDeeeeeee), [Jim](http://jdlh.com/), and Bobby for sending corrections and suggestions.


## Notes

[^1]:

     [https://www.scientificamerican.com/article/new-covid-vaccines-need-absurd-amounts-of-material-and-labor1/](https://www.scientificamerican.com/article/new-covid-vaccines-need-absurd-amounts-of-material-and-labor1/)

[^2]:

     [https://www.neb.com/gmp/gmp-grade-reagents-for-rna-synthesis](https://www.neb.com/gmp/gmp-grade-reagents-for-rna-synthesis)

[^3]:
     [https://caretdashcaret.com/2020/12/30/pseudouridylyl-not-pseudouridine/](https://caretdashcaret.com/2020/12/30/pseudouridylyl-not-pseudouridine/)

[^4]:
     [https://news.ycombinator.com/item?id=25539741](https://news.ycombinator.com/item?id=25539741)

[^5]:
     [https://www.researchgate.net/publication/333456052_Design_of_in_vitro_Transcribed_mRNA_Vectors_for_Research_and_Therapy](https://www.researchgate.net/publication/333456052_Design_of_in_vitro_Transcribed_mRNA_Vectors_for_Research_and_Therapy)

[^6]:
    [ https://aiche.onlinelibrary.wiley.com/doi/full/10.1002/amp2.10060](https://aiche.onlinelibrary.wiley.com/doi/full/10.1002/amp2.10060)

[^7]:
     [https://www.exeleadbiopharma.com/news/liposomes-and-lipid-nanoparticles-as-delivery-vehicles-for-personalized-medicine](https://www.exeleadbiopharma.com/news/liposomes-and-lipid-nanoparticles-as-delivery-vehicles-for-personalized-medicine)

[^8]:

     [https://patents.google.com/patent/WO2018081480A1](https://patents.google.com/patent/WO2018081480A1)

[^9]:
    [ https://www.fda.gov/media/144413/download](https://www.fda.gov/media/144413/download)

[^10]:

     [https://www.reuters.com/article/us-moderna-patent-idUSKCN24O2XY](https://www.reuters.com/article/us-moderna-patent-idUSKCN24O2XY)

[^11]:
     [https://www.bio-rad.com/featured/en/tris-buffer.html](https://www.bio-rad.com/featured/en/tris-buffer.html)

[^12]:
     [https://www.politico.eu/article/merkel-us-uk-speed-on-vaccines-rankles-but-nothing-wrong-with-eu-approach/](https://www.politico.eu/article/merkel-us-uk-speed-on-vaccines-rankles-but-nothing-wrong-with-eu-approach/)

[^13]:
     [https://www.sec.gov/Archives/edgar/data/1682852/000168285220000023/lonzamodernagltafullye.htm](https://www.sec.gov/Archives/edgar/data/1682852/000168285220000023/lonzamodernagltafullye.htm)

[^14]:
     [https://www.bostonmagazine.com/health/2020/06/04/moderna-coronavirus-vaccine/](https://www.bostonmagazine.com/health/2020/06/04/moderna-coronavirus-vaccine/)

[^15]:
     [https://www.usatoday.com/story/news/health/2021/02/07/pfizer-expects-cut-covid-19-vaccine-production-time-almost-50/4423251001/](https://www.usatoday.com/story/news/health/2021/02/07/pfizer-expects-cut-covid-19-vaccine-production-time-almost-50/4423251001/)

[^16]:
     [https://investors.biontech.de/news-releases/news-release-details/pfizer-and-biontech-co-develop-potential-covid-19-vaccine](https://investors.biontech.de/news-releases/news-release-details/pfizer-and-biontech-co-develop-potential-covid-19-vaccine)

[^17]:
     [https://investors.biontech.de/news-releases/news-release-details/pfizer-and-biontech-celebrate-historic-first-authorization-us](https://investors.biontech.de/news-releases/news-release-details/pfizer-and-biontech-celebrate-historic-first-authorization-us)

[^18]:
     [https://www.reuters.com/article/biontech-fosunpharma-vaccine-collaborati/biontech-in-china-alliance-with-fosun-over-coronavirus-vaccine-candidate-idUSL8N2B90UW](https://www.reuters.com/article/biontech-fosunpharma-vaccine-collaborati/biontech-in-china-alliance-with-fosun-over-coronavirus-vaccine-candidate-idUSL8N2B90UW)

[^19]:
     [https://investors.biontech.de/static-files/82c9e451-7503-4217-a51f-ee7fb6497b17](https://investors.biontech.de/static-files/82c9e451-7503-4217-a51f-ee7fb6497b17)

[^20]:
     [https://pfe-pfizercom-d8-prod.s3.amazonaws.com/Vaccines_Infographic5_July2020.pdf](https://pfe-pfizercom-d8-prod.s3.amazonaws.com/Vaccines_Infographic5_July2020.pdf)

[^21]:
     [https://www.usatoday.com/story/news/health/2021/02/07/pfizer-expects-cut-covid-19-vaccine-production-time-almost-50/4423251001/](https://www.usatoday.com/story/news/health/2021/02/07/pfizer-expects-cut-covid-19-vaccine-production-time-almost-50/4423251001/)

[^22]:
     [https://www.nature.com/articles/d41586-019-03072-8](https://www.nature.com/articles/d41586-019-03072-8)

[^23]:
     [https://www.lonza.com/investor-relations/-/media/38ADC8E8FB834519B5E7FDA0EC1DC15E.ashx](https://www.lonza.com/investor-relations/-/media/38ADC8E8FB834519B5E7FDA0EC1DC15E.ashx)

[^24]:
     [https://cen.acs.org/business/outsourcing/Pfizer-Moderna-ready-vaccine-manufacturing/98/i46](https://cen.acs.org/business/outsourcing/Pfizer-Moderna-ready-vaccine-manufacturing/98/i46)

[^25]:
     [https://seekingalpha.com/article/4398427-moderna-inc-mrna-ceo-stephane-bancel-presents-39th-annual-jpmorgan-virtual-healthcare](https://seekingalpha.com/article/4398427-moderna-inc-mrna-ceo-stephane-bancel-presents-39th-annual-jpmorgan-virtual-healthcare)

[^26]:
     [https://www.washingtonpost.com/health/2020/11/17/coronavirus-vaccine-manufacturing/](https://www.washingtonpost.com/health/2020/11/17/coronavirus-vaccine-manufacturing/)

[^27]:
     [https://biontechse.gcs-web.com/node/9081/pdf](https://biontechse.gcs-web.com/node/9081/pdf)

[^28]:
     [https://www.rentschler-biopharma.com/news/press-releases-and-announcements/detail/view/joining-forces-against-sars-cov-2/](https://www.rentschler-biopharma.com/news/press-releases-and-announcements/detail/view/joining-forces-against-sars-cov-2/)

[^29]:
     [https://www.scientificamerican.com/article/new-covid-vaccines-need-absurd-amounts-of-material-and-labor1/](https://www.scientificamerican.com/article/new-covid-vaccines-need-absurd-amounts-of-material-and-labor1/)

[^30]:
     [https://www.gao.gov/products/GAO-21-207](https://www.gao.gov/products/GAO-21-207)

[^31]:
     [https://www.spiegel.de/wirtschaft/unternehmen/coronavirus-wie-der-staat-schnell-fuer-mehr-impfdosen-sorgen-koennte-a-00000000-0002-0001-0000-000175196816](https://www.spiegel.de/wirtschaft/unternehmen/coronavirus-wie-der-staat-schnell-fuer-mehr-impfdosen-sorgen-koennte-a-00000000-0002-0001-0000-000175196816)

[^32]:
     [https://www.cordenpharma.com/CordenPharma_and_Moderna_Extend_Lipid_Supply_Agreement_for_Moderna_Vaccine_mRNA-1273_Against_Novel_Coronavirus_SARS-CoV-2](https://www.cordenpharma.com/CordenPharma_and_Moderna_Extend_Lipid_Supply_Agreement_for_Moderna_Vaccine_mRNA-1273_Against_Novel_Coronavirus_SARS-CoV-2)

[^33]:
     [https://www.cordenpharma.com/press-release/CDMO_Expands_US_Peptide_Manufacturing_Capacity](https://www.cordenpharma.com/press-release/CDMO_Expands_US_Peptide_Manufacturing_Capacity)

[^34]:
     [https://www.knauer.net/en/knauer-is-expanding-its-business-activities-into-the-field-of-lipid-nanoparticle-production-equipment/n39517](https://www.knauer.net/en/knauer-is-expanding-its-business-activities-into-the-field-of-lipid-nanoparticle-production-equipment/n39517)

[^35]:
     [https://investors.biontech.de/covid-19-vaccine-partners](https://investors.biontech.de/covid-19-vaccine-partners)

[^36]:
     [https://www.pharmaceuticalonline.com/doc/lipid-nanoparticles-are-having-a-breakout-moment-0001](https://www.pharmaceuticalonline.com/doc/lipid-nanoparticles-are-having-a-breakout-moment-0001)

[^37]:
     [https://acuitastx.com/wp-content/uploads/2020/12/Emergency-Use-Authorization-Release.pdf](https://acuitastx.com/wp-content/uploads/2020/12/Emergency-Use-Authorization-Release.pdf)

[^38]:
     [https://www.spiegel.de/wirtschaft/unternehmen/coronavirus-wie-der-staat-schnell-fuer-mehr-impfdosen-sorgen-koennte-a-00000000-0002-0001-0000-000175196816](https://www.spiegel.de/wirtschaft/unternehmen/coronavirus-wie-der-staat-schnell-fuer-mehr-impfdosen-sorgen-koennte-a-00000000-0002-0001-0000-000175196816)

[^39]:
     [https://www.wsj.com/articles/if-one-leading-coronavirus-vaccine-works-thank-this-tiny-firm-in-rural-austria-11604664001](https://www.wsj.com/articles/if-one-leading-coronavirus-vaccine-works-thank-this-tiny-firm-in-rural-austria-11604664001)

[^40]:

     [https://investors.biontech.de/news-releases/news-release-details/biontech-acquire-gmp-manufacturing-site-expand-covid-19-vaccine](https://investors.biontech.de/news-releases/news-release-details/biontech-acquire-gmp-manufacturing-site-expand-covid-19-vaccine)

[^41]:

     [https://www.deraktionaer.de/artikel/pharma-biotech/corona-impfstoff-biontech-und-dermapharm-kooperieren-aktionaer-top-tipp-im-aufwind-20206842.html](https://www.deraktionaer.de/artikel/pharma-biotech/corona-impfstoff-biontech-und-dermapharm-kooperieren-aktionaer-top-tipp-im-aufwind-20206842.html)

[^42]:

     [https://www.siegfried.ch/siegfried+und+biontech+unterzeichnen+vertrag+zur+aseptischen+abf%25c3%25bcllung+eines+covid-19-impfstoffes/news/5738](https://www.siegfried.ch/siegfried+und+biontech+unterzeichnen+vertrag+zur+aseptischen+abf%25c3%25bcllung+eines+covid-19-impfstoffes/news/5738)

[^43]:

     [https://www.spiegel.de/wirtschaft/corona-warum-es-so-schwierig-ist-schnell-mehr-impfstoff-herzustellen-a-00000000-0002-0001-0000-000175089041](https://www.spiegel.de/wirtschaft/corona-warum-es-so-schwierig-ist-schnell-mehr-impfstoff-herzustellen-a-00000000-0002-0001-0000-000175089041)

[^44]:

     [https://www.fiercepharma.com/pharma/sanofi-after-r-d-setback-lends-a-hand-to-vaccine-rival-pfizer-for-coronavirus-shot](https://www.fiercepharma.com/pharma/sanofi-after-r-d-setback-lends-a-hand-to-vaccine-rival-pfizer-for-coronavirus-shot)

[^45]:

     [https://www.novartis.com/news/media-releases/novartis-signs-initial-agreement-provide-manufacturing-capacity-pfizer-biontech-covid-19-vaccine](https://www.novartis.com/news/media-releases/novartis-signs-initial-agreement-provide-manufacturing-capacity-pfizer-biontech-covid-19-vaccine)

[^46]:
     [https://www.catalent.com/catalent-news/moderna-and-catalent-announce-collaboration-for-fill-finish-manufacturing-of-modernas-covid-19-vaccine-candidate/](https://www.catalent.com/catalent-news/moderna-and-catalent-announce-collaboration-for-fill-finish-manufacturing-of-modernas-covid-19-vaccine-candidate/)

[^47]:
     [https://rovi.es/en/content/moderna-and-rovi-announce-collaboration-outside-united-states-fill-finish-manufacturing-0](https://rovi.es/en/content/moderna-and-rovi-announce-collaboration-outside-united-states-fill-finish-manufacturing-0)

[^48]:
     [https://www.recipharm.com/press/recipharm-and-moderna-finalize-agreement-aseptic-drug-product-manufacturing-and-fill-finish](https://www.recipharm.com/press/recipharm-and-moderna-finalize-agreement-aseptic-drug-product-manufacturing-and-fill-finish)

[^49]:
     [https://www.reuters.com/article/us-health-coronavirus-ema-pfizer-idUSKBN29D1L4](https://www.reuters.com/article/us-health-coronavirus-ema-pfizer-idUSKBN29D1L4)

[^50]:
     [https://www.politico.com/news/2020/12/16/pfizer-vaccine-extra-doses-447117](https://www.politico.com/news/2020/12/16/pfizer-vaccine-extra-doses-447117)

[^51]:
     [https://www.scientificamerican.com/article/the-covid-cold-chain-how-a-vaccine-will-get-to-you/](https://www.scientificamerican.com/article/the-covid-cold-chain-how-a-vaccine-will-get-to-you/)

[^52]:
     [https://www.modernatx.com/covid19vaccine-eua/providers/storage-handling](https://www.modernatx.com/covid19vaccine-eua/providers/storage-handling)

[^53]:
     [https://www.cvdvaccine.ca/product-storage-and-dry-ice](https://www.cvdvaccine.ca/product-storage-and-dry-ice)

[^54]:
     [https://www.washingtonpost.com/health/2020/11/17/coronavirus-vaccine-manufacturing/](https://www.washingtonpost.com/health/2020/11/17/coronavirus-vaccine-manufacturing/)

[^55]:
     [https://p.dw.com/p/3nHWs](https://p.dw.com/p/3nHWs)

[^56]:
     [https://www.supplychaindive.com/news/pfizer-vaccine-deliveries-turned-around-after-becoming-too-cold/592447/](https://www.supplychaindive.com/news/pfizer-vaccine-deliveries-turned-around-after-becoming-too-cold/592447/)

[^57]:
     [https://www.modernatx.com/covid19vaccine-eua/providers/storage-handling](https://www.modernatx.com/covid19vaccine-eua/providers/storage-handling)

[^58]:
     [https://investors.modernatx.com/news-releases/news-release-details/moderna-announces-longer-shelf-life-its-covid-19-vaccine](https://investors.modernatx.com/news-releases/news-release-details/moderna-announces-longer-shelf-life-its-covid-19-vaccine)

[^59]:
     [https://www.fiercepharma.com/pharma/pfizer-sidelines-us-government-covid-19-vaccine-distribution-plan-favor-its-own-reports](https://www.fiercepharma.com/pharma/pfizer-sidelines-us-government-covid-19-vaccine-distribution-plan-favor-its-own-reports)

[^60]:

     [https://www.npr.org/sections/health-shots/2020/11/24/938591815/pfizers-coronavirus-vaccine-supply-contract-excludes-many-taxpayer-protections](https://www.npr.org/sections/health-shots/2020/11/24/938591815/pfizers-coronavirus-vaccine-supply-contract-excludes-many-taxpayer-protections)

[^61]:

     [https://www.mckesson.com/About-McKesson/Coronavirus-Response/](https://www.mckesson.com/About-McKesson/Coronavirus-Response/)

[^62]:
     [https://www.mckesson.com/about-mckesson/newsroom/press-releases/2018/mckesson-announces-new-headquarters-in-las-colinas-texas/](https://www.mckesson.com/about-mckesson/newsroom/press-releases/2018/mckesson-announces-new-headquarters-in-las-colinas-texas/)

[^63]:
     [https://www.businessinsider.com/europe-canada-covid-19-vaccine-cuts-as-pfizer-renovates-plant-2021-1](https://www.businessinsider.com/europe-canada-covid-19-vaccine-cuts-as-pfizer-renovates-plant-2021-1)

[^64]:
     [https://www.canada.ca/en/public-services-procurement/news/2020/12/government-of-canada-awards-contract-to-distribute-covid-19-vaccine-from-coast-to-coast-to-coast.html](https://www.canada.ca/en/public-services-procurement/news/2020/12/government-of-canada-awards-contract-to-distribute-covid-19-vaccine-from-coast-to-coast-to-coast.html)

[^65]:
     [https://www.dw.com/en/coronavirus-digest-uk-hits-new-covid-infection-record/a-56071203](https://www.dw.com/en/coronavirus-digest-uk-hits-new-covid-infection-record/a-56071203)

[^66]:
     [https://www.zeit.de/politik/deutschland/2020-12/corona-impfungen-impfstoff-logistik-impfzentren-gesundheitssystem](https://www.zeit.de/politik/deutschland/2020-12/corona-impfungen-impfstoff-logistik-impfzentren-gesundheitssystem)

[^67]:
     [https://newsroom.kuehne-nagel.com/kuehnenagel-finalises-agreement-with-moderna-for-covid-19-vaccine-distribution/](https://newsroom.kuehne-nagel.com/kuehnenagel-finalises-agreement-with-moderna-for-covid-19-vaccine-distribution/)

[^68]:
     [https://www.blick.ch/wirtschaft/schweiz-spanien-belgien-schweiz-der-lange-weg-von-der-fabrik-bis-zur-spritze-moderna-impfstoff-ist-3902-km-unterwegs-id16291583.html](https://www.blick.ch/wirtschaft/schweiz-spanien-belgien-schweiz-der-lange-weg-von-der-fabrik-bis-zur-spritze-moderna-impfstoff-ist-3902-km-unterwegs-id16291583.html)

[^69]:
     [https://newsroom.kuehne-nagel.com/kuehnenagel-invests-in-global-vaccine-distribution-network/](https://newsroom.kuehne-nagel.com/kuehnenagel-invests-in-global-vaccine-distribution-network/)

[^70]:
     [https://www.welt.de/wirtschaft/article223706206/Gerresheimer-Trilink-Va-Q-tec-Jetzt-schlaegt-die-Stunde-der-Impfstoff-Gewinner.html](https://www.welt.de/wirtschaft/article223706206/Gerresheimer-Trilink-Va-Q-tec-Jetzt-schlaegt-die-Stunde-der-Impfstoff-Gewinner.html)

[^71]:
     [https://www.cnn.com/2020/11/21/world/coronavirus-vaccine-dry-ice-intl/index.html](https://www.cnn.com/2020/11/21/world/coronavirus-vaccine-dry-ice-intl/index.html)

[^72]:
     [https://www.cganet.com/compressed-gas-industry-expects-sufficient-dry-ice-supply-for-covid-19-vaccines-in-us-canada/](https://www.cganet.com/compressed-gas-industry-expects-sufficient-dry-ice-supply-for-covid-19-vaccines-in-us-canada/)

[^73]:
     [https://www.cbs58.com/news/cheese-industry-threatened-by-covid-dry-ice-demand](https://www.cbs58.com/news/cheese-industry-threatened-by-covid-dry-ice-demand)

[^74]:
     [https://www.gasworld.com/covid-19-vaccine-dry-ice-set-for-spike-in-demand/2020109.article](https://www.gasworld.com/covid-19-vaccine-dry-ice-set-for-spike-in-demand/2020109.article)

[^75]:
     [https://simpleflying.com/boeing-aircraft-vaccine-capacity-increased/](https://simpleflying.com/boeing-aircraft-vaccine-capacity-increased/)

[^76]:
     [https://www.wsj.com/articles/united-begins-flying-pfizers-covid-19-vaccine-11606512293](https://www.wsj.com/articles/united-begins-flying-pfizers-covid-19-vaccine-11606512293)

[^77]:
     [https://www.freightwaves.com/news/faa-issues-dry-ice-alert-to-airlines-carrying-vaccine](https://www.freightwaves.com/news/faa-issues-dry-ice-alert-to-airlines-carrying-vaccine)

[^78]:
     [https://va-q-tec.com/en/technology/phase-change-materials/](https://va-q-tec.com/en/technology/phase-change-materials/)

[^79]:
     [https://www.reuters.com/article/health-coronavirus-va-q-tec-idUSKBN2841KU?taid=5fbd0e5e39486a0001899664&utm_campaign=trueAnthem:+Trending+Content&utm_medium=trueAnthem&utm_source=twitter](https://www.reuters.com/article/health-coronavirus-va-q-tec-idUSKBN2841KU?taid=5fbd0e5e39486a0001899664&utm_campaign=trueAnthem:+Trending+Content&utm_medium=trueAnthem&utm_source=twitter)

[^80]:
     [https://www.cvdvaccine.ca/files/Pfizer%20BioNTech%20COVID-19%20Vaccine%20--%20Shipping%20and%20Handling%20Guidelines.pdf](https://www.cvdvaccine.ca/files/Pfizer%20BioNTech%20COVID-19%20Vaccine%20--%20Shipping%20and%20Handling%20Guidelines.pdf)

[^81]:
     [https://controlant.com/blog/2020/controlant-now-providing-monitoring-and-supply-chain-visibility-for-pfizer-biontech-covid-19-vaccine-distribution-and-storage/](https://controlant.com/blog/2020/controlant-now-providing-monitoring-and-supply-chain-visibility-for-pfizer-biontech-covid-19-vaccine-distribution-and-storage/)

[^82]:
     [https://www.pfizer.com/products/coronavirus/manufacturing-and-distribution](https://www.pfizer.com/products/coronavirus/manufacturing-and-distribution)

[^83]:
     [https://www.mckesson.com/Our-Stories/Demystifying-the-Cold-Chain/](https://www.mckesson.com/Our-Stories/Demystifying-the-Cold-Chain/)

[^84]:
     [https://www.zdf.de/nachrichten/panorama/coronavirus-impfstoff-logistik-100.html](https://www.zdf.de/nachrichten/panorama/coronavirus-impfstoff-logistik-100.html)

[^85]:
     [https://www.schott.com/english/news/press.html?NID=com5812](https://www.schott.com/english/news/press.html?NID=com5812)

[^86]:
     [https://www.handelsblatt.com/unternehmen/industrie/verpackungshersteller-gerresheimer-will-bis-zu-eine-milliarde-impfflaeschchen-liefern/26732650.html](https://www.handelsblatt.com/unternehmen/industrie/verpackungshersteller-gerresheimer-will-bis-zu-eine-milliarde-impfflaeschchen-liefern/26732650.html)

[^87]:
     [https://www.stevanatogroup.com/en/news-events/press-releases/stevanato-group-signs-an-agreement-with-the-coalition-for-epidemic-preparedness-innovations-cepi/](https://www.stevanatogroup.com/en/news-events/press-releases/stevanato-group-signs-an-agreement-with-the-coalition-for-epidemic-preparedness-innovations-cepi/)

[^88]:
     [https://www.newyorker.com/magazine/2020/12/07/the-race-to-make-vials-for-coronavirus-vaccines](https://www.newyorker.com/magazine/2020/12/07/the-race-to-make-vials-for-coronavirus-vaccines)

[^89]:
     [https://www.corning.com/worldwide/en/about-us/news-events/news-releases/2020/05/corning-and-pfizer-announce-new-supply-agreement-for-corning-valor-glass-packaging.html](https://www.corning.com/worldwide/en/about-us/news-events/news-releases/2020/05/corning-and-pfizer-announce-new-supply-agreement-for-corning-valor-glass-packaging.html)

[^90]:
     [https://www.corning.com/worldwide/en/about-us/news-events/news-releases/2020/06/us-departments-of-defense-health-human-services-select-corning-valor-glass-packaging-to-accelerate-delivery-of-covid-19-vaccines.html](https://www.corning.com/worldwide/en/about-us/news-events/news-releases/2020/06/us-departments-of-defense-health-human-services-select-corning-valor-glass-packaging-to-accelerate-delivery-of-covid-19-vaccines.html)

[^91]:
     [https://www.corning.com/worldwide/en/about-us/news-events/news-releases/2015/06/corning-agrees-to-purchase-gerresheimers-pharmaceutical-glass-tubing-business.html](https://www.corning.com/worldwide/en/about-us/news-events/news-releases/2015/06/corning-agrees-to-purchase-gerresheimers-pharmaceutical-glass-tubing-business.html)

[^92]:
     [https://www.sio2ms.com/news/48-barda](https://www.sio2ms.com/news/48-barda)

[^93]:
     [https://www.biopharmadive.com/news/coronavirus-vaccine-vials-supply-bottleneck/578793/](https://www.biopharmadive.com/news/coronavirus-vaccine-vials-supply-bottleneck/578793/)

[^94]:
     [https://www.defense.gov/Newsroom/Releases/Release/Article/2184808/dod-awards-138-million-contract-enabling-prefilled-syringes-for-future-covid-19/source/GovDelivery/](https://www.defense.gov/Newsroom/Releases/Release/Article/2184808/dod-awards-138-million-contract-enabling-prefilled-syringes-for-future-covid-19/source/GovDelivery/)

[^95]:
     [https://apiject.com/wp-content/uploads/2020/11/APIJECT-PRESS-RELEASE-FINAL-%E2%80%93-201119-%E2%80%93-1.pdf](https://apiject.com/wp-content/uploads/2020/11/APIJECT-PRESS-RELEASE-FINAL-%E2%80%93-201119-%E2%80%93-1.pdf)

[^96]:
     [https://www.cvdvaccine.ca/product-storage-and-dry-ice](https://www.cvdvaccine.ca/product-storage-and-dry-ice)

[^97]:
     [https://coronavirus.health.ny.gov/system/files/documents/2020/12/hospital_vaccine_guidance_week1.pdf](https://coronavirus.health.ny.gov/system/files/documents/2020/12/hospital_vaccine_guidance_week1.pdf)

[^98]:
     [https://marginalrevolution.com/marginalrevolution/2021/01/the-magical-extra-doses-and-supply-chain-optimization.html](https://marginalrevolution.com/marginalrevolution/2021/01/the-magical-extra-doses-and-supply-chain-optimization.html)

[^99]:
     [https://www.supplychaindive.com/news/nitrile-glove-supply-chain-procurement-MSC-Industrial/593145/](https://www.supplychaindive.com/news/nitrile-glove-supply-chain-procurement-MSC-Industrial/593145/)

[^100]:
     [https://www.reuters.com/article/asia-rubber-idUSL4N2HE0BD](https://www.reuters.com/article/asia-rubber-idUSL4N2HE0BD)

[^101]:
     [http://showacareers.com](http://showacareers.com)

[^102]:
     [https://www.zdf.de/nachrichten/panorama/coronavirus-impfstoff-logistik-100.html](https://www.zdf.de/nachrichten/panorama/coronavirus-impfstoff-logistik-100.html)
