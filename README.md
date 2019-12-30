# Big data course 2019

Authors: Marc & Liubov (network theory) | Anirudh & Felix (Big data in mental health) | Loic (data management)

Marc Santolini: marc.santolini@cri-paris.org

Liubov Tupikina: liubov.tupikina@cri-paris.org

**Let us know more about you in this [form](https://forms.gle/qzUibhZVm7GEa5rP9)!**

**Let us know about your github and topics you are interested: https://docs.google.com/spreadsheets/d/1dsMScv5jodScJQ8dXe66ZbOLGK3o8-cq8KlrHdB2Nr8/edit?usp=sharing.**

This is the repository of the [CRI](https://cri-paris.org/) Digital Master "Big data" course for Fall 2019.

# Course description on network theory
(Marc, Liubov)

This course will provide an introduction to the field of big data, with a focus on network data and data for mental health. Topics will cover data project management, infrastructure of big data, data analysis and visualisation, and mental health data. The course will be divided into a big data and a network data parts.

Why focus on network data? Over the past century, network studies have had significant impact in disciplines as varied as mathematics, sociology, physics, biology, computer science or quantitative geography, giving birth to Network Science as a field of itself. With the recent rise of social networks in the last decade, their use has now become widespread in the digital world. Here we will provide an introduction to the field of Network Science,  from the theoretical foundations (generating, analysing, perturbing networks) to the practical hands-on part (analysis and visualisation of a real-world networks). 

# Evaluation of the network theory course
1. Reversed classroom topics https://docs.google.com/document/d/1fWYlafN2GUoiqX-tuVJpsXAeqlY3HqhVrY9SRSqxroM/edit?usp=sharing on 11 December 2019
2. Projects (see github folder with template of notebook) on 18 December 2019 
All projects from students are located in folders here https://github.com/Big-data-course-CRI

## Network topics of the course will cover

1.  How to construct networks from real data?
2.  How to analyze networks? (centrality measures, community detection, statistical analyses etc.)
3.  How to visualise networks? 
4.  Dynamics and spreading phenomena on networks (epidemics / information spreading, diffusion)
5.  How do networks wirings change in time? (network robustness, temporal networks)
6.  How to represent more complex network data? Multilayer, multiplex networks.

Students will select, analyse and present a network of their choice as part of a personal project for the course. They will also choose an advanced topic in network science & big data for which they will make a presentation in a reverse classroom setting. They will in particular contribute to a wikipedia page about that topic.

# Data Efforts in the Mental Health part:
(Anirudh, Felix)

In this part, students will be presented with topics related to the infrastructure of ‘big data’. They will be introduced to barriers, current trends, types, protocols and importance of ‘big data’ collection in the sphere of mental health, specifically through the
 (i) Healthy Brain Network project for 10000 children collecting and sharing neuroimaging & phenotypic data. 
Students will also contribute to the development of 
(ii) A Linked Semantic Mental Health Database and scientific framework mapping signs, symptoms and behaviors to subjective and objective measures, projects and technologies (https://github.com/ChildMindInstitute/mhdb/wiki)
(iii) MindLogger Data Collection Platform & App to dramatically improve the convenience, consistency, efficiency, accuracy & analysis of widely distributed data efforts (https://mindlogger.org/)

Students will then spend the last part of the course working on a research project developing and applying digital tools related to ‘big data’ and mental health, using the skills obtained from the first part of the course. 

# Resources

## Introductory material on networks:
(Marc, Liubov)

* Introductory interactive textbook by A-L Barabasi: http://networksciencebook.com/ 
  * Chapter 2 for network metrics
  * Chapter 9 for community detection
* An introduction to network visualisation: 
  * BASIC 
    * Gephi: http://www.martingrandjean.ch/gephi-introduction/
  * INTERMEDIATE
    * Cytoscape:  https://github.com/cytoscape/cytoscape-tutorials/wiki
  * ADVANCED
    * R: https://kateto.net/network-visualization 
    * Python: https://www.analyticsvidhya.com/blog/2018/04/introduction-to-graph-theory-network-analysis-python-codes/
    * Cytoscape.js: https://blog.js.cytoscape.org/2016/05/24/getting-started/
    * D3.js: https://www.d3-graph-gallery.com/network
    * PYthon package on statistics

* Network databases
  * Index of Complex Networks (ICON): https://icon.colorado.edu/  5,000+ networks
  * Network repository: http://networkrepository.com/ offers a lot of visualisation tools already in the website
  * On Github: 
    * Deezer Social Networks, Facebook Page-Page Networks, Wikipedia Article Networks: https://github.com/benedekrozemberczki/datasets
    * A Repository of Benchmark Graph Datasets for Graph Classification (31 Graph Datasets In Total https://github.com/shiruipan/graph_datasets
    * Repository of Network repositories: https://github.com/ComplexNetTSP/ComplexNetWiki/wiki/Networks-datasets
   * Your own!! Any dataset with two columns can be a network after all... Why not try with your favorite data? You can use API to mine your own network, for example with [Twitter](https://towardsdatascience.com/access-data-from-twitter-api-using-r-and-or-python-b8ac342d3efe) or [Youtube](https://www.pythonforbeginners.com/scripts/using-the-youtube-api/)

* For visualisations 
  * Gephi https://gephi.org/ for simple graph visualisation
  * Introduction to Gephi: http://www.martingrandjean.ch/gephi-introduction/
  * Cytoscape https://cytoscape.org/ for more fine grained visualisation. Introduction to cytoscape https://github.com/cytoscape/cytoscape-tutorials/wiki
  * D3.js for interactive visualisations: https://www.d3-graph-gallery.com/network
  * Cytoscape.js for other interactive visualisations: http://js.cytoscape.org/
  * R by following the (amazing) guide from https://kateto.net/network-visualization 
  * A paper and a pen. Sometimes it’s all that it takes: https://benfry.com/exd09/.

* For analyses 
  * R https://www.rstudio.com/ with the library iGraph (some intro here: https://kateto.net/networks-r-igraph)
  * Python https://www.python.org/ with the networkx library (https://networkx.github.io/), matplotlib, numpy, seaborn, scipy, pylab, jupiter notebook

* Other resources
  * Exploring complex systems (not just networks): http://www.complexity-explorables.org/
  * About collective phenomena and emergence: https://youtu.be/16W7c0mb-rE 
  * Presentations on network science https://github.com/Liyubov/talks-from-conferences/tree/master/teaching_networks 
  * Programming Python and collective intelligence https://resources.oreilly.com/examples/9780596529321/ 
  * Firsts in network science from Petter Holme https://petterhol.me/2019/04/15/firsts-in-network-science/
  * Analysis of city data https://www.data.gov/
  * Data for science slides and folders from B.Gonsales https://github.com/Dataforscience/networks


* Papers about network science:
https://drive.google.com/drive/u/1/folders/1RXXtMR1DMaWSm22lyqxwSDx_H07kRElt


## Big Data & Mental Health:
(Felix, Anirudh)

* Linked Semantic Mental health Database: https://github.com/ChildMindInstitute/mhdb/wiki
* MindLogger Data Collection Platform & App: https://mindlogger.org/
* Healthy Brain Network Data Collection Project:
  * https://healthybrainnetwork.org/
  * http://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/index.html

* News, Tutorials, Explorations and Data Adventures of a mental health lab: https://matter.childmind.org/blog

* Follow a Scientist - Projects and Papers :
  * https://www.binarybottle.com/projects.html
  * https://www.binarybottle.com/papers.html


## Topics and ideas for the projects 

* Internet and WWW analysis:
Data collected in 1999. Ref: Albert, R., Jeong, H., & Barabasi, A. L. (1999). 
Internet: Diameter of the world-wide web. Nature, 401(6749), 130-131
http://networkrepository.com/

* Citation and collaboration network analysis:
Leskovec, J., Kleinberg, J., & Faloutsos, C. (2007) with other data examples 
https://snap.stanford.edu/data/


* Neural networks:
Brain networks by O.Sporns 
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3811098/

* Ecological network:
Ecological networks and fragility by Montoya Sole (2000)
https://www.ncbi.nlm.nih.gov/pubmed/16855581

* Transportational networks:
Barthelemy (2011) https://journals.openedition.org/nda/2374

Collaborations with other existing projects
* Functional networks building and analysis, e.g.  pyunicorn
* Comparison of networks, e.g. project https://github.com/netsiphd/netrd

# Criteria for projects 

1. loading or collecting your own network data 
2. analyzing data from your network and answering your research projects
3. documenting your project (in README files of the project)


# How To Use Github 
https://guides.github.com/activities/hello-world/ 

To push your folder with project to existing Github repository 
https://help.github.com/en/github/using-git/pushing-commits-to-a-remote-repository
