<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** We are using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/christianschuler8989/StudyToolkitVid">
    <img src="images/logo.png" alt="Logo" width="330" height="120">
  </a>

  <h3 align="center">StudyToolkitVid</h3>

  <p align="center">
    A toolkit for creating studies to evaluate quality of videos!
    <br />
    <a href="https://github.com/christianschuler8989/StudyToolkitVid/tree/main/docs"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/christianschuler8989/StudyToolkitVid">View Demo (TODO)</a>
    ·
    <a href="https://github.com/christianschuler8989/StudyToolkitVid/issues">Report Bug</a>
    ·
    <a href="https://github.com/christianschuler8989/StudyToolkitVid/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#datastructure">Data Structure</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Modular concept of the researchers’ toolkit _StudyToolkitVid_. From the formulated research question to the media editing to acquire test material, executing an online study and subsequently analysing the resulting data using statistical methods.

[![Product Name Screen Shot][screenshot-pipeline]](https://github.com/christianschuler8989/StudyToolkitVid)

There are many ways to edit media and investigate human perception based on great implementations available online; however, we didn't find one that really suited our needs while investigating the importance of lip synchrony, so we created this toolkit. We wanted to create a toolkit so easy and intuitive to use that it'll enable less tech-savy people to explore their scientific itches. On the other hand we try to keep it as modular as possible to enable adjustments and partial use of it.

Our reasoning:
* Everyone loves freely available and easily accessible software.
* Your time should be focused on creating something amazing while exploring different research questions and not get slowed down by rudimentary issues- trying to solve problems, already solved by others.
* You also shouldn't be doing the same tasks over and over- especially by hand
  + Creating data sets for investigating perceived quality of video material
  + Setting up and executing a user study based on these (or other) data sets
  + Running and reporting a statistical analysis following the results from a study

Of course, no one toolkit will serve all projects since your needs may be different. While our focus is especially on the needs of investigating lip synchrony in video material, we will also try to add more diverse functionalities in the future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. We appreciate all contributions and want to thank everyone who helps out in any way possible!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

List of major frameworks/libraries used to bootstrap this project:

* [PyQt](https://wiki.python.org/moin/PyQt)
  - "PyQt is one of the most popular Python bindings for the Qt cross-platform C++ framework. PyQt was developed by Riverbank Computing Limited."
  - With the use of PyQt we were able to create a pipeline that bridges the following utilities in an easy-to-use and neatly packaged toolkit.
* [WebMAUS](https://clarin.phonetik.uni-muenchen.de/BASWebServices/interface/WebMAUSBasic)
  - "This web service inputs a media file with a speech signal and a text file with a corresponding orthographic transcript, and computes a word segmentation and a phonetic segmentation and labeling."
  - The output of WebMAUS is used in <a href="#mediaEditing">Part 1 - Media Editing</a> of the StudyToolkitVid pipeline.
* [beaqlejs](https://github.com/HSU-ANT/beaqlejs)
  - "BeaqleJS (browser based evaluation of audio quality and comparative listening environment) provides a framework to create browser based listening tests and is purely based on open web standards like HTML5 and Javascript."
  - A modified version, to also enable use of video files, is used to create the studies in <a href="#statisticalAnalysis">Part 2 - Study Setup</a>.
* [R](https://www.r-project.org/)
  - "R is a free software environment for statistical computing and graphics. It compiles and runs on a wide variety of UNIX platforms, Windows and MacOS."
  - R is the foundation for the scripts used in <a href="#statisticalAnalysis">Part 3 - Statistical Analysis</a> of this toolkit.
<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running follow these simple steps.

### Prerequisites
1. You need a Python installation (tested with: 3.10.9)

* For how to install Python on Windoof refer to: [Using Python on Windows](https://docs.python.org/3.10/using/windows.html)
* For how to install Python on macOS refer to: [Using Python on a Mac](https://docs.python.org/3.10/using/mac.html)
* For how to install Python on Linux refer to: The person who introduced you to Linux, and please tell them "The Lannisters send their regards!" (or go to [Using Python on Unix platforms](https://docs.python.org/3.10/using/unix.html))

2. You need to use a terminal (at least once ;) )

For more information about how to work with a terminal, refer to [Microsoft's Guide](https://learn.microsoft.com/en-us/windows/terminal/install) for Windoof, [Apple's Guide](https://support.apple.com/de-de/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/2.12/mac/11.0) for macOS, and [Ubuntu's Guide](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview) for Linux systems.


### Installation
Create a directory for the toolkit and all your projects to be saved in.
For this description we will call it "MyAwesomeDirectory"
Then navigate into this directory and open the terminal from within it.

1. Clone this repository to get a local copy of the toolkit on your system:
Execute the following lines inside of your terminal.
   ```sh
   git clone git@github.com:christianschuler8989/StudyToolkitVid.git
   ```
2. (Optional, but recommended) Create a virtual environment for the toolkit:
   1. (If not yet installed) Install python venv:
   ```sh
   python3 -m pip install virtualenv
   ```
   2. Create an environment named "venvToolkit"
   ```sh
   python -m venv venvToolkit
   ```
   3. Activate the virtual environment every time before starting the toolkit
   ```sh
   source venvToolkit/bin/activate
   ```
3. Navigate into the cloned toolkit-directory named "StudyToolkitVid", so you end up
   ```sh
   cd StudyToolkitVid
   ```
   Assuming you cloned the repository into your "/Home/Download/" directory, you would type
   ```sh
   cd /Home/Download/MyAwesomeDirectory/StudyToolkitVid
   ```
4. Install the requirements:
   ```sh
   python -m pip install -r requirements.txt
   ```
5. Start the toolkit (continue in <a href="#usage">Usage</a> section below):
   ```sh
   python main.py --run
   ```

### Data Structure

The structure of the pipelines directories. Arrows indicate file-movement inbetween the different parts of the toolkit.
![Product Name Screen Shot][screenshot-datastructure]

Alligning with best practice standards in science, files placed in an "input" directory are only read by the toolkit, never modified directly. Any modification of data takes place inside the "temp" directories, which can then automatically be cleaned up to free space, since all results are to be found in the "output" directories. The output of one step can serve as input for the next, or be used in other ways and form, separate to the toolkit.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
<a name="usage"></a>
File naming as part of the pipeline for an automated workflow.
![Product Name Screen Shot][screenshot-naming]

In any project that works with and modifies data in any shape or form, a decision has to be made regarding the naming of files. There is a trade-off between "human-readability" and "preventing-inpractical-clutter". For example: If a media file is modified in numerous different ways and we want the name of the file to contain all applied modifications, we have to be aware of the different limits that a file name can maximally have before encountering errors.


### Part 1 - Media Editing
<a name="mediaEditing"></a>
Creating data sets for investigating perceived quality of video material.
[TODO]


### Part 2 - Study Setup
<a name="studySetup"></a>
Setting up and executing a user study based on these (or other) data sets.
[TODO]


### Part 3 - Statistical Analysis
<a name="statisticalAnalysis"></a>
Running and reporting a statistical analysis following the results from a study.
[TODO]


_For more information, please refer to the [Documentation](https://github.com/christianschuler8989/StudyToolkitVid/tree/main/docs/StudyToolkitVid_Documentation.pdf)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Finally "git-it-up"
- [ ] Media Editing
    - [x] Core Functionalities
    - [ ] Smooth Lip-Asynchrony Introduction
    - [ ] Automated Lip Recognition
    - [x] Testing
    - [ ] Beginner-Friendly UI
- [ ] Add Study Creation
    - [x] Core Functionalities
    - [ ] More User-Customization
    - [x] Testing
    - [ ] Beginner-Friendly UI
- [ ] Add Statistical Analysis
    - [ ] Core Functionalities
    - [ ] More User-Customization
    - [ ] Result Exploration
    - [ ] Automated Visualizations
    - [ ] Testing
- [x] Automated Installation/Setup
- [ ] General Testing
    - [x] Core functionalities
    - [ ] Advanced functionalities
    - [x] Different Operating Systems
        - [x] Ubuntu 22.04
        - [x] Windoof 10
        - [x] macOS Monterey 12.3
- [ ] Quality of Life
    - [x] Example Media Files
    - [ ] Tool-Tip Pop-Ups
    - [ ] Documentation
    - [x] User Guide
- [ ] Multi-Language Support
    - [x] English
    - [ ] German
    - [ ] Chinese
    - [ ] Spanish
- [ ] Expand File Format Support
    - [x] .mp4
    - [ ] Other Video Formats
    - [ ] Text (Literature & Translation Studies)
    - [ ] Image (Art & Computer Vision Studies)

Go to the [open issues](https://github.com/christianschuler8989/StudyToolkitVid/issues) section to propose new features or simply report encountered bugs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Christian Schuler - [GitHub Page](https://christianschuler8989.github.io/) - christianschuler8989(4T)gmail.com

Dominik Hauser - do_340(4T)hotmail.de

Anran Wang - [@AnranW](https://github.com/AnranW) - echowanng1996(thesymbolforemail)hotmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

A list of helpful resources we would like to give credit to:

* [The Digital and Data Literacy in Teaching Lab, who initially funded this project](https://www.isa.uni-hamburg.de/ddlitlab.html)
* [Our Mentor Prof. Dr. Timo Baumann who always believed in us](https://timobaumann.de/work/)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template) 
* [PyQt](https://wiki.python.org/moin/PyQt)
* [BAS WebService of the Bavarian Archive for Speech Signals hosted by the Institute of Phonetics and Speech Processing at the Ludwig-Maximilians-Universität, München, Germany](http://hdl.handle.net/11858/00-1779-0000-0028-421B-4)
* [S. Kraft, U. Zölzer: "BeaqleJS: HTML5 and JavaScript based Framework for the Subjective Evaluation of Audio Quality"](https://github.com/HSU-ANT/beaqlejs)
* [R](https://www.r-project.org/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/christianschuler8989/StudyToolkitVid.svg?style=for-the-badge
[contributors-url]: https://github.com/christianschuler8989/StudyToolkitVid/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/christianschuler8989/StudyToolkitVid.svg?style=for-the-badge
[forks-url]: https://github.com/christianschuler8989/StudyToolkitVid/network/members
[stars-shield]: https://img.shields.io/github/stars/christianschuler8989/StudyToolkitVid.svg?style=for-the-badge
[stars-url]: https://github.com/christianschuler8989/StudyToolkitVid/stargazers
[issues-shield]: https://img.shields.io/github/issues/christianschuler8989/StudyToolkitVid.svg?style=for-the-badge
[issues-url]: https://github.com/christianschuler8989/StudyToolkitVid/issues
[license-shield]: https://img.shields.io/github/license/christianschuler8989/StudyToolkitVid.svg?style=for-the-badge
[license-url]: https://github.com/christianschuler8989/StudyToolkitVid/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/christian-schuler-59090a177/
[screenshot-pipeline]: images/StudyToolKitVid-pipelineFlow.png
[screenshot-naming]: images/StudyToolKitVid-dataNaming.png
[screenshot-datastructure]: images/StudyToolKitVid-directoriesUse.png

