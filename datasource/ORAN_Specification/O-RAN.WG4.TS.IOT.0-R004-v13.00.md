Technical Specification

O-RAN Fronthaul Working Group

Fronthaul Interoperability Test Specification (IOT)

Copyright © 2025 by the O-RAN ALLIANCE e.V.

The copying or incorporation into any other work of part or all of the
material available in this specification in any form without the prior
written permission of O-RAN ALLIANCE e.V. is prohibited, save that you
may print or download extracts of the material of this specification for
your personal use, or copy the material of this specification for the
purpose of sending to individual third parties for their information
provided that you acknowledge O-RAN ALLIANCE as the source of the
material and that you inform the third party that these conditions apply
to them and that they must comply with them.

O-RAN ALLIANCE e.V., Buschkauler Weg 27, 53347 Alfter, Germany

![webwxgetmsgimg
(7).jpeg](media/image1.jpeg){width="1.1936340769903762in"
height="0.5102777777777778in"}O-RAN.WG4.TS.IOT.0-R004-v13.00

# Contents  {#contents .TT}

Foreword 5

Modal verbs terminology 5

1 Scope 6

2 References 6

2.1 Normative References 6

2.2 Informative References 7

3 Definition of terms, symbols and abbreviations 7

3.1 Terms 7

3.2 Abbreviations 9

4 Fronthaul Interoperability 10

4.1 General 10

4.2 Summary of Test Scenarios 11

4.3 Future Enhancements 11

4.4 Fronthaul M-Plane Architectural options 12

4.5 Fronthaul Synchronization options 12

5 Interoperability Measurements 13

5.1 Interoperability Standard Test Definitions 13

5.1.1 Standard Test Configurations 13

5.1.2 Device Under Test (DUT) 13

5.1.3 Network Management System (NMS) 14

5.1.4 Testing Tools 15

5.1.5 Time Synchronization 18

5.1.6 Assumptions 18

5.1.7 Specifications to be used for testing 18

5.1.8 Interoperability (IOT) Test Profiles 18

5.1.9 Measurements of interest 19

5.2 Standard Test Data Configurations 19

5.3 Standard Test Execution 19

5.4 Interoperability Test Cases 19

5.5 Reporting and validation of used capabilities 20

6 M-Plane IOT Test 21

6.1 Overview 21

6.2 Start-up in hierarchical mode 21

6.2.1 Test Description and Applicability 21

6.2.2 Minimum Requirements (Prerequisites) 21

6.2.3 Test Purpose and Scope 21

6.2.4 Testability requirements imposed on O-RU and O-DU 22

6.2.5 Methodology and Initial Conditions 22

6.2.6 Procedure: M-Plane start up test 22

6.2.7 Test Requirement (expected result) 25

6.2.8 Test Report (Failure) 25

6.3 Start-up in hybrid mode 26

6.3.1 Test Description and Applicability 26

6.3.2 Minimum Requirements (Prerequisites) 26

6.3.3 Test Purpose and Scope 26

6.3.4 Testability requirements imposed on O-RU, O-DU and NMS 27

6.3.5 Methodology and Initial Conditions 27

6.3.6 Procedure: M-Plane start up test 27

6.3.7 Test Requirement (expected result) 29

6.3.8 Test Report (Failure) 29

6.3.9 Supplementary test: NETCONF Access Control (Failure) 29

7 S-Plane IOT Test 29

7.1 Overview 29

7.2 Functional test of O-DU + O-RU using ITU-T G.8275.1 profile (LLS-C1)
32

7.2.1 Test Description and Applicability 32

7.2.2 Minimum Requirements (Prerequisites) 32

7.2.3 Purpose and Scope 32

7.2.4 Testability Requirements imposed on O-RU and O-DU 32

7.2.5 Test Methodology 32

7.2.6 Test Requirements (expected results) 33

7.3 Functional test of O-DU + bridged network + O-RU using ITU-T
G.8275.1 profile (LLS-C2) 34

7.3.1 Test Description and Applicability 34

7.3.2 Minimum Requirements (Prerequisites) 34

7.3.3 Purpose and Scope 34

7.3.4 Testability Requirements imposed on O-RU and O-DU 34

7.3.5 Test Methodology 35

7.3.6 Test Requirements (expected results) 35

7.4 Functional test of O-DU + bridged network + O-RU using ITU-T
G.8275.1 profile (LLS-C3) 37

7.4.1 Test Description and Applicability 37

7.4.2 Minimum Requirements (Prerequisites) 37

7.4.3 Purpose and Scope 37

7.4.4 Testability Requirements imposed on O-RU, O-DU and bridged network
37

7.4.5 Test Methodology 37

7.4.6 Test Requirements (expected results) 38

7.5 Functional test of O-DU + O-RU using ITU-T G.8275.2 profile (LLS-C1)
39

7.6 Functional test of O-DU + bridged network + O-RU using ITU-T
G.8275.2 profile (LLS-C2) 39

7.7 Functional test of O-DU + bridged network + O-RU using ITU-T
G.8275.2 profile (LLS-C3) 39

7.8 Functional test of O-DU + bridged network + O-RU (LLS-C4) 40

7.9 Performance test of O-DU + Two O-RUs using ITU-T G.8275.1 profile
(LLS-C1) 40

7.9.1 Test Description and applicability 40

7.9.2 Minimum Requirements (Prerequisites) 40

7.9.3 Purpose and scope 40

7.9.4 Testability Requirements imposed on O-RU and O-DU 40

7.9.5 Test Methodology 40

7.9.6 Test Requirement (expected result) 41

7.10 Performance test of O-DU + bridged network + Two O-RUs using ITU-T
G.8275.1 profile (LLS-C2) 41

7.10.1 Test Description and applicability 41

7.10.2 Minimum Requirements (Prerequisites) 41

7.10.3 Purpose and Scope 41

7.10.4 Testability Requirements imposed on O-RU and O-DU 41

7.10.5 Test Methodology 42

7.10.6 Test Requirement (expected result) 42

7.11 Performance test of O-DU + bridged network + Two O-RUs using ITU-T
G.8275.1 profile (LLS-C3) 42

7.11.1 Test Description and applicability 42

7.11.2 Minimum Requirements (Prerequisites) 42

7.11.3 Purpose and scope 43

7.11.4 Testability Requirements imposed on O-RU and O-DU 43

7.11.5 Test Methodology 43

7.11.6 Test Requirement (expected result) 43

7.12 Performance test of O-DU + Two O-RUs using ITU-T G.8275.2 profile
(LLS-C1) 43

7.13 Performance test of O-DU + bridged network + Two O-RUs using ITU-T
G.8275.2 profile ((LLS-C2) 44

7.14 Performance test of O-DU + bridged network + Two O-RUs using ITU-T
G.8275.2 profile (LLS-C3) 44

7.15 Performance test of O-DU + bridged network + Two O-RUs (LLS-C4) 44

8 C/U-Plane IOT Test 44

8.1 Overview 44

8.2 Radio Layer 3 C-Plane establishment and Initial Radio U-Plane data
transfer 44

8.2.1 Test Description and Applicability 44

8.2.2 Minimum Requirements (Prerequisites) 45

8.2.3 Test Purpose and Scope 45

8.2.4 Testability requirements imposed on O-RU and O-DU 45

8.2.5 Test Methodology 46

8.2.6 Test Requirement (expected result) 46

8.3 Radio U-Plane downlink data transfer (Downlink throughput
performance) 46

8.3.1 Radio U-Plane downlink data transfer performance with one UE 46

8.3.2 Radio U-Plane downlink data transfer performance with two UEs 48

8.4 Radio U-Plane uplink data transfer (Uplink throughput performance)
50

8.4.1 Radio U-Plane uplink data transfer performance with one UE 50

8.4.2 Radio U-Plane uplink data transfer performance with two UEs 52

9 C/U-Plane Delay Management IOT Test 55

9.1 General 55

9.2 Test environment 56

9.3 Timing accuracy definition 57

9.4 Delay Management \#1, minimum fronthaul latency 57

9.4.1 Test Description and Applicability 57

9.4.2 Minimum Requirements 57

9.4.3 Test Purpose 57

9.3.4 Testability requirements imposed on O-RU and O-DU 57

9.4.5 Test Methodology 57

9.4.6 Test Requirement (expected result) 58

9.5 Delay Management \#2, maximum fronthaul latency 58

9.5.1 Test Description and Applicability 58

9.5.2 Minimum Requirements 58

9.5.3 Test Purpose 58

9.5.4 Testability requirements imposed on O-RU and O-DU 58

9.5.5 Test Methodology 59

9.5.6 Test Requirement (expected result) 59

9.6 Delay Management \#3, normal fronthaul latency 59

9.6.1 Test Description and Applicability 59

9.6.2 Minimum Requirements 59

9.6.3 Test Purpose 59

9.6.4 Testability requirements imposed on O-RU and O-DU 60

9.6.5 Test Methodology 60

9.6.6 Test Requirement (expected result) 60

9.7 Delay Management \#4, larger fronthaul latency then supported 60

9.7.1 Test Description and Applicability 60

9.7.2 Minimum Requirements 60

9.7.3 Test Purpose 61

9.7.4 Testability requirements imposed on O-RU and O-DU 61

9.7.5 Test Methodology 61

9.7.6 Test Requirement (expected result) 61

Annex A (normative): Profiles used for Interoperability Testing 62

A.1 General 62

A.2 M-Plane IOT Profile 65

A.2.1 M-Plane IOT Profile 1 Hierarchical-sudo 65

A.2.2 M-Plane IOT Profile 2 Hybrid-sudo+nms 67

A.2.3 M-Plane IOT Profile 3 Hierarchical-sudo-IPv6 69

A.2.4 M-Plane IOT Profile 4 Hybrid-sudo+nms-IPv6 72

A.3 CUS-Plane IOT Profiles 74

A.3.1 NR TDD 74

A.3.2 NR FDD 168

A.3.3 LTE FDD 183

A.3.4 LTE TDD 191

A.4 Delay Sets 195

A.4.1 NR TDD FR1 Cat-B mMIMO WDBF Delay Sets for DMRS-BF profiles 195

A.4.2 NR TDD FR1 Cat-B mMIMO CIBF Delay Sets 196

A.4.3 NR TDD FR1 Cat-B mMIMO DMRS-BF Delay Sets 198

Annex (informative): Change history/Change request (history) 199

#  

# Foreword

This Technical Specification (TS) has been produced by WG4 of the O-RAN
Alliance.

The content of the present document is subject to continuing work within
O-RAN and may change following formal O-RAN approval. Should the O-RAN
Alliance modify the contents of the present document, it will be
re-released by O-RAN with an identifying change of version date and an
increase in version number as follows:

version xx.yy.zz

where:

xx: the first digit-group is incremented for all changes of substance,
ie technical enhancements, corrections, updates, etc. (the initial
approved document will have xx=01). Always 2 digits with leading zero if
needed.

yy: the second digit-group is incremented when editorial only changes
have been incorporated in the document. Always 2 digits with leading
zero if needed.

zz: the third digit-group included only in working versions of the
document indicating incremental changes during the editing process.
External versions never include the third digit-group. Always 2 digits
with leading zero if needed.

# Modal verbs terminology

In the present document \"**shall**\", \"**shall not**\", \"should\",
\"**should not**\", \"**may**\", \"**need not**\", \"**will**\",
\"**will not**\", \"**can**\" and \"**cannot**\" are to be interpreted
as described in clause 3.2 of the O-RAN Drafting Rules (Verbal forms for
the expression of provisions).

\"**must**\" and \"**must not**\" are **NOT** allowed in O-RAN
deliverables except when used in direct citation.

# 1 Scope

The present document specifies the interoperability testing (IOT) for
O-DU and O-RU from different vendors connected using the O-RAN fronthaul
(FH) interface. It is noted however that the same content can be
utilized for the IOT for O-DU and O-RU from the same vendor connected
using the O-RAN FH interface.

A guiding principle defining the tests in the present document is that
any test shall exercise the fronthaul interface to a greater extent than
the test prerequisite so that the test is a proper test of some
fronthaul functionality or performance.

All tests focus on testing the fronthaul interface, but due to the
non-intrusive nature of the tests, system-level aspects of the O-DU and
O-RU are inevitably part of the interoperability tests too. Because of
this, it is recognized that positive test outcomes indicate successful
interoperability, but negative results may not be attributed solely to
problems in the FH interface and additional investigation may be
required.

It is also noted that additional test scenarios are required for
comprehensive testing of the FH interface functionality and performance,
these are not addressed in the present document.

In general, unless otherwise stated, the tests cover LTE (Stand-Alone),
NR Non-Stand-Alone (NSA) and NR Stand-Alone (SA). An O-DU and O-RU are
considered interoperable under a Profile Test Configuration (PTC), if
the device under test (DUT) can pass all mandatory and applicable
conditional mandatory tests using the specific Profile Test
Configuration.

The material contained within the present document is of stage 3 \[25\].

# 2 References

## 2.1 Normative References

The following documents contain provisions which, through reference in
this text, constitute provisions of the present document.

\- References are either specific (identified by date of publication,
edition number, version number, etc) or non‑specific.

\- For a specific reference, subsequent revisions do not apply.

\- For a non-specific reference, the latest version applies.

\- In the case of a reference to a 3GPP document, a non-specific
reference implicitly refers to the latest version of that document in
Release 18, or the latest 3GPP release prior to Release 18 that includes
that document. .

\- The versions of the ITU-T documents reflect their publication dates
at the time of the writing. For the most recent version, please refer to
ITU-T <https://www.itu.int/rec/T-REC-G/e>.

\[1\] Void

\[2\] O-RAN WG4 Control, User and Synchronization Specification Version
17.01, February 2025

\[3\] O-RAN WG4 Management Plane Specification Version 17.01, February
2025

\[4\] O-RAN Management Plane Yang Models Version 17.01, February 2025

\[5\] ITU-T G.8275.1, Precision time protocol telecom profile for
phase/time synchronization with full timing support from the network,
ITU, March 2020

\[6\] ITU-T G.8275.2, Precision time protocol telecom profile for
phase/time synchronization with partial timing support from the network,
ITU, March 2020

\[7\] ITU-T G.8271.1 "Network limits for time synchronization in packet
networks", ITU, March 2020

\[8\] ITU-T G.8271.2 "Network limits for time synchronization in packet
networks with partial timing support from the network", ITU, Aug 2017

\[9\] ITU-T G.8273 "Framework of phase and time clocks", March 2018

\[10\] ITU-T G.8261. "Timing and synchronization aspects in packet
networks", August 2019

\[11\] eCPRI Specification v1.0 "Common Public Radio Interface: eCPRI
Interface Specification", August 2017

\[12\] 3GPP TS 36.104, "Evolved Universal Terrestrial Radio Access
(E-UTRA); Base Station (BS) radio transmission and reception"

\[13\] 3GPP TS 38.104, "NR; Base Station (BS) radio transmission and
reception"

\[14\] 3GPP TS 36.211, "Evolved Universal Terrestrial Radio Access
(E-UTRA); Physical channels and modulation"

\[15\] 3GPP TS 38.211, "NR; Physical channels and modulation", 3GPP,
(Release 15.8.0)

\[16\] 3GPP TS 36.331, "Evolved Universal Terrestrial Radio Access
(E-UTRA); Radio Resource Control (RRC)"

\[17\] 3GPP TS 38.331, "NR; Radio Resource Control (RRC); Protocol
specification"

\[18\] 3GPP TS 36.141, "Evolved Universal Terrestrial Radio Access
(E-UTRA); Base Station (BS) conformance testing", 3GPP, (Release
15.10.0)

\[19\] 3GPP TS 38.141-2, "NR; Base Station (BS) conformance testing Part
2: Radiated conformance testing", 3GPP, (Release 15.7.0)

\[20\] 3GPP TS 23.401, "General Packet Radio Service (GPRS) enhancements
for Evolved Universal Terrestrial Radio Access Network (E-UTRAN)
access", 3GPP, (Release 15.12.0)

\[21\] 3GPP TS 23.502, "Procedures for the 5G System (5GS)", 3GPP,
(Release 15.11.0)

\[22\] 3GPP TS 37.340, "Evolved Universal Terrestrial Radio Access
(E-UTRA) and NR; Multi-connectivity", 3GPP, (Release 15.10.0)

\[23\] 3GPP TS 38.214, "NR; Physical layer procedures for data", 3GPP,
(Release 15.11.0)

\[24\] O-RAN Fronthaul Working Group, Conformance Test Specification
Version 12, February 2025

\[25\] ITU-T Recommendation I.130 "Method for the characterization of
telecommunication services supported by an ISDN and network capabilities
of an ISDN"

\[26\] 3GPP TS 38.306, "NR; User Equipment (UE) radio access
capabilities"

## 2.2 Informative References

\[i.1\] 3GPP TR 21.905: \"Vocabulary for 3GPP Specifications\"

# 3 Definition of terms, symbols and abbreviations

## 3.1 Terms

For the purposes of the present document, the terms and definitions
given in 3GPP TR 21.905 \[i.1\] and the following apply. A term defined
in the present document takes precedence over the definition of the same
term, if any, in 3GPP TR 21.905 \[i.1\].

C-Plane Control Plane: refers specifically to real-time control between
O-DU and O-RU, and should not be confused with the UE's control plane

Customized IOT Configuration A set of IOT parameters not matching any
specific IOT Profile Test Configuration that may be defined by anyone
wanting to execute an interoperability test defined in this
specification but instead using a custom set of test parameters

DL DownLink: data flow towards the radiating antenna

Delay Set Collection of timing values specific to one (or more)
beamforming methods. A Delay Set (DS) can include all or part of the
timing values of a beamforming method

eNB eNodeB (applies to LTE) \<E-UTRAN NodeB / Evolved NodeB\>

fm-pm Fault Management, Performance Management role

gNB gNodeB (applies to NR) \<Next Generation NodeB\>

IOT Profile A high-level interoperability test configuration definition
under which multiple more-detailed IOT Profile Test Configurations may
fit, allowing the grouping of test cases in broad categories

IOT Profile Test Configuration An interoperability test configuration
defined within this specification that includes detailed parameter
values that are representative of typical deployment cases, such that
the results of interoperability tests using such a configuration may
guide an understanding of the ability of a multi-vendor deployment to
interoperate

M-Plane Management Plane: refers to non-real-time management operations
between the O-DU and the O-RU

NETCONF Network Configuration Protocol. For details see RFC 6241,
"Network Configuration Protocol (NETCONF)", IETF, June 2011

NMS A Network Management System dedicated to O-RU operations

nms NMS role

NOT REQ No requirement on the O-DU or O-RU as an entry criterion for IOT
testing for a given functionality. The O-DU may support the
functionality. The O-RU may support the functionality. See Table A.1-1

NSA Non-Stand-Alone network mode that supports operation of SgNB
attached to MeNB

O-CU O-RAN Central Unit -- a logical node hosting PDCP, RRC, SDAP and
other control functions

O-DU O-RAN Distributed Unit: a logical node hosting RLC/MAC/High-PHY
layers based on a lower layer functional split. O-DU in addition hosts
an M-Plane instance

O-RU O-RAN Radio Unit \<O-RAN Radio Unit: a logical node hosting Low-PHY
layer and RF processing based on a lower layer functional split. This is
similar to 3GPP's "TRP" or "RRH" but more specific in including the
Low-PHY layer (FFT/iFFT, PRACH extraction).\>. O-RU in addition hosts
M-Plane instance

O-RU REQ The O-RU supports the functionality as an entry criterion for
IOT testing. The O-DU may support the functionality. See Table A.1-1

PLFS Physical Layer Frequency Support, as per ITU-T G.8271.1. SyncE is
one example

PTP Precision Time Protocol (PTP) is a protocol for distributing precise
time and frequency over packet networks. PTP is specified in the IEEE
Standard 1588

PDCCH Physical Downlink Control Channel applies for LTE and NR air
interface

PBCH Physical Broadcast Channel applies for LTE and NR air interface

REQ The O-DU and O-RU support the functionality as an entry criterion
for IOT testing. See Table A.1-1

SA Stand-Alone network mode that supports operation of gNB attached to a
5G Core Network

SCS OFDM Sub Carrier Spacing

SSH Secure Shell protocol for remote login

SSB Synchronization Signal Block, in 5G PBCH and synchronization signal
are packaged as a single block

sudo Super-User Do role

subordinate The term "subordinate" is used as a replacement for "slave"
and is consistent with its use in O-RAN WG4 CUS Specification \[2\].
When consensus emerges on how to eliminate the use of the term "slave"
in the referenced standards organization, that approach will be applied
to this specification

swm Software fault management role

S-Plane Synchronization Plane: Data flow for synchronization and timing
information between nodes

SyncE Synchronous Ethernet, is an ITU-T standard for computer networking
that facilitates distribution of clock signals over the Ethernet
physical layer

T-BC Telecom Boundary Clock

TLS Transport Layer Security protocol

TWAMP Two-Way Active Measurement Protocol

UDP User Datagram Protocol

UE User Equipment terminology for a mobile device in LTE and NR

UL UpLink: data flow from the UE towards the core network, that is from
the O-RU towards in the O-DU in a Fronthaul context

U-Plane User Plane: refers to IQ sample data transferred between O-DU
and O-RU

## 3.2 Abbreviations

For the purposes of the present document, the abbreviations given in
3GPP TR 21.905 \[i.1\] and the following apply. An abbreviation defined
in the present document takes precedence over the definition of the same
abbreviation, if any, in 3GPP TR 21.905 \[i.1\].

5GS 5G System, comprises the access network, core network and user
equipment

ARFCN Absolute Radio Frequency Channel Number

BFN Beamforming network

CC Component Carrier

CN Core Network

C/U-Plane C-Plane and U-Plane

DHCP Dynamic Host Configuration Protocol

DL DownLink

DS Delay Set

DUT Device Under Test

eNB eNodeB

EARFCN E-UTRA ARFCN

EVM Error Vector Magnitude

FH Fronthaul

GSCN Global Synchronization Channel Number

gNB gNodeB

MeNB Master eNB

MIMO Multiple Input Multiple Output

M-MIMO Massive MIMO

mMIMO M-MIMO

NETCONF Network Configuration Protocol

NMS Network Management System

NSA Non-Stand-Alone

O-CU O-RAN Central Unit

O-DU O-RAN Distributed Unit

O-RU O-RAN Radio Unit

OTA Over the Air

PBCH Physical Broadcast Channel

PCI Physical Cell Identity

PRTC Primary Reference Time Clock

PTC Profile Test Configuration

RF Radio Frequency

RSRP Reference Signal Received Power

SA Stand-Alone

SCS Sub Carrier Spacing

SDAP Service Data Adaptation Protocol

SgNB Secondary gNB

SSB Synchronization Signal Block

UE User Equipment

UL UpLink

U-Plane User Plane

# 4 Fronthaul Interoperability

## 4.1 General

O-RAN WG4 has specified and published the O-RAN FH interface
specifications (CUS-Plane \[2\] and M-Plane \[3\]) with the objective to
enable interoperability of O-DU and O-RU from different vendors. The aim
of the present document is to further facilitate such multi-vendor IOT
using the O-RAN FH interface by defining standard test configurations,
IOT profiles and interoperability test cases.

It shall be possible to perform interoperability testing in a
non-intrusive manner; that is, in a manner in which the network elements
under test are not required to support any functionality or mode of
operation beyond that required for normal operation in a
telecommunication network. However, making the endpoints of the FH
interface between the O-DU and O-RU visible would require definition of
new interfaces which may entail caching and transport of data.
Furthermore, and more importantly, operators require that the total
radio system functions and performs adequately when integrating O-DU and
O-RU from different vendors. Consequentially, this specification
approaches interoperability testing by means of system level testing.

FH interoperability testing by way of system test involves creation of a
stimulus in the O-DU to O-RU direction using an actual or emulated O-CU,
potentially with CN support/emulation, and measurement of the result at
the output of the O-RU in the RF domain by an actual or emulated UE
together with an RF signal/spectrum analyzer as required. Likewise, in
the reverse direction, the stimulus to probe the FH in the O-RU to O-DU
direction is provided by an actual or emulated UE and is measured at the
output of the O-DU by an actual or emulated O-CU with CN
support/emulation as required.

Inasmuch as the interoperability testing by way of system test involves
configuring and collecting results from the O-RU it shall be effected by
means of the M-Plane FH interface. For elements that fall outside of
this scope, such as the O-DU, the configuration and collection of data
and status information for testing purposes may be accomplished by NMS.

Interoperability involves testing the FH interface in terms of M-Plane,
S-Plane, C-Plane and U-Plane. Some aspects of these planes may be tested
independently. However, some tests, such as those that require the
devices to be brought into service and a call established entail
simultaneous activity across multiple planes.

The status of the test can be MANDATORY, CONDITIONAL MANDATORY or
OPTIONAL. Note that test that is MANDATORY is required to be performed
for interoperability testing. The test that is CONDIONAL MANDATORY is
only required to be performed if the specific condition(s) are met. If a
test is OPTIONAL, it does not need to be included in interoperability
testing but could be included if desired.

## 4.2 Summary of Test Scenarios

The following set of interoperability test cases are defined for the
current version of WG4 FH IOT specification.

-   FH tests focused on the M-Plane:

    -   Start-up (O-RU start-up from the power-on of O-RU to the
        availability of service)

-   FH tests focused on the S-Plane:

    -   Synchronization status detection

    -   Frequency and time error (performance)

-   FH tests focused on the C/U-Planes:

    -   Radio Layer 3 C-Plane establishment and Initial Radio U-Plane
        data transfer

    -   Radio downlink U-Plane data transfer (Downlink throughput
        performance)

    -   Radio uplink U-Plane data transfer (Uplink throughput
        performance)

-   FH tests focused on the C/U-Plane Delay Management

    -   Test with minimum, intermediate, maximum, and excess latency

## 4.3 Future Enhancements

Additional test cases are under consideration for the future versions of
the present document. A non-exhaustive list of candidate test cases for
future versions is provided below:

-   FH tests focused on the M-Plane:

    -   Software management (O-RU software update)

    -   Fault management

    -   File management

-   FH tests focused on the C/U-Plane:

    -   Beamforming (testing the actual characteristics of the
        radiated/received signals at O-RU)

    -   Compression (testing different compression methods and IQ
        bitwidth and validating expected performance)

        Note: beamforming and compression are tested as part of the IOT
        cases already specified in Clause 8 and the relevant IOT
        profiles (refer to Annex A for more details). The test cases
        above extend the capability to test the fronthaul interface in
        respect of these features.

    -   Multiple O-RUs

    -   Multiple UEs

## 4.4 Fronthaul M-Plane Architectural options

As described in the "O-RAN WG4 Management Plane Specification" \[3\],
two architectural models are supported, namely a "hierarchical" and a
"hybrid" model. As a general guideline the following apply,

1.  Hierarchical model: The O-RU is entirely managed by one O-DU (sudo)
    using a NETCONF based M-Plane interface.

2.  Hybrid model: The architecture allows one or more direct logical
    interface(s) between management system(s) (performing different
    roles, nms, fm-pm, swm, etc) and O-RU in addition to a logical
    interface between O-DU (sudo role) and the O-RU.

## 4.5 Fronthaul Synchronization options 

Various synchronization options have been specified in the O-RAN WG4
CUS-Plane Specification \[2\] (LLS-C1, LLS-C2, LLS-C3 and LLS-C4).
Depending on the specific O-RAN deployment being considered, not all of
them might be relevant. When testing the S-Plane, the System Integrator
shall identify which of the test cases are relevant depending on the
specific deployment scenarios addressed. As a general guideline the
following applies:

1.  Direct connection between O-DU and O-RU:

    LLS-C1 is generally the main sync option to be validated

    LLS-C4 may be considered as an alternative or as a complement to
    LLS-C1

```{=html}
<!-- -->
```
1.  Bridged network between O-DU and O-RU

    LLS-C2 for cases where the synchronization is delivered to the O-RU
    via the O-DU and over the bridged network. In this case the PRTC/PRC
    may be embedded in the O-DU or may be located anywhere in the
    network (connected via backhaul or FH transport).

    LLS-C3 for cases when the synchronization is distributed to the O-RU
    without involving the O-DU In this case the PRTC/PRC may be located
    anywhere in the network (connected via backhaul or FH transport) and
    may also be co-located with the O-DU.

    LLS-C4 may be considered as alternative or as a complement to
    LLS-C2/LLS-C3. LLS-C4 is not addressed in the present document.

The FH focused tests for S-Plane for the current version of this
specification covers LLS-C1, LLS-C2 and LLS-C3 using the ITU-T G.8275.1
\[5\] profile (Full Timing Support). FH focused tests for S-Plane for
LLS-C1, LLS-C2 and LLS-C3 using the ITU-T G.8275.2 \[6\] profile
(Partial Timing Support), and LLS-C4 are not addressed in the present
document.

# 5 Interoperability Measurements

1.  ## 5.1 Interoperability Standard Test Definitions

    1.  ### 5.1.1 Standard Test Configurations

Interoperability testing is performed to prove that the end-to-end
functionality between the O-DU and O-RU is as required by the O-RAN FH
CUS-Plane \[2\] and M-Plane \[3\] specifications on which these
components are based. This requires system level testing with O-DU and
O-RU as an integrated system.

### 5.1.2 Device Under Test (DUT)

The case where the O-DU and O-RU are provided by different vendors is
the focus of the present document, but the case where both are from the
same vendor is also valid.

The O-DU and O-RU, with their interconnecting FH, is considered as the
DUT. This is the same whether the O-CU and O-DU are implemented as an
aggregated node, or as disaggregated nodes.

For simplicity and without prejudice the tests in the following sections
are defined with reference to a disaggregated O-DU. However, the tests
apply equally when the O-DU is replaced by the O-DU functionality of an
aggregated O-CU/O-DU and where the Layer 2 and Layer 3 radio processing
on the network side is provided by the O-CU functionality of the
combined-node. Any differences to the test due to replacement of the
disaggregated O-DU with an aggregated O-CU/O-DU are detailed as they
arise.

The simplest test configuration involves a single O-DU and a single
O-RU. In this configuration, the O-DU and O-RU are labelled as
DUT1(O-DU) and DUT1(O-RU) respectively.

More advanced test configurations will involve defining the cardinality
between the 1...M O-DU(s) and 1...N O-RU(s) as part of the test scenario
which will determine the configuration required.

An example of such test configuration is to have a single O-DU connected
to multiple N O-RUs. In this example, the O-DU is labelled as DUT1(O-DU)
and the O-RU(s) are labelled as DUT1(O-RU) \... DUTN(O-RU) accordingly.

A second example is to have multiple M O-DUs connected to multiple N
O-RUs. In this second example, the O-DUs are labelled as DUT1(O-DU) ...
DUTM(O-DU) and the O-RU(s) are labelled as DUT1(O-RU) \... DUTN(O-RU)
accordingly. However, deployment scenarios where a single O-RU is
managed and used by more than one O-DU is not addressed in this version
of the WG4 FH IOT Specification.

External physical and or logical connection between the O-DUs and O-RUs
are to be specified in the IOT profiles (eg, number of 10/25/40GE).

The IOT profile specifies a complete DL and UL configuration to be used
for the DUT subject to IOT. An O-DU and an O-RU are considered
interoperable under a PTC if the DUT can pass all mandatory and
applicable conditional mandatory tests using the specific PTC.

![](media/image2.png){width="4.0326377952755905in"
height="3.388643919510061in"}

**Figure 5.1.2-1: The simplest DUT configuration**

### 5.1.3 Network Management System (NMS)

Network Management System (NMS) is required to support M-Plane testing
particularly in the Hybrid architecture model as the O-RU has logical
connection with the NMS \[3\]. In the hierarchical model, the NMS
manages the O-DU and the O-DU manages the O-RU respectively.

![](media/image3.png){width="4.960416666666666in"
height="2.9166666666666665in"}

**Figure 5.1.3-1: The relationship between DUT and NMS (hybrid mode
connection to O-RU shown dashed)**

External physical and or logical connection between the NMS and O-DUs
and O-RUs are to be specified in the IOT profiles (eg, number of
10/25/40GE), see Annex A for details.

### 5.1.4 Testing Tools

One of the key objectives of interoperability testing is to validate the
functionality of production grade DUTs. Hence it is important to ensure
that the DUTs are not negatively impacted with the utilization of
internal functions solely to support interoperability testing. ie, DUTs
are not expected to be testing tools when deployed in production
networks and therefore DUTs should not be used as testing tools during
interoperability tests.

Interoperability tests are performed with a set of testing tools which
are used to both apply active stimulus and as well as passive monitoring
and measurements of the DUTs.

The test is applicable to deployment scenarios where the O-CU and O-DU
are implemented as disaggregated nodes connected by an F1 interface and
scenarios where they are implemented as an aggregated node without an
accessible F1 interface.

The deployment scenario where the 4G LTE eNB is implemented as
disaggregated 4G O-CU and 4G O-DU nodes connected by a W1 interface is
not addressed in the present document.

**Active stimulus testing tools:**

-   **5G NR O-CU or O-CU emulator:** either as a disaggregated node or
    as an aggregated node with O-DUs (DUT): used to provide Layer 2 and
    Layer 3 radio processing on the network side. In case of
    disaggregated nodes, terminates the 3GPP 5G F1 interface with the
    O-DU (DUT)

    -   O-CU and O-CU emulator can be connected to either a real Core
        network or emulated Core. An emulated Core can be simpler to
        deploy for interoperability testing purposes

    -   External physical and or logical connection between the O-CU or
        O-CU emulator with the O-DU (DUT), if any, will be lab setup
        dependent either through physical or wireless medium

![](media/image4.png){width="6.609674103237095in"
height="3.178472222222222in"}

**Figure 5.1.4-1: Test setup when O-CU is disaggregated from O-DU (left)
and when O-CU is aggregated with O-DU (right).**

Figure 5.4.1-1 illustrates the test set-up for disaggregated O-CU/O-DU
and aggregated O-CU/O-DU. The beamforming network is optional, indicated
by the grey box with dashed outline; it is used for beamforming IOT
profiles.

-   **4G LTE MeNB or MeNB emulator**: used to terminate the 3GPP EN-DC
    X2 interface with the 5G NR O-CU or O-CU emulator

    -   Required when the DUTs (O-DU and O-RU) are configured to operate
        5G NR NSA option 3/3a/3x

    -   4G LTE MeNB or MeNB emulator can either have physical or logical
        connection with the Test UE or UE emulator. RF connection
        between the 4G LTE MeNB or MeNB emulator with the Test UE or UE
        emulator will be either through cabled connection or Over the
        Air (OTA)

-   **Test UEs and/or UEs emulator and optional beamforming network (for
    beamforming IOT profiles)**: used to generate stateful device
    connections and traffic to validate the O-DU and O-RU implementation
    of the O-RAN FH interface protocols as these are stimulated by the
    3GPP upper layer protocols. The beamforming network (BFN), for
    example a Butler Matrix, is used to generate a static RF channel
    with rank not lower than the number of spatial streams required for
    the beamforming IOT profiles

    -   Required so that the O-RU which is the DUT does not need to be
        put into a "test mode" which does not happen in live deployments

    -   Test UEs will require SIM cards which are pre-provisioned with
        subscriber profiles. UEs used for testing can be simpler to
        setup but given that these Test UEs are designed to be
        commercial UEs with possibly certain diagnostic functions
        enabled for logging purposes, they are limited in terms of
        configurability

    -   UEs emulator will require SIM profile configuration with the
        subscriber's profiles. UEs emulator can be used in test
        scenarios which require multiple UEs' sessions, more flexibility
        and configurability to help drive test scenarios

    -   RF connection between the Test UEs or UEs emulator with the O-RU
        (DUT) will be either through cabled connection or OTA. However,
        in case BFN is used, the RF connection between the Test UEs or
        UEs emulator and the BFN is via cable and the RF connection
        between BFN and O-RU (DUT) is also via cable. The use of OTA for
        beamforming IOT profiles is not addressed in the present
        document

**Passive monitoring and measurements testing tools:**

-   **Test UEs and/or UEs emulator**: used to produce measurements and
    logs

    -   Measurements and KPIs logs for test case validation and
        reporting

    -   Diagnostics logs for troubleshooting purposes which can help
        with test setup validation and root cause analysis for failed
        test cases

    -   Diagnostics mode is enabled on the Test UEs for diagnostic
        logging purposes. Device logging tools are connected to the Test
        UEs for logging purposes

    -   UEs used for testing can be simpler to setup but given that
        these Test UEs are designed to be commercial UEs, they are
        limited in terms of diagnostic logging capabilities due to
        limited processing and buffer space

    -   UEs emulator can be used in test scenarios which require
        extensive diagnostics capabilities

-   **Application Test Server**: An endpoint application test traffic
    emulator which can be used to generate and/terminate various traffic
    streams to or from the Test UEs/UEs emulator respectively. May
    provide one or more of these options,

    -   Stateful traffic, eg, TCP, TWAMP

    -   Stateless traffic eg, UDP

    -   Required to place traffic load on the DUT

    -   External physical and or logical connection between Application
        Test Server and O-CU/O-CU emulator is out of scope of the
        specification

-   **Test results and KPIs reporting:** which can be provided through
    one or more of these options

    -   UE logging tools which are connected to the Test UEs

    -   Device emulator reporting dashboards typically built in as part
        of the Device emulator solution

    -   External dashboard and reporting applications

-   **FH Protocol Analyzer**: used for protocol analysis of O-RAN FH
    protocols to achieve the following:

    -   Test case validation which can help with test setup validation
        and troubleshooting purposes for root cause analysis for test
        cases which fail

    -   Understanding which capabilities were used during test execution

    -   Decoding and validation of M-Plane flow sequencing prior to
        SSH/TLS secure connection establishment

    -   Monitoring traffic from the O-RAN FH typically through a tap or
        span port. Taps are typically preferred as span ports are less
        reliable but can be used if taps are not readily available in
        the test lab. Connectivity specifics (eg, number of 10/25/40GE)
        are to be specified in the IOT profiles

-   **RF Spectrum and Beam Signal Analyzer**: used for RF and Beam power
    and quality analysis for:

    -   Test case validation and troubleshooting which can help with
        test setup validation and root cause analysis for test cases
        which fail

        Eg, the Beam Signal Analyzer can be used to validate that the
        O-RUs (DUT) are in-service, configured and operating correctly,
        which in case of 5G, includes validating that the SS/PBCH blocks
        (SSB) are configured with the correct Sub Carrier Spacing (SCS),
        transmitted at the correct frequency locations (can be offset
        from the center frequency), and in case of both 4G and 5G, burst
        periods with the correct Physical Cell Identities (PCI), Beam
        Identifiers and, expected power and quality

    -   RF Spectrum and Beam Signal Analyzer performs OTA RF
        measurements and signal analysis

-   O-CU or O-CU emulator

-   MeNB or MeNB emulator

-   Core or Core emulator:

    -   Used to produce measurements and diagnostics logs for
        troubleshooting purposes which can help with test setup
        validation and root cause analysis for test cases which fail

![](media/image5.png){width="6.560123578302712in"
height="3.120138888888889in"}

**Figure 5.1.4-2: Test setup when O-CU is disaggregated from O-DU (left)
and when O-CU is aggregated with O-DU (right).**

Figure 5.4.1-2 illustrates the test set-up for disaggregated O-CU/O-DU
and aggregated O-CU/O-DU. The beamforming network is optional, indicated
by the grey box with dashed outline; it is used for beamforming IOT
profiles.

### 5.1.5 Time Synchronization

All the components including the DUTs (O-DUs and O-RUs) and the Testing
Tools are required to be synchronized to a common system time and master
time source unless otherwise stated.

Synchronization Plane (S-Plane) configuration for the DUTs is specified
in the IOT profiles (see Annex A for details).

Test tools shall be time synchronized to the master timing source with
PTP.

### 5.1.6 Assumptions

In this version of the WG4 FH IOT specifications, the following
assumptions apply

-   All wireline transport interfaces and the air interface are assumed
    to conform to ideal conditions (no impairments).

-   All wireless connection assumed to adopt 3GPP approaches for "ideal"
    RF environment for test setup.

-   O-DU and O-RU comply to the same version of the O-RAN FH interface
    specifications.

-   All elements in the interoperability test and the supporting test
    environment, where 3GPP support is relevant, comply to the same
    version of the 3GPP Specification.

-   All O-RUs involved in a test are of the same category; all A or
    all B.

### 5.1.7 Specifications to be used for testing

In this version of the WG4 FH IOT specifications, the following sets of
specifications and releases/versions shall be supported

-   O-RAN FH

    -   Control, User and Synchronization Plane Specification \[2\]

    -   Management Plane Specification \[3\]

    -   Management Plane Yang Models \[4\]

-   eCPRI

    -   eCPRI Specification V1.0 "Common Public Radio Interface: eCPRI
        Interface Specification" \[11\]

        It is important to ensure that all DUTs (O-DU and O-RU) and
        Testing Tools use compatible release/version of the O-RAN FH and
        eCPRI specifications \[11\] which in this version of the WG4 FH
        IOT Specification is ensured by use of the same version.

-   3GPP

    -   Release 15 December 2018 and later versions specifications

        It is important to ensure that all DUTs (O-DU and O-RU) and
        Testing Tools use compatible release/version of the 3GPP
        specifications, which in this version of the WG4 FH IOT
        Specification is ensured by use of the same version.

### 5.1.8 Interoperability (IOT) Test Profiles

The IOT Profiles are specified in Annex A. Under each profile, one or
more Profile Test Configurations is defined, which specify test entry
criteria (parameter values supported) on O-DU and O-RU undergoing IOT
testing. There may be cases where the precise values of parameters in an
IOT Profile Test Configuration cannot be used, perhaps due to equipment
limitations or licensing rules. For example, a tester may only be
licensed to utilize 90MHz of spectrum, for which no relevant IOT Profile
Test Configuration is defined. In such a case the tester may choose to
define a Customized IOT Configuration which will generally be similar to
a defined IOT Profile Test Configuration but with some variations in
parameter values. For example, a tester may choose to define a
Customized IOT Configuration that would fall under the
"NR-TDD-FR2-CAT-A-ABF" IOT Profile but use five 100MHz component
carriers, which is not defined in any of the IOT Profile Test
Configurations under the "NR-TDD-FR2-CAT-A-ABF" IOT Profile.

Some IOT profiles specify multiple beamforming methods, with each
beamforming method specifying different C/U-Plane timing relationships
(delay values). In such cases, allowed delay values can be specified
separately from the profile table. The allowed delay values are
specified as Delay Sets. A Delay Set (DS) is a collection of timing
values specific to one beamforming method. If a separate delay table is
specified for an IOT profile enumerating allowed Delay Sets, then the
IOT test entry criterion includes that the O-DU and O-RU both can be
configured with at least one common Delay Set for each beamforming
method specified in the IOT profile.

-   EXAMPLE 1: If an O-DU can configure DS1 and DS3 for a beamforming
    method and the O-RU supports DS2 for the same beamforming method,
    they cannot be tested together

-   EXAMPLE 2: If an O-DU can configure DS1 and DS2 for a beamforming
    method and the O-RU supports DS2 for the same beamforming method,
    they can be tested (using DS2)

-   EXAMPLE 3: If an O-DU can configure DS1 for beamforming method \#1
    and DS2 and DS3 for beamforming method \#2, and the profile
    specifies both beamforming methods to be tested, the IOT testing
    using this profile requires an O-RU which can support DS1 for
    beamforming method \#1 and either supports DS2 or DS3 (or both) for
    beamforming method \#2

Normally when reporting the result of an interoperability test, the
tester may cite only the IOT Profile Test Configuration name (along with
the relevant version of the present document containing the IOT Profile
Test Configuration definition), which can be used to understand the full
test situation by consulting Annex A. In the case of reporting the
results of an interoperability test using a Customized IOT
Configuration, the tester should also provide a complete list of
parameter values to allow a reader to understand the full test scenario.
Table A.1-2 identifies whether a particular IOT profile parameter is
modifiable or forbidden in definition of a Customized IOT Configuration.

### 5.1.9 Measurements of interest

-   Availability (eg, are the DUTs in service)

-   Accessibility (eg, can the device connect to the network)

-   Retainability (eg, can the device connection be maintained)

-   Mobility (eg, moving between two O-RUs)

-   Integrity (eg, data transfers between the device and the network)

## 5.2 Standard Test Data Configurations

The test data configurations are specified as part of the IOT profiles
in Annex A.

## 5.3 Standard Test Execution

Most interoperability tests will follow a standard execution plan
although individual tests are expected to deviate from this in some way.
By defining the standard execution plan an understanding of how tests
are arranged can be gained, thereafter examining individual tests can
reveal how deviations from the standard execution plan may be defined.

## 5.4 Interoperability Test Cases

As stated in the introduction, interoperability involves testing the FH
interface in terms of M-Plane, S-Plane, C-Plane and U-Plane. Some
aspects of these planes may be tested independently. However, some
tests, such as those that require the devices to be brought into service
and a call established entail simultaneous activity across multiple
planes

Each interoperability test provides 1) test description and
applicability, 2) the minimum requirements and prerequisites listing
required testing tools as required, 3) test purpose and scope, 4)
testability requirements imposed on the O-RU and O-DU, 5) test
methodology with procedural description as required, 6) the test
requirement and expected test result.

Failure conditions are not addressed.

The following set of IOT cases are defined in the present document.

M-Plane IOT Test

1.  Startup Installation: O-DU and O-RU getting in Service

S-Plane IOT Tests

1.  Functional test of O-DU + O-RU using ITU-T G.8275.1 profile (LLS-C1)

2.  Functional test of O-DU + bridged network + O-RU using ITU-T
    > G.8275.1 profile (LLS-C2)

3.  Functional test of O-DU + bridged network + O-RU using ITU-T
    > G.8275.1 profile (LLS-C3)

4.  Performance test of O-DU + Two O-RUs using ITU-T G.8275.1 profile
    > (LLS-C1)

5.  Performance test of O-DU + bridged network + Two O-RUs using ITU-T
    > G.8275.1 profile (LLS-C2)

6.  Performance test of O-DU + bridged network + Two O-RUs using ITU-T
    > G.8275.1 profile (LLS-C3)

C/U-Plane IOT Tests

1.  Radio Layer 3 C-Plane establishment and Initial Radio U-Plane data
    > transfer

2.  Radio U-Plane downlink data transfer (Downlink throughput
    > performance)

3.  Radio U-Plane uplink data transfer (Uplink throughput performance)

C/U-Plane Delay Management Test

1.  Test with minimum fronthaul latency

2.  Test with maximum fronthaul latency

3.  Test with a fronthaul latency value between maximum and minimum

4.  Test larger fronthaul latency then supported

## 5.5 Reporting and validation of used capabilities

Since the interoperability tests are designed to be non-intrusive in
nature, the tests may pass without invoking a certain capability
supported by O-RU and O-DU, even if the capability is indicated by the
PTC as test entry criterion. See Table A.1-1 for terminology of IOT test
entry requirements. It is possible that a subset of capabilities might
not be exercised during a test, and it may not be clear which capability
was exercised or not during a test. For C/U-plane IOT tests, the
utilization of "to be reported" capabilities associated with each PTC
shall be reported. This aids in understanding which capabilities of the
DUT were positively tested as part of the IOT tests. Furthermore, the
utilization of "to be validated" capabilities shall be validated in
C/U-plane IOT tests. "To be reported" capabilities and "to be validated"
capabilities are described for each C/U-plane IOT test and for some PTCs
in Annex A.

If the utilization of a "to be validated" capability cannot be
confirmed, then the inconclusive outcome of the test shall be documented
as a "fail". The utilization of a "to be reported" capability does not
change test outcome, ie, the result of a C/U-plane test is a "pass" if
the performance acceptance criteria are met, even if the utilization of
one or more "to be reported" capabilities are not confirmed.

How to validate a capability is outside the scope of the present
document. Examples of validation methods include analysing FH protocol
logs, DUT using the capability by design or demonstrated by DUT test
logs, inferring from the support declaration and enablement via M-plane,
etc.

NOTE: In the present document, "to be reported" capabilities and "to be
validated" capabilities are listed only for NR TDD DMRS-BF IOT profiles
and C/U-plane IOT tests.

# 6 M-Plane IOT Test 

## 6.1 Overview

The M-Plane IOT test for hierarchical mode is described in Section 6.1
and the respective test for hybrid mode is described in Section 6.2. Two
IOT profiles are defined for each mode, the first addressing IPv4 with
SSH and the second addressing IPv6 with a choice of SSH or TLS. In this
version of the specification NMS operation in hybrid mode is limited to
read-only operation.

## 6.2 Start-up in hierarchical mode

### 6.2.1 Test Description and Applicability

This test case is MANDATORY.

The DUT is composed of single O-DU and single O-RU.

Test scenario refers to Chapter 6 "Start-up" in hierarchical
architecture for M-Plane \[3\].

### 6.2.2 Minimum Requirements (Prerequisites)

Single O-DU (DUT1(O-DU)) and a single O-RU (DUT1(O-RU))

1.  Are connected through the O-RAN FH

Assumptions which are required for this test scenario

1.  DHCP server is configured for test purposes (either function served
    > by O-DU or external DHCP server with O-DU or router as relay --
    > that should have no impact on test scenario). In case of external
    > DHCP server, Configuration of DHCP server and DHCP procedures are
    > excluded from validation of IOT.

```{=html}
<!-- -->
```
1.  IPv4 and IPv6 are conditional mandatory from v07 of \[3\] and either
    > IPv4 or IPv6 transport connection for M-Plane is used in this
    > test.

2.  A combination of VLAN identity and MAC address is only used for C/U-
    > Plane connectivity.

3.  Network between O-DU and O-RU allows for connectivity between
    > actors.

4.  O-RU has account configured with sudo access privilege. O-DU knows
    > credentials of sudo account available at O-RU.

5.  Appropriate software file for O-RU is pre-installed in O-RU and
    > corresponding manifest.xml is located in O-DU. No software upgrade
    > is required during startup test sequence of O-RU for this IOT test
    > case.

Testing tools which are required for this test scenario

-   FH Protocol Analyzer monitoring traffic between O-DU and O-RU is
    used for validation of M-Plane procedural flows and contents of
    messages prior to the establishment of the SSH/TLS connection for
    M-Plane and when certain procedures do not use encryption (eg,
    loopback messages and responses of IEEE 802.1Q).

### 6.2.3 Test Purpose and Scope

Purpose of this test is to validate the startup sequence of O-RU and the
interface to DHCP server and NETCONF client in O-DU for the start-up
scenario.

The detailed steps outlined in this test case are for informational
purposes and can be useful for troubleshooting purposes in the event
that the test case fails. Procedures which are not encrypted can be
observed with the FH Protocol Analyzer for validation of the test
progress.

Notwithstanding this being an M-Plane test, correct evaluation of the
success of the M-Plane operation requires also that the fronthaul
C-Plane and U-Plane also be operational, at least in the DL direction.

### 6.2.4 Testability requirements imposed on O-RU and O-DU

The appropriate software runs on the O-RU and O-DU for the test purpose.

### 6.2.5 Methodology and Initial Conditions

1.  There is physical connectivity between O-RU and O-DU

```{=html}
<!-- -->
```
6.  O-DU is powered up and in service or running

7.  DHCP server is connected and available

8.  O-RU is powered up for this start-up test scenario

9.  The credential information (per the used M-Plane IOT profile) is
    > commonly pre-installed in O-DU and O-RU as one of test assumptions
    > in 6.2.2.

### 6.2.6 Procedure: M-Plane start up test

#### 6.2.6.1 Step: Transport layer initialization 

1.  Depending on initial condition -- either power-on to O-RU or
    > physical network connection is enabled between O-RU and O-DU.

```{=html}
<!-- -->
```
10. FH Protocol Analyzer observation: DHCP Discovery coming from O-RU's
    > MAC address

    Note: message is sent as part of VLAN scan procedure, hence it can
    be in serial sequence "VID after VID with timer in between" or in
    parallel sequence "burst to subset of VIDs, timer, another burst to
    different subset of VIDs". FH Protocol Analyzer confirms that the
    O-RU includes an appropriate option in the DHCP DISCOVER per the
    used IOT profile.

11. FH Protocol Analyzer observation: VLAN scan continues until response
    > from DHCP server is received.

12. FH Protocol Analyzer observation: O-RU continues DHCP procedure
    > using only the VID on which response from DHCP server has been
    > received.

13. FH Protocol Analyzer observation: DHCP procedure is finished by DHCP
    > Acknowledgement message sent towards O-RU. As a result of DHCP
    > procedure, O-RU obtains its own IP details plus IP per the used
    > IOT profile of corresponding NETCONF Client in O-DU.

#### 6.2.6.2 Step: RU calls home to NETCONF client (TCP connection establishment)

1.  FH Protocol Analyzer observes Call Home -- a TCP session
    > establishment initiated by O-RU towards O-DU per the used IOT
    > profile

#### 6.2.6.3 Step: SSH/TLS Secure connection establishment 

1.  SSH session/TLS connection establishment initiated by O-DU towards
    > O-RU.

#### 6.2.6.4 Step: NETCONF Capability discovery

1.  NETCONF Hello message sent by O-RU towards O-DU. The message exposes
    > capability of ietf-yang-library

```{=html}
<!-- -->
```
14. NETCONF Hello message sent by O-DU towards O-RU

15. \<rpc\>\<get\> message sent by O-DU to O-RU. The \<rpc\>\<get\> has
    > \< yang-library xlsnm =
    > "urn:ietf:params:xml:ns:yang:ietf-yang-library"\> subtree filter
    > imposed

16. \<rpc\>\<reply\> message sent by O-RU to O-DU. The message contains
    > content of leaf "yang-library" of ietf-yang-library.yang module

#### 6.2.6.5 Step: Optional provisioning of new management accounts

Note: this step is intentionally omitted as pre-provisioned O-RU is
expected for IOT (meaning: no need to perform optional step and
configure supplementary management accounts).

#### 6.2.6.6 Step: Initial process of NETCONF Subscribe for each stream

1.  NETCONF "create-subscription" RPC message(s) sent by O-DU towards
    > O-RU. Number of NETCONF subscriptions is up to O-DU.

    Note: O-DU can subscribe itself to default event stream or to
    specific streams of events. In case no subscription to default
    stream is performed, then O-DU shall subscribe itself at least to
    event streams "supervision-notification" and "alarm-notif".
    Subscription to other streams is optional, however not prohibited.

```{=html}
<!-- -->
```
17. NETCONF "create-subscription" RPC Reply messages sent by O-RU for
    > each RPC message

#### 6.2.6.7 Step: Supervision of NETCONF connection

1.  Periodic sequence of NETCONF messages:

    a.  supervision-notification sent by O-RU towards O-DU

    b.  RPC supervision-watchdog-reset sent by O-DU towards O-RU

    c.  RPC reply sent by O-RU towards O-DU

Note: in above sequence following timers shall be respected:
"supervision-notification-interval", "guard-timer-overhead" sent as
parameters in RPC supervision-watchdog-reset (O-DU -\> O-RU) and
"next-update-at" sent as parameter in RPC reply (O-RU -\> O-DU).

#### 6.2.6.8 Step: Retrieval of O-RU information and Additional configuration

1.  O-DU sends \<rpc\>\<get\>\<filter="subtree"\> to get each yang
    > module listed in ietf-yang-library.yang in O-RU, for example

    -   ietf-hardware augmented by o-ran-hardware

    -   ietf-interface augmented by o-ran-interfaces

    -   o-ran-operations

    -   o-ran-transceiver

    -   o-ran-sync

    -   o-ran-mplane-int

    -   o-ran-lbm

    -   o-ran-performance-management

    -   o-ran-delay-management

    -   o-ran-module-cap

    -   o-ran-alarm-id

    -   o-ran-fan

    -   o-ran-supervision

    -   o-ran-user mgmt

```{=html}
<!-- -->
```
18. O-RU responds with \<rpc-reply\>\<data\> for each yang module per
    > \<rpc\>\<get\>

19. O-DU sends \<rpc\>\<edit-config\> to each configurable yang module
    > for additional configuration to O-RU whenever it is necessary

20. O-RU responds with \<rpc-reply\>\<ok/\>

    Note: The configurable yang modules are o-ran-sync, o-ran-lbm,
    o-ran-operations and others (up to O-DU implementation) except
    o-ran-uplane-conf, o-ran-processing-element, ietf-interface
    augmented by o-ran-interfaces. Additional configuration of step 3
    and 4 can be examined between Chapters 6.2.6.9 and 6.2.6.10.

#### 6.2.6.9 Step: Software management

1.  O-DU sends \<rpc\>\<get\>\<filter="subtree"\> to get
    > o-ran-software-management.yang

```{=html}
<!-- -->
```
21. O-RU responds with \<rpc-reply\>\<data\> for
    > \<software-inventory\>\< software-slot\>. At least 2 slots are
    > contained in software-inventory

    Note: software update is not applied as the pre-condition that
    appropriate software file for O-RU is pre-installed in O-RU and
    corresponding manifest.xml is located in O-DU.

#### 6.2.6.10 Step: C/U-Plane transport connectivity check between O-DU and O-RU

1.  O-DU configures by \<rpc\>\<edit-config\> vlan-id for the usage of
    > C/U-Plane in ietf-interface augmented by o-ran-interfaces to O-RU.
    > O-RU responds with \<rpc-reply\>\<ok/\>

```{=html}
<!-- -->
```
22. O-DU sends loopback message to O-RU with MAC address and vlan-id
    > periodically. The O-RU MAC address and vlan-id used in LBM is same
    > as the one that set in ietf-interface augmented by
    > o-ran-interfaces.

23. O-RU sends loopback response to O-DU per received loopback message
    > respectively

#### 6.2.6.11 Step: U-Plane configuration between O-DU and O-RU

1.  O-DU sends \<rpc\>\<get\>\<user-plane-configuration\> to determine
    > the presence of following instances: multiple
    > static-low-level-\[tr\]x-endpoints, multiple \[tr\]x-arrays and
    > the relations between them. O-RU replies \<rpc-reply\>\<data\>
    > including key information on number of endpoints, band number,
    > number of arrays and polarization.

```{=html}
<!-- -->
```
24. O-DU sends \<rpc\>\<edit-config\> to create
    > low-level-\[tr\]x-endpoints, with the same name as
    > static-low-level-\[tr\]x-endpoints. The NETCONF Client is
    > responsible for assigning unique values to the \"eaxc-id\"
    > addresses of all low-level-rx-endpoint elements and
    > low-level-tx-endpoint elements, within the O-RU when operating in
    > the same direction (Tx or Rx), even when these operate across
    > different named interfaces of the O-RU. Number of instances of
    > low-level-\[tr\]x-endpoints depend on contents of selected test
    > profile, eg, for number of CCs. It may be less than number of
    > instances of static-low-level-\[tr\]x-endpoints. O-RU replies
    > \<rpc-reply\>\<ok/\>\</rpc-reply\>.

25. O-DU sends \<rpc\>\<edit-config\> to create \[tr\]x-array-carriers.
    > Number of created instances of \[tr\]x-array-carriers is
    > equivalent to number of CCs times number of arrays, where number
    > of CCs is defined by operator. Appropriate values are configured
    > to absolute-frequency-center, channel-bandwidth, gain, and so on.
    > In provided configuration the value of leaf "active" is set as
    > 'INACTIVE' (or leaf is omitted in configuration and O-RU uses its
    > default value \'INACTIVE\') for all just created
    > \[tr\]x-array-carriers. O-RU replies
    > \<rpc-reply\>\<ok/\>\</rpc-reply\>.

26. O-DU sends \<rpc\>\<edit-config\> to create processing-elements
    > related to interfaces offering access to desired endpoints. The
    > key information such as MAC address is configured according to
    > selected transport flow, eg, o-ru-mac-address, o-du-mac-address
    > and vlan-id for C/U-Plane in case of Ethernet flow. O-RU replies
    > \<rpc-reply\>\<ok/\>\</rpc-reply\>.

27. O-DU sends \<rpc\>\<edit-config\> to create
    > low-level-\[tr\]x-link(s) to make relationship between
    > low-level-\[tr\]x-endpoint(s), \[tr\]x-array-carriers and
    > processing elements belonging to transport. The number of
    > instance(s) for low-level-\[tr\]x-links is equivalent to that of
    > instance(s) of low-level-\[tr\]x-endpoints.

#### 6.2.6.12 Step: Fault Management activation

1.  O-DU sends \<rpc\>\<get\>\<filter="subtree"\> to get o-ran-fm.yang

```{=html}
<!-- -->
```
28. O-RU responds with \<rpc-reply\>\<data\> for
    > \<active-alarm-list\>\<active-alarms\>

    Note: subscription to NETCONF default event stream fulfils the
    condition to signal notification alarm-notif when O-RU detects any
    alarm.

#### 6.2.6.13 Step: Performance measurement activation (if required at start-up timing)

Note: Step for Retrieval of O-RU information may cover the configuration
of o-ran-performance-management.yang if it is required at start-up
installation timing.

#### 6.2.6.14 Step: Retrieval of O-RU state, including synchronization information, from O-RU

If O-DU already knows at the moment this step is going to be performed
(eg, from notification "synchronization-state-change"), that
"sync-state" of O-RU is 'LOCKED', O-DU may skip this step.

S-Plane has to be operational.

1.  O-DU sends \<rpc\>\<get\>\<sync\> to O-RU

```{=html}
<!-- -->
```
29. S-Plane in O-RU has been locked, sends \<rpc-reply\>\<data\>
    > \<sync-status\>\<sync-state\> LOCKED

#### 6.2.6.15 Step: Configuring the O-RU operational parameters: carrier activation

S-Plane has to be operational (sync-state != FREERUN, preferable
sync-state = LOCKED) prior to running this step

1.  O-DU sends \<rpc\>\<edit-config\> to perform activation by setting
    > the value of the parameter "active" at \[tr\]x-array-carriers to
    > "ACTIVE". O-RU sends \<rpc-reply\>\<ok/\>

```{=html}
<!-- -->
```
30. O-RU sends notification \[tr\]x-array-carriers-state-change that
    > indicates all \[tr\]x-array-carriers' names with "state" = "READY"

Note: C/U-Plane service is available at this step.

### 6.2.7 Test Requirement (expected result) 

Observe that both the O-DU and O-RU get in service successfully by
monitoring correct transmission of synchronization signals and broadcast
channel (ie, PSS/SSS and PBCH for LTE and SSB for NR).

Record downlink carrier frequency (EARFCN for LTE as specified in 3GPP
TS 36.104 \[12\] and GSCN/NR-ARFCN for NR as specified in 3GPP TS 38.104
\[13\]), cell (PCI for LTE and for NR as specified in 3GPP TS 36.211
\[14\] and TS 38.211 \[15\], respectively) and system information (MIB
for LTE and NR as specified in 3GPP TS 36.331 \[16\] and TS 38.331
\[17\], respectively). In case that beam sweeping is applied to SSB,
system information should be recorded for each of the SSB indices
detected.

The parameter values for downlink carrier frequency, cell, system
information and SSB indices are part of the radio test setup
configuration. This test is considered successful if the recorded
measurements values match up with the values which are used for the
radio test setup configuration.

### 6.2.8 Test Report (Failure) 

If the test case fails, vendor specific methods will be relied on to
assist with troubleshooting the root cause(s) which led to the failure.
The steps outlined in this test case can be used to guide the
troubleshooting process.

## 6.3 Start-up in hybrid mode

### 6.3.1 Test Description and Applicability

This test case is conditional MANDATORY. The condition is, the O-DU
supports hybrid M-Plane deployment.

The DUT is composed of single O-DU, a single O-RU and a single NMS.

Test scenario refers to Chapter 5.1.2 "M-Plane Architectural Model" and
Chapter 6 "Start-up" in hybrid architecture for M-Plane \[3\]. As per
M-Plane Chapter 5.1.2, all compliant O-RUs shall be able to support both
hierarchical and hybrid deployment. If the O-DU supports hybrid M-Plane
deployment, the testing of hybrid use case shall therefore include being
able to demonstrate that an O-RU is able to support simultaneous NETCONF
sessions to the O-DU and NMS. In order to ensure limited impacts to the
baseline hierarchical O-DU to NMS configuration management tasks, in
this test the second NETCONF client associated with "nms" user
privileges is limited to demonstrating that it is able to retrieve the
configuration and operational state from an O-RU which has been
configured by an O-DU.

### 6.3.2 Minimum Requirements (Prerequisites)

Single O-DU (DUT1(O-DU)), a single O-RU (DUT1(O-RU)) and a single NMS
(DUT1(NMS).

1.  Are connected through the O-RAN FH

Assumptions which are required for this test scenario

1.  DHCP server is configured for test purposes (either function served
    by O-DU or external DHCP server with O-DU or router as relay -- that
    should have no impact on test scenario). In case of external DHCP
    server - Configuration of DHCP server and DHCP procedures are
    excluded from validation of IOT.

```{=html}
<!-- -->
```
31. IPv4 and IPv6 are conditional mandatory from v07 of \[3\] and either
    IPv4 or IPv6 transport connection for M-Plane is used in this test.

32. A combination of VLAN identity and MAC address is used for C/U-
    Plane connectivity.

33. A common VLAN is used for M-Plane connectivity between the O-RU and
    O-DU and between the O-RU and the NMS.

34. Network between O-DU and O-RU and between NMS and O-RU allows for
    connectivity between actors.

35. An account user-name has been configured for group "nms" access
    control privileges in a previous O-DU/O-RU testing step as specified
    in sub-section 6.2.6.5.

36. O-RU has two accounts configured. One account has sudo access
    privilege with credentials used by the O-DU. The other account has
    nms access privilege and the credentials used by the NMS.

37. Appropriate software file for O-RU is pre-installed in O-RU and
    corresponding manifest.xml is located in O-DU. No software upgrade
    is required during startup test sequence of O-RU for this IOT test
    case.

38. An NMS is configured for supporting NETCONF Call Home functionality.

Testing tools which are required for this test scenario

-   FH Protocol Analyzer monitoring traffic between O-DU and O-RU and
    between NMS and O-RU is used for validation of M-Plane procedural
    flows and contents of messages prior to the establishment of the SSH
    connection for M-Plane and when certain procedures do not use
    encryption (eg, loopback messages and responses of IEEE 802.1Q).

### 6.3.3 Test Purpose and Scope

Purpose of this test is to validate the startup sequence of O-RU and the
interface to DHCP server and NETCONF clients in the O-DU and NMS for the
start-up scenario. As described in \[3\], all O-RUs supporting the
M-Plane specification shall support multiple NETCONF sessions, and hence
all compliant O-RUs shall be able to support both hierarchical and
hybrid deployment.

The detailed steps outlined in this test case are for informational
purposes and can be useful for troubleshooting purposes in the event
that the test case fails. Procedures which are not encrypted can be
observed with the FH Protocol Analyzer for validation of the test
progress.

Notwithstanding this being an M-Plane test, correct evaluation of the
success of the M-Plane operation requires also that the fronthaul
C-Plane and U-Plane also be operational, at least in the DL direction.

### 6.3.4 Testability requirements imposed on O-RU, O-DU and NMS

The appropriate software runs on the O-RU, O-DU and NMS for the test
purpose.

### 6.3.5 Methodology and Initial Conditions

1.  There is physical and or logical connectivity between O-RU and O-DU
    and between the O-RU and NMS

```{=html}
<!-- -->
```
39. O-DU and NMS are powered up and in service or running

40. DHCP server is connected and available

41. O-RU is powered up for this start-up test scenario

42. The credential information (per the used M-Plane IOT profile) is
    configured on the O-RU according to one of test assumptions listed
    in in 6.3.2.

### 6.3.6 Procedure: M-Plane start up test

#### 6.3.6.1 Step: Transport layer initialization 

1.  Depending on initial condition -- either power-on to O-RU or
    physical or logical network connection is enabled between O-RU and
    O-DU/NMS.

```{=html}
<!-- -->
```
43. FH Protocol Analyzer observation: DHCP Discovery coming from O-RU's
    MAC address

    Note: message is sent as part of VLAN scan procedure, hence it can
    be in serial sequence "VID after VID with timer in between" or in
    parallel sequence "burst to subset of VIDs, timer, another burst to
    different subset of VIDs". FH Protocol Analyzer confirms that the
    O-RU includes an appropriate in the DHCP DISCOVER per the used IOT
    profile.

44. FH Protocol Analyzer observation: VLAN scan continues until response
    from DHCP server is received.

45. FH Protocol Analyzer observation: O-RU continues DHCP procedure
    using only the VID on which response from DHCP server has been
    received.

46. FH Protocol Analyzer observation: DHCP procedure is finished by DHCP
    Acknowledgement message sent towards O-RU. As a result of DHCP
    procedure, O-RU obtains its own IP details plus IP of corresponding
    NETCONF Clients in O-DU and in NMS per used IOT profile.

#### 6.3.6.2 Step: RU calls home to discovered NETCONF client (TCP connection establishment)

1.  FH Protocol Analyzer observes Call Home -- a TCP session
    establishment initiated by O-RU towards O-DU per used IOT profile

```{=html}
<!-- -->
```
47. FH Protocol Analyzer observes Call Home -- a TCP session
    establishment initiated by O-RU towards NMS per used IOT profile

#### 6.3.6.3 Step: SSH/TLS Secure connection establishment 

1.  SSH session/TLS connection establishment initiated by O-DU towards
    O-RU using sudo account privilege.

```{=html}
<!-- -->
```
48. SSH session/TLS connection establishment initiated by NMS towards
    O-RU using nms account privilege.

#### 6.3.6.4 Step: NETCONF Capability discovery

1.  NETCONF Hello message sent by O-RU towards NETCONF clients (O-DU and
    NMS). The message exposes capability of ietf-yang-library

```{=html}
<!-- -->
```
49. NETCONF Hello message sent by NETCONF clients (O-DU and NMS) towards
    O-RU.

50. \<rpc\>\<get\> message sent by NETCONF clients (O-DU and NMS) to
    O-RU. The \<rpc\>\<get\> has \<yang-library xlsnm =
    "urn:ietf:params:xml:ns:yang:ietf-yang-library"\> subtree filter
    imposed

51. \<rpc\>\<reply\> message sent by O-RU to NETCONF Clients (O-DU and
    NMS). The message contains content of leaf "yang-library" of
    ietf-yang-library.yang module

#### 6.3.6.5 Step: Optional provisioning of new management accounts

Note: this step is intentionally omitted as pre-provisioned O-RU is
expected for IOT (meaning: no need to perform optional step and
configure supplementary management accounts).

#### 6.3.6.6 Step: Initial process of NETCONF Subscribe for each stream

1.  NETCONF "create-subscription" RPC message(s) sent by O-DU towards
    O-RU. Number of NETCONF subscriptions is up to O-DU.

    Note: O-DU can subscribe itself to default event stream or to
    specific streams of events. In case no subscription to default
    stream is performed, then O-DU shall subscribe itself at least to
    event streams "supervision-notification" and "alarm-notif".
    Subscription to other streams is optional, however not prohibited.

```{=html}
<!-- -->
```
52. NETCONF "create-subscription" RPC Reply messages sent by O-RU for
    each RPC message

Note: subsequent steps use the NMS to retrieve the configuration and
operational state of the O-RU and are performed after step 6.2.6.7
through 6.2.6.15 that complete O-RU start-up.

#### 6.3.6.7 Step: NMS retrieval of O-RU information and Additional configuration

1.  NMS sends \<rpc\>\<get\>\<filter="subtree"\> to get each yang module
    listed in ietf-yang-library.yang in O-RU, with the exception of
    o-ran-usermgmt and o-ran-supervision, for example

    ietf-hardware augmented by o-ran-hardware

    ietf-interface augmented by o-ran-interfaces

    o-ran-operations

    o-ran-transceiver

    o-ran-sync

    o-ran-mplane-int

    o-ran-lbm

    o-ran-performance-management

    o-ran-delay-management

    o-ran-module-cap

    o-ran-uplane-conf

    o-ran-alarm-id

    o-ran-fan

```{=html}
<!-- -->
```
53. O-RU responds with \<rpc-reply\>\<data\> for each yang module per
    \<rpc\>\<get\>

### 6.3.7 Test Requirement (expected result) 

Observe that the O-RU calls home to both the O-DU and NMS and then is
able to establish simultaneous NETCONF sessions between the O-RU and
O-DU and between the O-RU and NMS.

Observe that the NMS is able to retrieve configuration and operational
state from models to which it does have NACM read privileges.

### 6.3.8 Test Report (Failure) 

If the test case fails, vendor specific methods will be relied on to
assist with troubleshooting the root cause(s) which led to the failure.
The steps outlined in this test case can be used to guide the
troubleshooting process.

### 6.3.9 Supplementary test: NETCONF Access Control (Failure) 

This is a supplementary test to verify correct handling of NMS read
attempt with incorrect privilege per 6.2.6.8.

1.  The NETCONF client in the NMS attempts to read user accounts
    provisioned on the O-RU. The NMS sends
    \<rpc\>\<get\>\<filter="subtree"\> to get the configuration and
    operational state for the o-ran-usermgmt yang module.

```{=html}
<!-- -->
```
54. O-RU responds with \<rpc-error\> response with "access-denied".

Expected result is to that an O-RU will deny access to an NMS that tries
to read configuration and/or operational state from models to which it
does not have NACM privileges.

If the test case fails, that is access is granted, vendor specific
methods will be relied on to assist with troubleshooting the root
cause(s) which led to the failure.

# 7 S-Plane IOT Test

## 7.1 Overview

This Section describes system level tests that are used to validate both
S-Plane functionality and S-Plane performance between O-DU and O-RU from
different vendors connected using the O-RAN WG4 FH interface specified
in \[2\] and the O-RAN WG4 M-Plane interface specified in \[3\].

S-Plane functionality is determined by retrieval of the O-DU and O-RU
synchronization state using the M-Plane or NMS as appropriate, whereas,
S-Plane performance is determined by over-the-air (OTA) measurements or
conductive (ie, a cabled electrical connection to the DUT's radio
interface) measurements of O-RU synchronization signal.

This Section provides a common high-level list of the items that are
expected to be covered in order to validate interoperability with the
relevant standard, both functional and performance aspects are
addressed:

-   The tests apply to both 4G(LTE) and 5G(NR) and are applicable to all
    O-RAN IOT profiles listed in Annex A

-   The O-RAN WG4 CUS Specification \[2\] Section validated is §11.3.2

-   SyncE Master test case is optional and only valid when the SyncE
    clock (eg, Implemented in the O-RU) takes advantage of it.
    Therefore, the related SyncE Master test cases are optional

-   Several test cases involve configuring the O-DU or O-RU

-   M-Plane connection is established, meaning whole protocol stack
    ETH/IP/TCP/SSH/TLS is up and running, Capabilities are exchanged
    between NETCONF Client and Server, Subscriptions to notifications
    are created

    -   Several test cases involve the configuration and collection of
        status of T-BC. However, as this is not specified in the
        Management Plane Specification \[3\], the parts of the tests
        below that require such functionality are not addressed in the
        present document.

    -   Further work needs to be done to align and refine the definition
        of the states in the O-RAN WG4 CUS Specification \[2\] and
        M-Plane \[3\] specifications for the next releases

At least one of the synchronization options (LLS-C1, LLS-C2, LLS-C3 or
LLS-C4), depending on the relevant O-RAN deployment as described in
Clause 4.5, shall be tested for functionality and performance.

The following bulleted notes apply specifically to S-Plane IOT
functional tests in addition to the general notes above,

-   Tests shall be done in the lab at constant temperature

-   Test equipment is needed to generate a reference S-Plane signal

-   For validation of synchronization information, use the FH M-Plane
    interface for the O-RU, and other interfaces such as NMS for O-DU

-   Retrieving sync-state of O-DU using the NMS is not addressed in the
    present document

-   O-RU reports over M-Plane the degraded received clock-class and
    clock-accuracy as well as locked state; details of how to do this
    are not addressed in the present document

-   With the exception of lls-C1, that doesn\'t include any T-BC in the
    fronthaul link, the test configuration shall use from 1 up to the
    maximum number of T-BCs specified for performance test, as set out
    in the performance test specific notes set out below, according to
    the preference of the tester

The following bulleted notes apply specifically to S-Plane IOT
performance tests in addition to the general notes above,

-   All tests should be done in lab under constant and variable
    C/U-Plane profile. The variable C/U-Plane profile (for example
    similar to the test case 13 shown in figure VI.11 of ITU-T G.8261
    \[10\]) should be defined for this test

-   A previous version of the present document (v 1.00) contained a
    requirement to perform the IOT performance tests under variable
    temperature conditions. That requirement was removed, and instead
    replaced with the following text that was also used in the
    Conformance Test Specification \[24\]: The thermal profile is not
    defined. The tests are defined to be run at a constant temperature,
    but the thermal profile choice and range is left as a decision for
    the vendor

-   Use the maximum number of T-BC devices as shown in O-RAN WG4 CUS
    Specification \[2\] in Annex H

    Note: Annex H includes example deployment cases that capture the
    influence of factors including, target end-to-end timing error
    requirement, clock type used in the network, and characteristics of
    the O-RU clock. Additional cases including, addressing O-RUs with
    different levels of clock performance, and different noise
    accumulation models etc are not addressed in the present document

-   The acceptance criterion for the tests is to satisfy the 3GPP OTA
    TAE limits specified in 3GPP TS 36.141 \[18\] for 4G(LTE) and
    38.141-2 \[19\] for 5G(NR), and summarized in eCPRI \[11\] and ITU-T
    G.8271 \[7\]. The particular conditions applicable to each test are
    set out in the relevant sections below

To perform the IOT S-Pane tests, following test set ups (Figure 7.1-1,
7.1-2 and 7.1-3) are proposed. The selection of the test setup is
dependent on the configuration mode lls-C1, lls-C2, or lls-C3. This
version of the document does not cover lls-C4:

-   Each diagram covers both functional test and performance test of the
    respective synchronization configuration mode. The main difference
    between the setups for functional and performance test is the need
    for a measurement equipment at the radio interface for performance
    test as indicated in previous paragraphs.

-   Each setup gives the option to select different types of S-Plane
    signals for the input of the O-DU. The selection of the option
    depends on the capability of the O-DU and operator's synchronization
    architecture. In lls-C3 mode, the O-DU has the option of selecting a
    master through its fronthaul interface or directly connecting to a
    T-GM.

-   T-GM via a midhaul network (for ls-C1 or lls-C2) or a fronthaul
    network (for lls-C3) over an Ethernet interface with PTP and SyncE
    (if applicable)

-   T-GM over an Ethernet interface with PTP and SyncE (if applicable)

-   PRTC: 1pps according to ITU-T G.703, 10MHz, and ToD according to
    G.8271 Annex A or any other proprietary ToD decoding specification
    supported by the O-DU

-   GNSS: RF input directly from an antenna used for GNSS signal
    reception

-   The measurement equipment has to be synchronized with the DUT, thus
    the need for a line arriving at the measurement equipment.

-   The arrows in these diagrams represent the direction of S-Plane
    messages (from master to subordinate), or from any source
    synchronization signal to the receiver.

![](media/image6.png){width="4.329834864391951in"
height="1.6539206036745406in"}

**Figure 7.1-1: Test setup for lls-C1**

> ![](media/image7.png){width="4.237853237095363in"
> height="1.579851268591426in"}

Figure 7.1-2: Test setup for lls-C2

![](media/image8.png){width="4.426349518810149in"
height="1.6501224846894138in"}

Figure 7.1-3: Test setup for lls-C3

## 7.2 Functional test of O-DU + O-RU using ITU-T G.8275.1 profile (LLS-C1)

### 7.2.1 Test Description and Applicability

This test case is CONDITIONAL MANDATORY and shall be performed if the
O-RU and O-DU declare support of LLS-C1 synchronization option (see
Clause 4.4).

This test validates that O-RU is synchronizing from an O-DU that
incorporates a PTP grand master and SyncE Master with ITU-T G.8275.1
\[5\] profile and is traceable to a PRTC.

This test involves one O-DU and one O-RU.

### 7.2.2 Minimum Requirements (Prerequisites)

1.  O-RU is connected to O-DU via direct fiber O-RAN links.

```{=html}
<!-- -->
```
55. The O-DU is connected to a PRTC traceable time source, directly
    > (GNSS Receiver either embedded or connected to the O-DU) or via
    > PTP, as described in Conformance Test Specification \[24\].

### 7.2.3 Purpose and Scope 

The O-RU is synchronizing from the O-DU with the ITU-T G.8275.1 \[5\]
profile. This test case validates the correct synchronization status of
the O-RU.

### 7.2.4 Testability Requirements imposed on O-RU and O-DU 

Requirements for M-Plane: is properly operating (as specified in 6.2).

Synchronization requirement: O-DU is connected to a local or remote
PRTC.

### 7.2.5 Test Methodology

These tests use the O-RAN M-Plane and O-DU NMS features.

The O-DU acts as a PTP master compliant with the ITU-T G.8275.1 \[5\]
profile.

Three conditions shall be covered:

-   startup

-   nominal

-   degraded

#### 7.2.5.1 Procedure: Startup conditions

1.  Not yet configured.

    External frequency and time source are available to the O-DU and
    deliver nominal status

    O-DU is not yet configured to select the time source and align its
    frequency and time to it

    O-DU not yet configured to act as PTP master on the FH ports

2.  Configured.

    O-DU is configured to align to the selected frequency and time
    source

3.  Until disciplining

    Until O-DU disciplining of the frequency and time to the selected
    source has completed, Startup conditions persists

    The O-RUs are configured to synchronize from PTP in ITU-T G.8275.1
    \[5\] profile and report their status

#### 7.2.5.2 Procedure: Nominal conditions

1.  O-DU is configured to start acting as a PTP master compliant with
    > the ITU-T G.8275.1 \[5\] profile on selected FH ports.

```{=html}
<!-- -->
```
56. O-DU acts as a PTP grand master or as a boundary clock with ports
    > towards the FH interface in Master state, compliant with the ITU-T
    > G.8275.1 \[5\] profile advertising "nominal" status.

57. O-DU reports status, acting as PTP master clock towards the FH
    > interface.

#### 7.2.5.3 Procedure: Degraded conditions

1.  O-DU is configured to enter HOLDOVER based on local oscillator
    > frequency.

```{=html}
<!-- -->
```
58. O-DU acts as configured clock, with PTP ports in master state,
    > compliant to ITU-T G.8275.1 profile advertising HOLDOVER status
    > with degraded clockClass and clockAccuracy as specified by ITU-T
    > G.8275.1 \[5\].

59. O-DU is configured to exit HOLDOVER and resumes normal frequency and
    > phase disciplining using the source.

60. O-DU acts as configured clock, with PTP ports towards the FH
    > interface in master state compliant to ITU-T G.8275.1 \[5\] in
    > "nominal" status.

### 7.2.6 Test Requirements (expected results) 

#### 7.2.6.1 Startup conditions

The acceptance criterion is that the following status is observed for
steps 1 to 3 (7.2.5.1 above):

-   the FREERUN sync-state of the O-RU using the M-Plane

-   the UNLOCKED PTP lock-state of the O-RU using the M-Plane

-   the UNLOCKED SyncE lock-state of the O-RU using the M-Plane
    (optional)

-   the FREERUN sync-state of the O-DU using the NMS

#### 7.2.6.2 Nominal conditions

The acceptance criterion is that the following status is observed for
steps 1 to 3 (7.2.5.2 above):

-   the LOCKED sync-state of the O-DU using the NMS

-   the received PTP clockClass level of the O-RU using the M-Plane

-   the received SyncE SSM level of the O-RU using the M-Plane
    (optional)

-   the LOCKED sync-state of the O-RU using the M-Plane

-   the LOCKED PTP lock-state and PARENT PTP state of the O-RU using the
    M-Plane

-   the LOCKED SyncE lock-state and OK or PARENT SyncE state of the O-RU
    using the M-Plane (optional)

#### 7.2.6.3 Degraded conditions

The acceptance criterion is that the following status is observed for
all steps 1 to 2 (7.2.5.3 above) (for steps 3 and 4, same criterion as
"Nominal conditions" apply):

-   the HOLDOVER sync-state of the O-DU using the NMS

-   the received PTP clockClass level of the O-RU using the M-Plane

-   the received SyncE SSM level of the O-RU using the M-Plane
    (optional). Note that if SyncE state is NOK, it is also permitted
    that the local default SSM level is reported using the M-Plane.

-   the sync-state of the O-RU using the M-Plane is LOCKED if the
    received clockClass (or optional SSM QL) value matches the
    configured list of accepted values, otherwise HOLDOVER or FREERUN

-   the PTP lock-state of the O-RU using the M-Plane is LOCKED,\
    and the PTP state of the O-RU using the M-Plane is PARENT if the
    received clockClass matches the configured list of accepted values,
    otherwise NOK.

-   the SyncE lock-state (optional) of the O-RU using the M-Plane is
    LOCKED or OK,\
    and the SyncE state of the O-RU using the M-Plane is PARENT or OK if
    the received SSM matches the configured list of accepted values,
    otherwise NOK.

Note: If the NETCONF client triggers a reset procedure of the O-RU by
FREERUN of the sync-state at these degraded conditions, the status
observation using M-plane is not available for NETCONF client. It is
observed that the alarm-notification is sent from the O-RU using M-Plane
and the regular start-up procedures is performed.

## 7.3 Functional test of O-DU + bridged network + O-RU using ITU-T G.8275.1 profile (LLS-C2) 

### 7.3.1 Test Description and Applicability

This test case is CONDITIONAL MANDATORY and shall be performed if the
O-RU and O-DU declare support of LLS-C2 synchronization option (see
Clause 4.5).

This test validates that O-RU is synchronizing from an O-DU via a chain
of T-BC using ITU-T G.8275.1 \[5\] profile.

This test involves one O-DU, one O-RU and multiple T-BCs.

The configuration, management, and retrieval of status of the T-BC are
not addressed in the present document.

### 7.3.2 Minimum Requirements (Prerequisites)

1.  O-RU is connected to O-DU via a chain of T-BCs.

```{=html}
<!-- -->
```
61. The T-BCs are class B. The subordinate port of the first T-BC is
    > connected to O-DU. The master clock of the last T-BC is connected
    > to the O-RU.

62. The O-DU is connected to a PRTC traceable time source, directly
    > (GNSS Receiver connected to the O-DU) or via PTP.

### 7.3.3 Purpose and Scope 

The O-RU is synchronizing from the O-DU with the ITU-T G.8275.1 \[5\]
profile over a bridged network that can deploy several T-BCs. This test
case validates the correct synchronization status of the O-RU.

### 7.3.4 Testability Requirements imposed on O-RU and O-DU 

Requirements for M-Plane: is properly operating (as specified in 6.2).

Synchronization requirement: O-DU is connected to a local PRTC/source
traceable to PRTC.

### 7.3.5 Test Methodology

These tests use the O-RAN M-Plane and O-DU NMS features.

Three conditions shall be covered:

-   startup

-   nominal

-   degraded

#### 7.3.5.1 Procedure: Startup conditions

1.  Not yet configured.

    External frequency and time source are available to the O-DU and
    deliver nominal status.

    O-DU is not yet configured to select the time source and align its
    frequency and time to it.

    O-DU not yet configured to act as PTP master on the FH ports.

```{=html}
<!-- -->
```
63. Configured.

    O-DU is configured to align to the selected frequency and time
    source.

64. Until disciplining

    Until O-DU disciplining of the frequency and time to the selected
    source has completed, Startup conditions persists.

    The O-RUs are configured to synchronize from PTP in ITU-T G.8275.1
    \[5\] profile and report their status.

#### 7.3.5.2 Procedure: Nominal conditions

1.  O-DU is configured to start acting as a PTP master compliant with
    > the ITU-T G.8275.1 \[5\] profile on selected FH ports.

```{=html}
<!-- -->
```
65. O-DU acts as a PTP grand master or as a boundary clock with ports
    > towards the FH interface in Master state, compliant with the ITU-T
    > G.8275.1 \[5\] profile advertising "nominal" status.

66. O-DU reports status, acting as PTP master clock towards the FH
    > interface.

#### 7.3.5.3 Procedure: Degraded conditions

1.  O-DU is configured to enter HOLDOVER based on local oscillator
    > frequency.

```{=html}
<!-- -->
```
67. O-DU acts as configured clock, with PTP ports in master state,
    > compliant to ITU-T G.8275.1 profile advertising HOLDOVER status
    > with degraded clockClass and clockAccuracy as specified by ITU-T
    > G.8275.1 \[5\].

68. O-DU is configured to exit HOLDOVER and resumes normal frequency and
    > phase disciplining using the source.

69. O-DU acts as configured clock, with PTP ports towards the FH
    > interface in master state compliant to ITU-T G.8275.1 \[5\] in
    > "nominal" status.

### 7.3.6 Test Requirements (expected results) 

#### 7.3.6.1 Startup conditions

The acceptance criterion is that the following status is observed for
steps 1 to 3 (7.4.5.1 above):

-   the FREERUN sync-state of the O-DU using the NMS

-   the FREERUN sync-state of the O-RU using the M-Plane

-   the UNLOCKED PTP lock-state of the O-RU using the M-Plane

-   the UNLOCKED SyncE lock-state of the O-RU using the M-Plane
    (optional)

#### 7.3.6.2 Nominal conditions

The acceptance criterion is that the following status is observed for
steps 1 to 3 (7.4.5.2 above):

-   the LOCKED sync state of the O-DU using the NMS

-   the LOCKED PTP lock-state of the O-DU using the NMS

-   the "Master Enabled" SyncE status of the O-DU using the NMS
    (optional)

-   the received PTP clockClass level of the O-RU using the M-Plane

-   the received SyncE SSM level of the O-RU using the M-Plane
    (optional)

-   the LOCKED sync-state of the O-RU using the M-Plane

-   the LOCKED PTP lock-state and PARENT PTP state of the O-RU using the
    M-Plane

-   the LOCKED SyncE lock-state and OK or PARENT SyncE state of the O-RU
    using the M-Plane (optional)

-   the synchronization status of the deployed T-BC using the respective
    NMS

#### 7.3.6.3 Degraded conditions

The acceptance criterion is that the following status is observed for
all steps 1 to 2 (7.4.5.3 above) (for steps 3 and 4, same acceptance
criterion as "Nominal conditions" apply)

-   the HOLDOVER sync-state of the O-DU using the NMS

-   the received PTP clockClass level of the O-RU using the M-Plane

-   the received SyncE SSM level of the O-RU using the M-Plane
    (optional). Note that if SyncE state is NOK, it is also permitted
    that the local default SSM level is reported using the M-Plane.

-   the sync-state of the O-RU using the M-Plane is LOCKED if the
    received clockClass (or optional SSM QL) value matches the
    configured list of accepted values, otherwise HOLDOVER or FREERUN

-   the PTP lock-state of the O-RU using the M-Plane is LOCKED,\
    and the PTP state of the O-RU using the M-Plane is PARENT or OK if
    the received SSM matches the configured list of accepted values,
    otherwise NOK

-   the SyncE lock-state (optional) of the O-RU using the M-Plane is
    LOCKED or OK,\
    and the SyncE state of the O-RU using the M-Plane is PARENT or OK if
    the received SSM matches the configured list of accepted values,
    otherwise NOK

Note: If the NETCONF client triggers a reset procedure of the O-RU by
FREERUN of the sync-state at these degraded conditions, the status
observation using M-plane is not available for NETCONF client. It is
observed that the alarm-notification is sent from the O-RU using M-Plane
and the regular start-up procedures is performed.

## 7.4 Functional test of O-DU + bridged network + O-RU using ITU-T G.8275.1 profile (LLS-C3)

### 7.4.1 Test Description and Applicability

This test case is CONDITIONAL MANDATORY and shall be performed if the
O-RU and O-DU declare support of LLS-C3 synchronization option (see
Clause 4.5).

This test validates that both the O-DU and O-RU are synchronizing from a
common PRTC via a chain of T-BCs using ITU-T G.8275.1 \[5\] profile.

This test involves one O-DU, one O-RU, a PRTC/T-GM and multiple T-BCs.

The configuration, management, and retrieval of status of the T-BC are
not addressed in the present document.

### 7.4.2 Minimum Requirements (Prerequisites)

1.  Both O-RU and O-DU are connected to a common PRTC via a chain of
    > T-BCs that are either directly connected to a PRTC/T-GM in the FH
    > network or are connected to another T-BC that is traceable to a
    > PRTC.

```{=html}
<!-- -->
```
70. The T-BCs are class B. The subordinate port of the first T-BC is
    > connected to a PRTC/T-GM. The O-DU and O-RU are connected to
    > master ports of either the same T-BC or different ones.

### 7.4.3 Purpose and Scope 

Both O-DU and O-RU are synchronized via a chain of T-BC from a common
PRTC/T-GM located in the FH networks using ITU-T G.8275.1 \[5\] profile.
This test case validates the correct synchronization status of the O-RU
and O-DU.

### 7.4.4 Testability Requirements imposed on O-RU, O-DU and bridged network

Requirements for M-Plane: is properly operating (as specified in 6.2)

Synchronization requirement: The T-BC is connected to a local PRTC or to
another T-BC that is traceable to a PRTC.

### 7.4.5 Test Methodology

These tests use the O-RAN M-Plane and O-DU NMS features.

Three conditions shall be covered:

-   startup

-   nominal

-   degraded

#### 7.4.5.1 Procedure: Startup conditions

1.  Not yet configured.

    External frequency and time source are available to the PRTC/T-GM
    and deliver nominal status.

    PRTC/T-GM is not yet configured to select the time source and align
    its frequency and time to it.

    PRTC/T-GM not yet configured to act as PTP master on the FH ports.

```{=html}
<!-- -->
```
4.  Configured.

    PRTC/T-GM is configured (eg, via proprietary) interface to align to
    the selected frequency and time source.

```{=html}
<!-- -->
```
71. Until disciplining

    Until PRTC/T-GM disciplining of the frequency and time to the
    selected source has completed, Startup conditions persists.

    The O-RUs are configured to synchronize from PTP in ITU-T G.8275.1
    \[5\] profile and report their status.

#### 7.4.5.2 Procedure: Nominal conditions

1.  PRTC/T-GM is configured to start acting as a PTP master compliant
    > with the ITU-T G.8275.1 \[5\] profile on selected FH ports.

```{=html}
<!-- -->
```
72. PRTC/T-GM acts as a PTP grand master towards the FH interface in
    > Master state, compliant with the ITU-T G.8275.1 \[5\] profile
    > advertising "nominal" status.

73. PRTC/T-GM reports status, acting as PTP master clock towards the FH
    > interface.

#### 7.4.5.3 Procedure: Degraded conditions

1.  PRTC/T-GM is configured to enter HOLDOVER based on local oscillator
    > frequency.

```{=html}
<!-- -->
```
74. PRTC/T-GM acts as configured clock, with PTP ports in master state,
    > compliant to ITU-T G.8275.1 profile advertising HOLDOVER status
    > with degraded clockClass and clockAccuracy as specified by ITU-T
    > G.8275.1 \[5\].

75. PRTC/T-GM is configured to exit HOLDOVER and resumes normal
    > frequency and phase disciplining using the source.

76. PRTC/T-GM acts as configured clock, with PTP ports towards the FH
    > interface in master state compliant to ITU-T G.8275.1 \[5\] in
    > "nominal" status.

### 7.4.6 Test Requirements (expected results) 

#### 7.4.6.1 Startup conditions

The validation is done by checking the correct synchronization state is
observed for steps 1 to 3 (7.4.6.1 above):

-   the FREERUN sync-state of the O-DU using the NMS

-   the UNLOCKED PTP lock-state of the O-DU using the NMS

-   the UNLOCKED SyncE lock-state of the O-DU using the NMS (optional)

-   the FREERUN sync-state of the O-RU using the M-Plane

-   the UNLOCKED PTP lock-state of the O-RU using the M-Plane

-   the UNLOCKED SyncE lock-state of the O-RU using the M-Plane
    (optional)

-   the synchronization status of the deployed T-BC using the respective
    NMS

#### 7.4.6.2 Nominal conditions

The validation is done by checking the correct synchronization state is
observed for steps 1 to 3 (7.4.6.2 above):

-   the LOCKED sync-state of the O-DU using the NMS

-   the LOCKED PTP lock-state of the O-DU using the NMS

-   the "Master Enabled" SyncE status of the O-DU using the NMS
    (optional)

-   the received PTP clockClass level of the O-RU using the M-Plane

-   the received SyncE SSM level of the O-RU using the M-Plane
    (optional).

-   the LOCKED sync-state of the O-RU using the M-Plane

-   the LOCKED PTP lock-state and PARENT PTP state of the O-RU using the
    M-Plane

-   the LOCKED SyncE lock-state and OK or PARENT SyncE state of the O-RU
    using the M-Plane (optional)

-   the synchronization status of the deployed T-BC using the respective
    NMS

#### 7.4.6.3 Degraded conditions

The validation is done by checking the correct synchronization state is
observed for all steps 1 to 2 (7.4.5.3 above) (for steps 3 and 4, same
acceptance criterion as "Nominal conditions" apply):

-   the HOLDOVER sync-state of the O-DU using the NMS

-   the received PTP clockClass level of the O-DU using the NMS

-   the received SyncE SSM level of the O-DU using the NMS (optional)

-   the received PTP clockClass level of the O-RU using the M-Plane

-   the received SyncE SSM level of the O-RU using the M-Plane
    (optional). Note that if SyncE state is NOK, it is also permitted
    that the local default SSM level is reported using the M-Plane

-   the synchronization status of the deployed T-BC using the respective
    NMS - the sync-state of the O-RU using the M-Plane is LOCKED if the
    received clockClass (or optional SSM QL) value matches the
    configured list of accepted values, otherwise HOLDOVER or FREERUN

-   the PTP lock-state of the O-RU using the M-Plane is LOCKED,\
    and the PTP state of the O-RU using the M-Plane is PARENT if the
    received clockClass matches the configured list of accepted values,
    otherwise NOK

-   the SyncE lock-state (optional) of the O-RU using the M-Plane is
    LOCKED or OK,\
    and the SyncE state of the O-RU using the M-Plane is PARENT or OK if
    the received SSM matches the configured list of accepted values,
    otherwise NOK

Note: If the NETCONF client triggers a reset procedure of the O-RU by
FREERUN of the sync-state at these degraded conditions, the status
observation using M-plane is not available for NETCONF client. It is
observed that the alarm-notification is sent from the O-RU using M-Plane
and the regular start-up procedures is performed.

## 7.5 Functional test of O-DU + O-RU using ITU-T G.8275.2 profile (LLS-C1)

This test is not addressed in the present document.

## 7.6 Functional test of O-DU + bridged network + O-RU using ITU-T G.8275.2 profile (LLS-C2) 

This test is not addressed in the present document.

## 7.7 Functional test of O-DU + bridged network + O-RU using ITU-T G.8275.2 profile (LLS-C3)

This test is not addressed in the present document.

## 7.8 Functional test of O-DU + bridged network + O-RU (LLS-C4)

This test case is not addressed in the present document.

## 7.9 Performance test of O-DU + Two O-RUs using ITU-T G.8275.1 profile (LLS-C1)

### 7.9.1 Test Description and applicability

This test case is CONDITIONAL MANDATORY and shall be performed if the
O-RU and O-DU declare support of LLS-C1 synchronization option (see
Clause 4.5).

This test validates that the two O-RUs meet the 3GPP limits at their air
interface, when

-   the O-DU gets its synchronization from a PRTC using either a local
    or remote PRTC as specified in the Conformance Test Specification
    \[24\], under either ideal or normal conditions

-   and is connected to two O-RUs via direct FH links

-   and distributes frequency and time to these O-RUs using the ITU-T
    G.8275.1 (SyncE + PTP) profile

### 7.9.2 Minimum Requirements (Prerequisites)

1.  IOT Functional test 7.2 is successfully passed and all O-DU, and
    > O-RUs report LOCKED status

```{=html}
<!-- -->
```
77. O-RUs are connected to the O-DU via direct fiber O-RAN links

78. O-RUs are suitable for Case 1.1 or 1.2 as specified in eCPRI \[11\]

### 7.9.3 Purpose and scope

The O-DU synchronize the O-RUs with the ITU-T G.8275.1 profile \[5\].
This test validates that the frequency and time error on the O-RU air
interfaces are within the limits of the 3GPP, in both constant and
variable temperature and traffic load conditions.

Only LOCKED state is tested; HOLDOVER state test is not addressed in the
present document.

### 7.9.4 Testability Requirements imposed on O-RU and O-DU 

Both O-DU and O-RU are running nominal software.

Requirements for M-Plane: is "up and running."

Synchronization requirement: O-DU and test equipment is connected to a
local PRTC or source traceable to PRTC.

Test 7.2.6.2 is successfully passed and both O-DU and O-RUs report
LOCKED status.

### 7.9.5 Test Methodology

After O-DU and O-RUs are frequency and phase locked to their PRTC
synchronization source using the LLS-C1 configuration, the frequency and
phase errors are measured on the O-RUs air interface using a test
equipment referenced to the same PRTC.

The O-DU input time error on the O-DU is as specified in the Conformance
Test Specification \[24\],

-   Either "ideal" with zero value

-   Or "normal", with configured values with standard masks

### 7.9.6 Test Requirement (expected result) 

For both constant and variable conditions tests, the acceptance
criterion is to measure with the test equipment:

-   ±50 ppb maximum frequency error at the air interface

-   ITU-T Level 4, eCPRI Cat C (mandatory): ± 1500ns maximum absolute
    time error at the O-RU air interface

-   ITU-T Level 6A, eCPRI Cat B (optional): ± 260ns maximum relative
    time error between the two O-RUs air interfaces\
    Note: This level of accuracy assumes an O-RU implementation suitable
    for Case 1.1 and case 1.2 as specified in eCPRI \[11\].

-   ITU-T Level 6B, eCPRI Cat A (optional) ± 130ns maximum relative time
    error between the two O-RUs air interfaces~~\
    ~~Note: This level of accuracy assumes an O-RU implementation
    suitable for Case 1.2 as specified in eCPRI \[11\]. It also assumes
    co-location of the O-RUs and O-DU.

## 7.10 Performance test of O-DU + bridged network + Two O-RUs using ITU-T G.8275.1 profile (LLS-C2) 

### 7.10.1 Test Description and applicability

This test case is CONDITIONAL MANDATORY and shall be performed if the
O-RU and O-DU declare support of LLS-C2 synchronization option (see
Clause 4.5).

This test validates that the two O-RUs are meeting the 3GPP limits at
their air interface, when:

-   the O-DU gets its synchronization from a PRTC using a local or
    remote PRTC as specified in the Conformance Test Specification
    \[24\], under either ideal or normal conditions

-   and is connected to two O-RUs via eCPRI FH links via bridged network
    elements acting as class B T-BCs

-   and distributes frequency and time to these O-RUs using the ITU-T
    G.8275.1 (SyncE + PTP) profile \[5\]

### 7.10.2 Minimum Requirements (Prerequisites)

1.  IOT Functional Test 7.3 is successfully passed and all O-DU, bridged
    > network elements and O-RUs report LOCKED status

```{=html}
<!-- -->
```
79. O-RUs are connected to O-DU via bridged network elements acting as
    > ITU-T G.8275.1 class B T-BCs using O-RAN links \[5\]

80. O-RUs are suitable for Case 1.1 or 1.2 as specified in eCPRI \[11\]

### 7.10.3 Purpose and Scope

The O-DU synchronizes the O-RUs with the ITU-T G.8275.1 \[5\] profile
via the bridged network elements.

This test validates that the frequency and time error on the O-RU air
interfaces are within the limits of the 3GPP, in both constant and
variable temperature and traffic load conditions.

Only LOCKED state is tested; HOLDOVER state test is not addressed in the
present document.

### 7.10.4 Testability Requirements imposed on O-RU and O-DU 

Both O-DU and O-RU are running nominal software.

Requirements for M-Plane: is "up and running"

Synchronization requirement: O-DU and test equipment is connected to a
local PRTC or source traceable to PRTC.

Test 7.3.6.2 is successfully passed and both O-DU and O-RUs report
LOCKED status.

### 7.10.5 Test Methodology

After O-DU and O-RUs are frequency and phase locked to their PRTC
synchronization source using the LLS-C2 configuration, the frequency and
phase errors are measured on the O-RUs air interface using a test
equipment referenced to the same PRTC.

The O-DU input time error on the O-DU is as specified in the Conformance
Test Specification \[24\],

-   Either "ideal" with zero value

-   Or "normal", with configured values with standard masks

### 7.10.6 Test Requirement (expected result) 

For both constant and variable conditions tests, the acceptance
criterion is to measure with the test equipment:

-   ±50 ppb maximum frequency error

-   ITU-T Level 4, eCPRI Cat C (mandatory): ± 1500ns maximum absolute
    time error at the O-RU air interface

-   ITU-T Level 6A, eCPRI Cat B (optional): ± 260ns maximum relative
    time error between the two O-RUs air interfaces\
    Note: This level of accuracy assumes up to 1 (respectively 2) class
    B T-BC on the path between the branching one and each O-RU
    implementation suitable for case 1.1 (respectively case 1.2) as
    specified in eCPRI \[11\].

-   ITU-T Level 6B, eCPRI Cat A (optional) ± 130ns maximum relative time
    error between the two O-RUs air interfaces~~\
    ~~Note: This level of accuracy assumes direct fiber link between the
    branching class B T-BC and each O-RU implementation suitable case
    1.2 as specified in eCPRI \[11\] (not supported by case 1.1). It
    also assumes co-location of the O-RUs and O-DU.

## 7.11 Performance test of O-DU + bridged network + Two O-RUs using ITU-T G.8275.1 profile (LLS-C3)

### 7.11.1 Test Description and applicability

This test case is CONDITIONAL MANDATORY and shall be performed if the
O-RU and O-DU declare support of LLS-C3 synchronization option (see
Clause 4.5).

This test validates that the two O-RUs are meeting the 3GPP limits at
their air interface, and the O-DU is meeting time error limits specified
in O-RAN WG4 CUS Specification \[2\] when

-   both O-DU and O-RUs get their synchronization from a PRTC using
    SyncE + PTP over a Full Timing Support network (ITU-T G.8275.1
    profile \[5\], ITU-T G.8271.1 network limits \[7\])

### 7.11.2 Minimum Requirements (Prerequisites)

1.  IOT Functional Test 7.4 is successfully passed and all O-DU, bridged
    > network elements and O-RUs report LOCKED status

```{=html}
<!-- -->
```
81. O-RUs and O-DU are connected to bridged network elements acting as
    > ITU-T G.8275.1 class B T-BCs using O-RAN links \[5\]. This FH
    > network has a local PRTC distributing SyncE and PTP to both O-DU
    > and O-RUs.

82. O-RUs are suitable for Case 1.1 or 1.2 as specified in eCPRI \[11\]

### 7.11.3 Purpose and scope

The FH network synchronizes all O-DU and O-RUs with the ITU-T G.8275.1
\[5\] profile via the bridged network elements.

This test validates that the frequency and time error on the O-RU air
interfaces and O-DU are within the limits of the 3GPP, in both constant
and variable temperature and traffic load conditions.

Only LOCKED state is tested; HOLDOVER state test is not addressed in the
present document.

### 7.11.4 Testability Requirements imposed on O-RU and O-DU 

Both O-DU and O-RU are running nominal software.

Requirements for M-Plane: is "up and running"

Synchronization requirement: FH network and test equipment is connected
to a local PRTC or source traceable to PRTC.

Test 7.4.6.2 is successfully passed and both O-DU and O-RUs report
LOCKED status.

### 7.11.5 Test Methodology

After O-DU and O-RUs are frequency and phase locked to their PRTC
synchronization source using the LLS-C3 configuration, the frequency and
phase errors are measured at the O-RUs air interface using a test
equipment referenced to the same PRTC.

The PRTC output time error on the O-DU is as specified in the
Conformance Test Specification \[24\],

-   Either "ideal" with zero value

-   Or "normal", with configured values with standard masks

### 7.11.6 Test Requirement (expected result) 

For both constant and variable conditions tests, the acceptance
criterion is to measure with the test equipment:

-   ±50 ppb maximum frequency error (mandatory): at the O-RU air
    interface

-   ITU-T Level 4, eCPRI Cat C (mandatory): ± 1500ns maximum absolute
    time error at the O-RU air interface and at the O-DU output test
    signal (for example 1PPS)

-   ITU-T Level 6A, eCPRI Cat B (optional): ± 260ns maximum relative
    time error between the two O-RUs air interfaces\
    Note: This level of accuracy assumes up to 1 (respectively 2) class
    B T-BC on the path between the branching one and each O-RU
    implementation suitable for case 1.1 (respectively case 1.2) as
    specified in eCPRI \[11\].

-   ITU-T Level 6B, eCPRI Cat A (optional) ± 130ns maximum relative time
    error between the two O-RUs air interfaces~~\
    ~~Note: This level of accuracy assumes direct fiber link between the
    branching class B T-BC and each O-RU implementation suitable case
    1.2 as specified in eCPRI \[11\] (not supported by case 1.1). It
    also assumes co-location of the O-RUs and O-DU.

## 7.12 Performance test of O-DU + Two O-RUs using ITU-T G.8275.2 profile (LLS-C1)

This test is not addressed in the present document.

## 7.13 Performance test of O-DU + bridged network + Two O-RUs using ITU-T G.8275.2 profile ((LLS-C2) 

This test is not addressed in the present document.

## 7.14 Performance test of O-DU + bridged network + Two O-RUs using ITU-T G.8275.2 profile (LLS-C3)

This test is not addressed in the present document.

## 7.15 Performance test of O-DU + bridged network + Two O-RUs (LLS-C4)

This test is not addressed in the present document.

# 8 C/U-Plane IOT Test

## 8.1 Overview

C/U-Plane IOT tests are used to validate the performance of DUT and
interoperability of O-DU and O-RU from different vendors using O-RAN
specified or customized IOT profile test configuration(s). IOT profiles
and associated PTCs to be tested are selected by the participating
vendors. Not all PTCs within a profile are required to be tested. See
Annex A for details on the IOT profiles and PTCs.

The test environment should be arranged to match the expectations of the
test eg, provide a noise-free channel and a traffic demand matching the
intent of the test.

An O-DU and O-RU are considered interoperable under a profile test
configuration (PTC) if the DUT can pass all mandatory and applicable
conditional mandatory tests using that PTC, such passing being subject
to the DUT using "to be validated" capabilities that may be listed in
that PTC. The usage of such capabilities need not be continuous, eg,
neither in every section description nor in every slot. The exact means
to validate the usage of such capabilities is out of scope of the
present document. Exemplary means include,

a\. Proprietary capability of the DUT, eg, a special test port or test
log readout

b\. O-RAN FH protocol analysis, including that data packets are sent to
appropriately configured endpoints

The PTC may also contain a list of "to be reported" capabilities. The
usage, or absence of usage, of these capabilities shall be reported in
the test report. The usage of these capabilities is not required to pass
the test. The means of determination of the usage of these capabilities
is out of the scope of the present document

It is expected that the DUT is capable of meeting each test and PTC
requirement. The exact means to achieve this is out of scope of the
present document. Exemplary means include,

a\. By design of the DUT

b\. Proprietary capability of the DUT such as a special configuration
mechanism

## 8.2 Radio Layer 3 C-Plane establishment and Initial Radio U-Plane data transfer

### 8.2.1 Test Description and Applicability

This test case is MANDATORY.

This is a Radio system level test which is used to validate the radio
system functionalities, performance and multi-vendor interoperability of
the O-DU and O-RU from different vendors connected using the O-RAN WG4
specified FH interface \[2\], \[3\].

This test validates if a UE can perform Radio Layer 3 C-Plane
establishment and initial Radio U-Plane data transfer procedures with
the network which includes the O-DU and O-RU as an integrated system
under test in this test setup.

Although there is no FH focused testing for C/U-Plane in this test, it
is still possible to observe successful interoperability via positive
test outcomes for this test. ie, if radio system level test passes, it
can be inferred that O-RAN WG4 specified FH interface C/U-Plane is
successfully working.

The DUT shall comprise a single O-DU (DUT1(O-DU)) and a single O-RU
(DUT1(O-RU)).

### 8.2.2 Minimum Requirements (Prerequisites)

Single O-DU (DUT1(O-DU)) and a single O-RU (DUT1(O-RU))

1.  Are connected through the O-RAN FH

```{=html}
<!-- -->
```
83. Are synchronized with the common S-Plane configuration

Testing tools which are required for this test scenario

-   Single Test UE or UE emulator: used to perform Radio Layer 3 C-Plane
    establishment and Radio U-Plane data transfers with the network

-   O-CU or O-CU emulator either as a disaggregated node or as an
    aggregated node with the O-DU(s) (DUT): used to provide Layer 2 and
    Layer 3 radio processing on the network side. In case of a
    disaggregated node, terminates the 3GPP 5G F1 interface with the
    O-DU(s) (DUT)

-   4G Core network or 4G Core network emulator: used to terminate UEs
    (emulator) NAS protocol in NSA mode

-   4G MeNB or 4G MeNB emulator: used to terminate the 3GPP EN-DC X2
    interface with 5G CU in NSA mode

-   5G Core Network or 5G Core Network emulator: used to terminate UEs
    (emulator) NAS protocol in SA mode

-   Application test server: used to generate and terminate application
    layer traffic (eg, UDP, TWAMP, etc) and provide application layer
    processing on the network side

Testing tools which can be useful for this test scenario particularly
for validating that the DUTs are configured and operating correctly
during the test, troubleshooting and detailed validation purposes

-   FH Protocol Analyzer: used for protocol analysis of O-RAN FH
    protocols in this specific test scenario, C/U-Plane procedural flows
    and contents

-   RF Spectrum and Beam Signal Analyzer: used for RF and Beam power and
    quality analysis ensuring that the O-RU (DUT1(O-RU)) is transmitting
    correctly on the configured broadcast and synchronization signals on
    the downlink

### 8.2.3 Test Purpose and Scope

Purpose of this test is to validate key radio operation after M-Plane
startup, ie, Radio Layer 3 C-Plane establishment and initial Radio
U-Plane data transfer on system level with integration of O-DU and O-RU
from different vendors.

Note that this test requires both Downlink and Uplink Radio Layer 3
C-Plane message. This means that this test also validates both transfer
of Downlink and Uplink FH U-Plane message and related Downlink FH
C-Plane messages.

### 8.2.4 Testability requirements imposed on O-RU and O-DU

Nominal software runs on the O-RU and O-DU.

### 8.2.5 Test Methodology

#### 8.2.5.1 Initial Conditions

1.  O-RU and O-DU are both in service, ie, M-Plane start-up procedure is
    > completed, and broadcast channels are being transmitted

```{=html}
<!-- -->
```
84. Test UE or UE emulator has not yet been registered with the network

#### 8.2.5.2 Procedure: Nominal test

Performs Radio Layer 3 C-Plane establishment procedure using the Test UE
or UE emulator. Note that Radio Layer 3 C-Plane establishment procedure
depends on the 5G NR operation mode. In the case when the DUTs are
operating in NSA mode, Radio Layer 3 C-Plane establishment procedure
includes Attach procedure and/or service request procedure specified in
3GPP TS 23.401 \[20\] and EN-DC setup procedure specified in 3GPP TS
37.340 \[22\]. In the case when the DUTs are operating in SA mode, Radio
Layer 3 C-Plane establishment procedure includes Registration procedure
and service request procedure specified in 3GPP TS 23.502 \[21\].

Performs data transfer from the application test server to the Test UE
or UE emulator. The application test server generates and transmits 10
IP packets with each packet 32 bytes in size.

Note that data transfer depends on the operation mode. In the case when
the DUTs are operating in NSA mode, data transfers can be performed over
Default EPS bearer using SN terminated split bearer specified in 3GPP TS
37.340 \[22\]. In case when the DUTs are operating in SA mode, data
transfers can be performed over PDU Session and QoS flow specified in
3GPP TS 23.502 \[21\].

This test case does not specify the test data pattern generated by the
application test server, but it is recommended that the test data
pattern should include some level of randomness (ie, avoiding all
zeros).

### 8.2.6 Test Requirement (expected result) 

Observe the Test UE or emulated UE can perform Radio Layer 3 C-Plane
establishment successfully and can perform data transfers over the
network particularly through the O-DU and O-RU.

Record Test UE or UE emulator logs that the Radio Layer 3 (eg, RRC/NAS)
message flows are per 3GPP TS 23.401 \[20\] Sections 5.3.4, 5.4 and 3GPP
TS 37.340 \[22\] in NSA mode and 3GPP TS 23.502 \[21\] Sections 4.2.3,
4.3 in SA mode.

Record Test UE or UE emulator Radio U-Plane logs that the data packets
transferred by application test server (ie, 10 IP packets of 32 bytes)
are received correctly.

## 8.3 Radio U-Plane downlink data transfer (Downlink throughput performance) 

### 8.3.1 Radio U-Plane downlink data transfer performance with one UE

#### 8.3.1.1 Test Description and Applicability

This test case is MANDATORY.

The DUT shall comprise a single O-DU (DUT1(O-DU)) and a single O-RU
(DUT1(O-RU)).This scenario allows to test if a UE can perform Radio
U-Plane data transfers with the network through O-DU and O-RU from
different vendors.

#### 8.3.1.2 Minimum Requirements (Prerequisites)

Single O-DU (DUT1(O-DU)) and a single O-RU (DUT1(O-RU)):

1.  Are connected through the O-RAN FH

```{=html}
<!-- -->
```
85. Are synchronized with the common S-Plane configuration

Testing tools which are required for this test scenario:

-   Single Test UE or UE emulator: used to perform Radio U-Plane data
    transfers with the network

-   BFN when beamforming IOT profiles are to be tested

-   O-CU or O-CU emulator either as a disaggregated node or as an
    aggregated node with the O-DU(s) (DUT): used to provide Layer 2 and
    Layer 3 radio processing on the network side. In case of
    disaggregated node, terminates the 3GPP 5G F1 interface with the
    O-DU(s) (DUT)

-   4G Core network or 4G Core network emulator: used to terminate UEs
    (emulator) NAS protocol in NSA mode

-   4G MeNB or 4G MeNB emulator: used to terminate the 3GPP EN-DC X2
    interface with 5G CU in NSA mode

-   5G Core Network or 5G Core Network emulator: used to terminate UEs
    (emulator) NAS protocol in SA mode

-   Application test server: used to generate and terminate application
    layer traffic (eg UDP, TWAMP, etc) and provide application layer
    processing on the network side

Testing tools which can be useful for this test scenario particularly
for validating that the DUTs are configured and operating correctly
during the test, troubleshooting and detailed validation purposes:

-   FH Protocol Analyzer: used for protocol analysis of O-RAN FH
    protocols in this specific test scenario, FH C/U-Plane procedural
    flows and contents

-   RF Spectrum and Beam Signal Analyzer: used for RF and Beam power and
    quality analysis ensuring that the O-RU (DUT1(O-RU)) is transmitting
    correctly on the configured broadcast and synchronization signals on
    the downlink

#### 8.3.1.3 Test Purpose and Scope

Purpose of this test is to validate key radio operation after Radio
Layer 3 C-Plane establishment and initial Radio U-Plane data transfer,
the Radio U-Plane data transfer including throughput performance on
system level with integration of O-DU and O-RU from different venders.

Note that this test requires Maximum Layer 1 Radio data rate (with some
margin). This means that this test also validates transfer of Downlink
FH C/U-Plane message with higher MIMO layers and higher order modulation
schemes.

#### 8.3.1.4 Testability requirements imposed on O-RU and O-DU

Nominal software runs on the O-RU and O-DU.

#### 8.3.1.5 Test Methodology

##### 8.3.1.5.1 Initial Conditions

1.  O-RU and O-DU are both in service, ie, M-Plane start-up procedure
    > has been completed and broadcast channels are being transmitted

```{=html}
<!-- -->
```
86. Test UE or UE emulator has registered to the network, ie, Radio
    > Layer 3 C-Plane establishment procedure is completed. Note that
    > Radio Layer 3 C-Plane establishment procedure depends on operation
    > mode. In case when the of DUTs are operating in NSA mode, Radio
    > Layer 3 C-Plane establishment procedure includes means Attach
    > procedure and/or service request procedure specified in 3GPP TS
    > 23.401 \[20\] and EN-DC setup procedure specified in 3GPP TS
    > 37.340 \[22\]. In case when the of DUTs are operating in SA mode,
    > Radio Layer 3 C-Plane establishment procedure includes means
    > Registration procedure and service request procedure specified in
    > 3GPP TS 23.502 \[21\].

##### 8.3.1.5.2 Procedure: Nominal test

Performs downlink data transfer from application test server to the Test
UE or UE emulator. The application test server generates and transmits
downlink data with data size large enough to achieve the maximum Layer 1
Radio data rate, which is specified in 8.2.6, for the duration of the
test. The duration of the test is 20 seconds.

Note that data transfer depends on the operation mode. In case when the
DUTs are operating in NSA mode, data transfers can be performed over
Default EPS bearer using SN terminated split bearer specified in 3GPP TS
37.340 \[22\]. In case when the DUTs are operating in SA mode, data
transfers can be performed over PDU Session and QoS flow specified in
3GPP TS 23.502 \[21\].

This test case does not specify the test data pattern generated by the
application test server, but it is recommended that the test data
pattern should include some level of randomness (ie, avoiding all
zeros).

#### 8.3.1.6 Test Requirement (expected result) 

Observe that the Test UE or emulated UE can perform Radio U-Plane data
transfers over the network particularly through the O-DU and O-RU at the
target data rate.

Record the Test UE or UE emulator Radio U-Plane logs and determine that
they contain measurements such as the measured Radio U-Plane data rates
during the test. The acceptance criterion is that Radio U-Plane data
rate on average during the test duration achieves the performance level
defined as follows

> **[Performance level]{.ul}**

Target data rate = Maximum Layer 1 Radio data rate \* (1 - Ratio of
Radio resource overhead) \* Margin,

where

*[Maximum Layer 1 Radio data rate]{.ul}* is calculated based on 3GPP TS
38. 211 \[15\] and TS 38.214 \[23\] by using RAN parameters, ie, Total
channel bandwidth, TDD configuration (when TDD), number of
spatial/antenna streams, modulation order and coding rate. Note that
these RAN parameters are defined in the IOT profiles (see Annex A for
details).

*[Ratio of Radio resource overhead]{.ul}* is calculated based on 3GPP TS
38.211 \[15\] by using Radio physical layer channel configurations, eg,
PDCCH resource mapping, Reference signal resource mapping, and so on,
assumed in the IOT setup. Note that the physical layer channel
configurations are part of the radio test setup configuration.

*[Margin]{.ul}* is assumed in order to account for issues other than the
FH. The value of *Margin* is 0.8.

### 8.3.2 Radio U-Plane downlink data transfer performance with two UEs 

#### 8.3.2.1 Test Description and Applicability

This test is CONDITIONAL MANDATORY; the condition being the DUT supports
at least two simultaneous UE data layers. Any PTC not stating a UE data
layer configuration is not required to execute the test.

The DUT shall comprise a single O-DU (DUT1(O-DU)) and a single O-RU
(DUT1(O-RU)).

This scenario allows to test that two UEs can simultaneously perform
Radio U-Plane data transfer with the network through O-DU and O-RU from
different vendors as set out below.

#### 8.3.2.2 Minimum Requirements (Prerequisites)

Single O-DU (DUT1(O-DU)) and a single O-RU (DUT1(O-RU))

1\. Are connected through the O-RAN FH

2\. Are synchronized with the common S-Plane configuration

Testing tools which are required for this test scenario:

1\. Two UEs, either test UEs or UE emulator capable to support two UEs,
where each UE supports a single layer: used to perform Radio U-Plane
data transfer with the network

2\. BFN able to simultaneously provide two downlink channels with
different effective angle of departure for the UEs. The angle of
departure and channel conditioning to provide sufficient rank of channel
matrix such that each UE can respectively receive the UE layer directed
to it. The BFN shall provide symmetrical uplink and downlink channels

3\. O-CU or O-CU emulator either as a disaggregated node or as an
aggregated node with the (DUT1) O-DU. In case of disaggregated node,
O-CU or O-CU emulator terminates the 3GPP 5G F1 interface with the DUT1
(O-DU)

4\. 5G Core Network or 5G Core Network emulator: used to terminate UEs
(emulator) NAS protocol

5\. Application test server: used to generate and terminate application
layer traffic (eg UDP, TWAMP, etc) and provide application layer
processing on the network side

Testing tools which can be useful for this test scenario particularly
for validating that the DUTs are configured and operating correctly
during the test, troubleshooting and detailed validation purposes:

1\. RF Spectrum and Beam Signal Analyzer: used for RF and Beam power and
quality analysis ensuring that the O-RU (DUT1(O-RU)) is correctly
transmitting the configured broadcast and synchronization signals on the
downlink

2\. FH Protocol Analyzer: For protocol analysis of O-RAN FH protocols
and message flows (for example to verify or report used capabilities)

Additional requirements for this test scenario:

1\. A means to determine that the DUT has used the capabilities declared
in the "to be validated" and "to be reported" tables associated with the
PTC. The exact means of determination is out of scope of the present
document

#### 8.3.2.3 Test Purpose and Scope

Purpose of this test is to validate, after Radio Layer 3 C-Plane
establishment and initial Radio U-Plane data transfer when 2 UEs are
connected to the network according to the relevant constraints in the
PTC, the Radio U-Plane data transfer including throughput performance on
system level with integration of O-DU and O-RU from different vendors.

This test requires Maximum Layer 1 Radio data rate (with some margin)
for successful completion. This means that this test also validates
transfer of Downlink FH C/U-Plane messages with two layers, one per
mobile, and higher order modulation schemes.

#### 8.3.2.4 Testability requirements imposed on O-RU and O-DU

Nominal software runs on the O-RU and O-DU.

#### 8.3.2.5 Test Methodology

##### 8.3.2.5.1 Initial Conditions

1\. O-RU and O-DU are both in service, ie, M-Plane start-up procedure
has been completed and broadcast channels are being transmitted

The two UEs, either test UE or UE emulator, have registered to the
network, ie, Radio Layer 3 C-Plane establishment procedures are
completed. Radio Layer 3 C-Plane establishment procedure includes
Registration procedure and service request procedure specified in 3GPP
TS 23.502 \[21\]

##### 8.3.2.5.2 Procedure: Nominal test

Perform downlink data transfer from the application test server on the
network side to the UEs. The application test server connected to the
UEs generates and transmits data with data size that, when aggregated
across both UEs, is large enough to achieve the maximum Layer 1 Radio
data rate, which is specified in 8.3.2.6, for the duration of the test.
The duration of the test is 20 seconds.

Data transfers shall be performed over PDU Session and QoS flow
specified in 3GPP TS 23.502 \[21\].

This test case does not specify the test data pattern generated by the
application test server connected to the UEs, but it is recommended that
the test data pattern should include some level of randomness (ie, avoid
all zeros).

#### 8.3.2.6 Test Requirement (expected result) 

Observe that both UEs perform Radio U-Plane data reception over the
network through the O-DU and O-RU, with aggregated UE transfer rate
achieving the target data rate.

Collect the Radio U-Plane logs of both UEs and analyze to determine each
contains measurements such as the measured Radio U-Plane data rates
during the test

Observe, for example by analyzing message flows over FH, that "to be
validated" capabilities listed in the PTC are used and such usage is
recorded in the test report.

Observe that the usage or absence of usage of the "to be reported"
capabilities listed in the PTC is recorded in the test report.

The performance acceptance criterion is that for the duration of the
test both UEs simultaneously receive downlink data such that the
aggregated Radio U-Plane rate achieves the performance level defined as
follows,

> **[Performance level]{.ul}**
>
> Target data rate = Maximum Layer 1 Radio data rate \* (1 -- Margin),
>
> where

*[Maximum Layer 1 Radio data]{.ul}* rate is calculated based on TS
38.306, clause 4.1.2 \[26\] with ʋ= 2 (for two layers, one per UE). The
data rate shall be pro-rated with the TDD configuration specified in IOT
profile. Parameter values for number of carriers (J), numerology (µ),
and total channel bandwidth (BW) are also specified in the IOT profiles.
Maximum supported modulation order (Q~m~) is DUT's maximum supported
modulation order in DL for the PTC being tested. Scaling factor (f)
shall be set to one. Any parameters in Equation 8.3.2.6-1 not defined in
the IOT profiles are defined in TS 38.306 \[26\]

> ![Max rate](media/image9.png){width="4.664770341207349in"
> height="0.6067508748906387in"}\[Equation 8.3.2.6-1\]

*[Margin]{.ul}* is assumed in order to account for impairments other
than the FH. The value of Margin is 0.2

*[Multi-layer operation is implicitly tested as achievement of target
performance requires that each UEs nominally consumes all available
resources on its respective layer]{.ul}*

If the data throughput performance achieves the necessary performance
level but use of "to be validated" capabilities listed in the PTC is NOT
confirmed, the inconclusive outcome of the test is marked as failure.

## 8.4 Radio U-Plane uplink data transfer (Uplink throughput performance) 

### 8.4.1 Radio U-Plane uplink data transfer performance with one UE

#### 8.4.1.1 Test Description and Applicability

This test case is MANDATORY.

The DUT shall comprise a single O-DU (DUT1(O-DU)) and a single O-RU
(DUT1(O-RU)).

This scenario allows to test if a UE can perform Radio U-Plane data
transfers with the network through O-DU and O-RU from different vendors.

#### 8.4.1.2 Minimum Requirements (Prerequisites)

Single O-DU (DUT1(O-DU)) and a single O-RU (DUT1(O-RU))

1.  Are connected through the O-RAN FH

```{=html}
<!-- -->
```
87. Are synchronized with the common S-Plane configuration

Testing tools which are required for this test scenario

-   Single Test UE or UE emulator: used to perform Radio U-Plane data
    transfers with the network

-   BFN when beamforming IOT profiles are to be tested

-   O-CU or O-CU emulator either as a disaggregated node or as an
    aggregated node with the O-DU(s) (DUT): used to provide Layer 2 and
    Layer 3 radio processing on the network side. In case of a
    disaggregated node, terminates the 3GPP 5G F1 interface with the
    O-DU(s) (DUT).

-   4G Core network or 4G Core network emulator: used to terminate UEs
    (emulator) NAS protocol in NSA mode

-   4G MeNB or 4G MeNB emulator: used to terminate the 3GPP EN-DC X2
    interface with 5G CU in NSA mode

-   5G Core Network or 5G Core Network emulator: used to terminate UEs
    (emulator) NAS protocol in SA mode

-   Application test server: used to generate and terminate application
    layer traffic (eg UDP, TWAMP, etc) and provide application layer
    processing on the network side

Testing tools which can be useful for this test scenario particularly
for validating that the DUTs are configured and operating correctly
during the test, troubleshooting and detailed validation purposes

-   FH Protocol Analyzer: used for protocol analysis of O-RAN FH
    protocols in this specific test scenario, FH C/U-Plane procedural
    flows and contents

-   RF Spectrum and Beam Signal Analyzer: used for RF and Beam power and
    quality analysis ensuring that the O-RU (DUT1(O-RU)) is transmitting
    correctly on the configured broadcast and synchronization signals on
    the downlink

#### 8.4.1.3 Test Purpose and Scope

Purpose of this test is to validate key radio operation after Radio
Layer 3 C-Plane establishment and initial Radio U-Plane data transfer,
the Radio U-Plane data transfer including throughput performance on
system level with integration of O-DU and O-RU from different venders.

Note that this test requires Maximum Layer 1 Radio data rate (with some
margin). This means that this test also validates transfer of Uplink FH
C/U-Plane message with higher MIMO layers and higher order modulation
schemes.

#### 8.4.1.4 Testability requirements imposed on O-RU and O-DU

Nominal software runs on the O-RU and O-DU.

#### 8.4.1.5 Test Methodology

##### 8.4.1.5.1 Initial Conditions

1.  O-RU and O-DU are both in service, ie, M-Plane start-up procedure
    has been completed and broadcast channels are being transmitted

```{=html}
<!-- -->
```
88. Test UE or UE emulator has registered to the network, ie, Radio
    Layer 3 C-Plane establishment procedure is completed. Note that
    Radio Layer 3 C-Plane establishment procedure depends on operation
    mode. In case when the of DUTs are operating in NSA mode, Radio
    Layer 3 C-Plane establishment procedure includes means Attach
    procedure and/or service request procedure specified in 3GPP TS
    23.401 \[20\] and EN-DC setup procedure specified in 3GPP TS 37.340
    \[22\]. In case when the of DUTs are operating in SA mode, Radio
    Layer 3 C-Plane establishment procedure includes means Registration
    procedure and service request procedure specified in 3GPP TS 23.502
    \[21\].

##### 8.4.1.5.2 Procedure: Nominal test

Performs uplink data transfer from the Test UE or UE emulator to
application test server on the network side. Either the Test UE or UE
emulator, or application test server connected with UE generates and
transmits uplink data with data size large enough to achieve the maximum
Layer 1 Radio data rate, which is specified in 8.3.6, for the duration
of the test. The Test UE or UE emulator transmits the uplink data. The
duration of the test is 20 seconds.

Note that data transfer depends on the operation mode. In case when the
DUTs are operating in NSA mode, data transfers can be performed over
Default EPS bearer using SN terminated split bearer specified in 3GPP TS
37.340 \[22\]. In case when the DUTs are operating in SA mode, data
transfers can be performed over PDU Session and QoS flow specified in
3GPP TS 23.502 \[21\].

This test case does not specify the test data pattern generated by
either the Test UE or UE emulator, or application test server connected
with UE, but it is recommended that the test data pattern should include
some level of randomness (ie, avoiding all zeros).

#### 8.4.1.6 Test Requirement (expected result) 

Observe that the Test UE or emulated UE can perform Radio U-Plane data
transfers over the network particularly through the O-DU and O-RU at the
target data rate.

Record the Test UE or UE emulator Radio U-Plane logs and determine that
they contain measurements such as the measured Radio U-Plane data rates
during the test. The acceptance criterion is that Radio U-Plane data
rate on average during the test duration achieves the performance level
defined as follows

> **[Performance level]{.ul}**

Target data rate = Maximum Layer 1 Radio data rate \* (1 - Ratio of
Radio resource overhead) \* Margin,

where

*[Maximum Layer 1 Radio data rate]{.ul}* is calculated based on 3GPP TS
38. 211 \[15\] and TS 38.214 \[23\] by using RAN parameters, ie, Total
channel bandwidth, TDD configuration (when TDD), number of
spatial/antenna streams, modulation order and coding rate. Note that
these RAN parameters are defined in the IOT profiles (see Annex A for
details).

*[Ratio of Radio resource overhead]{.ul}* is calculated based on 3GPP TS
38.211 \[15\] by using Radio physical layer channel configurations, eg,
PUCCH resource mapping, Reference signal resource mapping, and so on,
assumed in the IOT setup. Note that the physical layer channel
configurations are part of the radio test setup configuration.

*[Margin]{.ul}* is assumed in order to account for issues other than the
FH. The value of *Margin* is 0.8.

### 8.4.2 Radio U-Plane uplink data transfer performance with two UEs 

#### 8.4.2.1 Test Description and Applicability

This test is CONDITIONAL MANDATORY; the condition being the DUT supports
at least two simultaneous UE data layers. Any PTC not stating a UE data
layer configuration is not required to execute the test.

The DUT shall comprise a single O-DU (DUT1(O-DU)) and a single O-RU
(DUT1(O-RU)).

This scenario allows to test that two UEs can simultaneously perform
Radio U-Plane data transfer with the network through O-DU and O-RU from
different vendors as set out below.

#### 8.4.2.2 Minimum Requirements (Prerequisites)

Single O-DU (DUT1(O-DU)) and a single O-RU (DUT1(O-RU))

1\. Are connected through the O-RAN FH

2\. Are synchronized with the common S-Plane configuration

Testing tools which are required for this test scenario:

1\. Two UEs, either test UEs or UE emulator capable to support two UEs,
where each UE supports a single layer: used to perform Radio U-Plane
data transfer with the network

2\. BFN able to simultaneously provide two uplink channels with
different effective angle of arrival for the UEs. The angle of arrival
and channel conditioning to provide sufficient rank of the channel
matrix, such that both UE layers can be properly detected by the DUT
during channel estimation and equalisation. The BFN shall provide
symmetrical uplink and downlink channels

3\. O-CU or O-CU emulator either as a disaggregated node or as an
aggregated node with the (DUT1) O-DU. In case of disaggregated node,
O-CU or O-CU emulator terminates the 3GPP 5G F1 interface with the DUT1
(O-DU)

4\. 5G Core Network or 5G Core Network emulator: used to terminate UEs
(emulator) NAS protocol

5\. Application test server: used to generate and terminate application
layer traffic (eg UDP, TWAMP, etc) and provide application layer
processing on the network side

Testing tools which can be useful for this test scenario particularly
for validating that the DUTs are configured and operating correctly
during the test, troubleshooting and detailed validation purposes:

1\. RF Spectrum and Beam Signal Analyzer: used for RF and Beam power and
quality analysis ensuring that the O-RU (DUT1(O-RU)) is correctly
transmitting the configured broadcast and synchronization signals on the
downlink

2\. FH Protocol Analyzer: For protocol analysis of O-RAN FH protocols
and message flows (for example to verify or report used capabilities)

Additional requirements for this test scenario:

1\. A means to determine that the DUT has used the capabilities declared
in the "to be validated" and "to be reported" tables associated with the
PTC. The exact means of determination is out of scope of the present
document

#### 8.4.2.3 Test Purpose and Scope

Purpose of this test is to validate, after Radio Layer 3 C-Plane
establishment and initial Radio U-Plane data transfer when 2 UEs are
connected to the network according to the relevant constraints in the
PTC, the Radio U-Plane data transfer including throughput performance on
system level with integration of O-DU and O-RU from different vendors.

This test requires Maximum Layer 1 Radio data rate (with some margin)
for successful completion. This means that this test also validates
transfer of Uplink FH C/U-Plane messages with two layers, one per
mobile, and higher order modulation schemes.

#### 8.4.2.4 Testability requirements imposed on O-RU and O-DU

Nominal software runs on the O-RU and O-DU.

#### 8.4.2.5 Test Methodology

##### 8.4.2.5.1 Initial Conditions

1\. O-RU and O-DU are both in service, ie, M-Plane start-up procedure
has been completed and broadcast channels are being transmitted

The two UEs, either test UE or UE emulator, have registered to the
network, ie, Radio Layer 3 C-Plane establishment procedures are
completed. Radio Layer 3 C-Plane establishment procedure includes
Registration procedure and service request procedure specified in 3GPP
TS 23.502 \[21\]

##### 8.4.2.5.2 Procedure: Nominal test

Perform uplink data transfer from the UEs to the application test server
on the network side. Both UEs, or application test server connected to
the UEs, generate and transmit uplink data with data size, when
aggregated across both UEs, is large enough to achieve the maximum Layer
1 Radio data rate, which is specified in 8.4.2.6, for the duration of
the test. The duration of the test is 20 seconds.

Data transfers shall be performed over PDU Session and QoS flow
specified in 3GPP TS 23.502 \[21\].

This test case does not specify the test data pattern generated by the
UEs, or application test server connected to the UEs, but it is
recommended that the test data pattern should include some level of
randomness (ie, avoid all zeros).

#### 8.4.2.6 Test Requirement (expected result) 

Observe that both UEs perform Radio U-Plane data transfer over the
network through the O-DU and O-RU, with aggregated UE transfer rate
achieving the target data rate.

Collect the Radio U-Plane logs of both UEs and analyze to determine each
contains measurements such as the measured Radio U-Plane data rates
during the test

Observe, for example by analyzing message flows over FH, that "to be
validated" capabilities listed in the PTC are used and such usage is
recorded in the test report.

Observe that the usage or absence of usage of the "to be reported"
capabilities listed in the PTC is recorded in the test report.

The performance acceptance criterion is that for the duration of the
test both UEs simultaneously transmit uplink data such that the
aggregated Radio U-Plane rate achieves the performance level defined as
follows,

**[Performance level]{.ul}**

Target data rate = Maximum Layer 1 Radio data rate \* (1 -- Margin),

where

*[Maximum Layer 1 Radio data rate]{.ul}* is calculated based on TS
38.306, clause 4.1.2 \[26\], Equation 8.3.2.6-1 above defines the
relationship, with ʋ= 2 (for two layers, one per UE). The data rate
shall be pro-rated with the TDD configuration specified in IOT profile.
Parameter values for number of carriers (J), numerology (µ), and total
channel bandwidth (BW) are also specified in the IOT profiles. Maximum
supported modulation order (Q~m~) is DUT's maximum supported modulation
order in UL for the PTC being tested. Scaling factor (f) shall be set to
one. Any parameters in Equation 8.3.2.6-1 not defined in the IOT
profiles are defined in TS 38.306 \[26\]

*[Margin]{.ul}* is assumed in order to account for impairments other
than the FH. The value of Margin is 0.2

*[Multi-layer operation is implicitly tested as achievement of target
performance requires that each UEs nominally consumes all available
resources on its respective layer]{.ul}*

If the performance acceptance criterion has been met, but use of "to be
validated" capabilities listed in the PTC is NOT confirmed, the
inconclusive outcome of the test is marked as failure.

# 9 C/U-Plane Delay Management IOT Test

## 9.1 General

The test cases defined in this section will validate that the
transmitted Control- and User-data packets sent from the O-DU are
received within the reception windows at the O-RU by checking that the
frame timing on the air interface is correct.

The same is applicable for uplink direction, ie, that the User-data
packets sent from the O-RU are received within the reception window on
the O-DU, this is done by checking that it is possible for a test UE to
attach and send data.

For all currently defined IOT Profiles the O-DU timing advance type is
'Fixed Timing Advance'. The Figure below is copied from the O-RAN WG4
CUS Specification \[2\] section 4.4.6 "Latency Categories for O-DU with
fixed timing advance".

![](media/image10.png){width="6.69375in" height="2.970138888888889in"}

**Figure 9.1-1: O-RAN WG4 CUS Specification \[2\] section 4.4.6 "Latency
Categories for O-DU with fixed timing advance".**

The Figure shows the downlink timing when fixed timing is used, the
point TX~DL_Start~ is a fixed point in relation to the "OTA
transmission" point.

The O-DU needs only to be configured with T~12max~, T~12min~ and
T~cp_adv_dl~ the values are taken from the profile that is used when
running these test cases. The T~cp_adv_dl~ value is the time in advance
the O-RU needs the C-Plane messages before the U-Plane information is
received by the O-RU. These test cases assume a symmetric latency in the
Fronthaul Network, ie, T12=T34.

These test cases assume that the difference between "fixed timing
advance" and "dynamic timing advance" is that for "fixed timing advance"
the O-DU will advance the transmission of downlink data the same amount
of time for all connected O-RUs regardless of the individual fronthaul
latency, for "dynamic timing advance" the advancement could be different
per O-RU and thus eg, T~12max~ shall be configured per O-RU.

An O-DU running in "Fixed Timing Advance"-mode is an O-DU that has the
ability to handle a specific value for T1a (sum of fronthaul latency T12
and O-RU processing delay T2a). The O-DU will set the TX~DL_Start~ to
this fixed value independent on actual T12_max value.

TXmax~lls-CU~ will vary due to different line-rates of the fronthaul
interface and amount of data (control+user) that is sent for a specific
symbol.

## 9.2 Test environment

Testing tools which are required for the delay management test cases.

-   Single Test UE or UE emulator: used to perform Radio Layer 3 C-Plane
    establishment and Radio U-Plane data transfers with the network

-   O-CU or O-CU emulator either as a disaggregated node or as an
    aggregated node with the O-DU(s) (DUT): used to provide Layer 2 and
    Layer 3 radio processing on the network side. In case of a
    disaggregated node, terminates the 3GPP 5G F1 interface with the
    O-DU(s) (DUT)

-   4G Core network or 4G Core network emulator: used to terminate UEs
    (emulator) NAS protocol in NSA mode

-   4G MeNB or 4G MeNB emulator: used to terminate the 3GPP EN-DC X2
    interface with 5G CU in NSA mode

-   5G Core Network or 5G Core Network emulator: used to terminate UEs
    (emulator) NAS protocol in SA mode

-   Application test server: used to generate and terminate application
    layer traffic (eg, UDP, TWAMP, etc) and provide application layer
    processing on the network side

![](media/image11.png){width="6.332638888888889in"
height="4.936805555555556in"}

**Figure 9.2-1: Delay-management test environment**

Testing tools which can be useful for this test scenario particularly
for validating that the DUTs are configured and operating correctly
during the test, troubleshooting and detailed validation purposes

-   FH Protocol Analyzer: used for protocol analysis of O-RAN FH
    protocols in this specific test scenario, C/U-Plane procedural flows
    and contents

-   RF Spectrum and Beam Signal Analyzer: used for RF and Beam power and
    quality analysis ensuring that the O-RU (DUT1(O-RU)) is transmitting
    correctly on the configured broadcast and synchronization signals on
    the downlink

## 9.3 Timing accuracy definition

When in "Test Requirement (expected result)" it is stated "... *timing
accuracy at the antenna reference point is according to requirement*"
the following is applicable.

In ORAN WG4 CUS Specification \[2\] section 11.2.5.5 "Air interface
maximum time error", tables 11.2.5.5-1 and 11.2.5.5-2 list the 3GPP air
interface timing accuracy for different LTE and 5G features. The timing
accuracy requirements are divided into 2 alternatives, relative or
absolute time errors.

Depending on what 3GPP features that are to be supported by a specific
IOT-profile different timing accuracy requirement is thus applicable.

## 9.4 Delay Management \#1, minimum fronthaul latency

### 9.4.1 Test Description and Applicability

This test case is OPTIONAL.

This is a Radio system level test which is used to validate the radio
system functionalities, performance and multi-vendor interoperability of
the O-DU and O-RU from different vendors connected using the O-RAN WG4
specified FH interface \[2\], \[3\].

This test validates that the O-RU will transmit the user data at correct
point in time and with correct content during different conditions
related to the fronthaul interface latency between the O-DU and the
O-RU.

### 9.4.2 Minimum Requirements

Single O-DU (DUT1(O-DU)) and a single O-RU (DUT1(O-RU))

1.  Are connected through the O-RAN FH

2.  Are synchronized with the common S-Plane configuration

### 9.4.3 Test Purpose

Purpose of this test is to validate that correct timing is achieved on
the air interface regardless of the O-RU processing time and using the
minimum feasible fronthaul latency.

### 9.3.4 Testability requirements imposed on O-RU and O-DU

Nominal software runs on the O-RU and O-DU.

### 9.4.5 Test Methodology

#### 9.4.5.1 Initial Conditions

1.  The fronthaul latency should be at a minimum for this test case. The
    T12_min in current IOT-Profiles is 0µs.\
    0µs is not possible to achieve in reality, instead the shortest
    possible fronthaul latency with existing test equipment is
    sufficient for this initial condition.

```{=html}
<!-- -->
```
89. O-RU and O-DU are both in service, ie, M-Plane start-up procedure is
    completed and broadcast channels are being transmitted

90. Test UE or UE emulator has registered to the network, ie, Radio
    Layer 3 C-Plane establishment procedure is completed

#### 9.4.5.2 Procedure: Nominal test

Performs downlink and uplink data transfer to/from the test UE.

### 9.4.6 Test Requirement (expected result) 

Observe that:

1.  With Fronthaul Protocol Analyzer (connected at the O-DU-end of
    fronthaul interface), observe that the fronthaul C- and U-Plane
    messages transmitted by the O-DU are transmitted within respective
    plane's transmission windows.

```{=html}
<!-- -->
```
91. With Fronthaul Protocol Analyzer (connected at the O-RU-end of
    fronthaul interface), observe that the fronthaul C- and U-Plane
    messages in downlink direction are received within respective
    plane's reception window by the O-RU.

92. With the RF Spectrum Analyzer, observe that the air interface
    transmission timing accuracy at the antenna reference point is
    according to requirements as specified in section 9.3.

93. With Fronthaul Protocol Analyzer (connected at the O-RU-end of
    fronthaul interface), observe that the U-Plane messages transmitted
    by the O-RU (uplink direction) are transmitted within the O-RU's
    transmission window

## 9.5 Delay Management \#2, maximum fronthaul latency

### 9.5.1 Test Description and Applicability

This test case is OPTIONAL.

This is a Radio system level test which is used to validate the radio
system functionalities, performance and multi-vendor interoperability of
the O-DU and O-RU from different vendors connected using the O-RAN WG4
specified FH interface \[2\], \[3\].

This test validates that the O-RU will transmit the user data at correct
point in time and with correct content during different conditions
related to the fronthaul interface between the O-DU and the O-RU.

### 9.5.2 Minimum Requirements

Single O-DU (DUT1(O-DU)) and a single O-RU (DUT1(O-RU))

1.  Are connected through the O-RAN FH

```{=html}
<!-- -->
```
94. Are synchronized with the common S-Plane configuration

### 9.5.3 Test Purpose

Purpose of this test is to validate that correct timing is achieved on
the air interface regardless of the O-RU processing time and using the
maximum supported fronthaul latency as per the corresponding IOT
profile.

### 9.5.4 Testability requirements imposed on O-RU and O-DU

Nominal software runs on the O-RU and O-DU.

### 9.5.5 Test Methodology

#### 9.5.5.1 Initial Conditions

1.  The fronthaul latency should be at a maximum for this test case. The
    T12_max in current IOT-Profiles is 160µs.

```{=html}
<!-- -->
```
95. O-RU and O-DU are both in service, ie, M-Plane start-up procedure is
    completed and broadcast channels are being transmitted

96. Test UE or UE emulator has registered to the network, ie, Radio
    Layer 3 C-Plane establishment procedure is completed.

#### 9.5.5.2 Procedure: Nominal test

Performs downlink and uplink data transfer to/from the test UE.

### 9.5.6 Test Requirement (expected result) 

Observe that:

1.  With Fronthaul Protocol Analyzer (connected at the O-DU-end of
    fronthaul interface), observe that the fronthaul C- and U-Plane
    messages transmitted by the O-DU are transmitted within respective
    plane's transmission windows.

```{=html}
<!-- -->
```
97. With Fronthaul Protocol Analyzer (connected at the O-RU-end of
    fronthaul interface), observe that the fronthaul C- and U-Plane
    messages in downlink direction are received within respective
    plane's reception window by the O-RU.

98. With the RF Spectrum Analyzer, observe that the air interface
    transmission timing accuracy at the antenna reference point is
    according to requirements as specified in section 9.3.

99. With Fronthaul Protocol Analyzer (connected at the O-RU-end of
    fronthaul interface), observe that the U-Plane messages transmitted
    by the O-RU (uplink direction) are transmitted within the O-RU's
    transmission window.

## 9.6 Delay Management \#3, normal fronthaul latency

### 9.6.1 Test Description and Applicability

This test case is OPTIONAL.

This is a Radio system level test which is used to validate the radio
system functionalities, performance and multi-vendor interoperability of
the O-DU and O-RU from different vendors connected using the O-RAN WG4
specified FH interface \[2\], \[3\].

This test validates that the O-RU will transmit the user data at correct
point in time and with correct content during different conditions
related to the fronthaul interface between the O-DU and the O-RU.

### 9.6.2 Minimum Requirements

Single O-DU (DUT1(O-DU)) and a single O-RU (DUT1(O-RU))

1.  Are connected through the O-RAN FH

```{=html}
<!-- -->
```
100. Are synchronized with the common S-Plane configuration

### 9.6.3 Test Purpose

Purpose of this test is to validate that correct timing is achieved on
the air interface regardless of the O-RU processing time and using a
normal fronthaul latency as per the corresponding IOT profile.

### 9.6.4 Testability requirements imposed on O-RU and O-DU

Nominal software runs on the O-RU and O-DU.

### 9.6.5 Test Methodology

#### 9.6.5.1 Initial Conditions

1.  The fronthaul latency should be set to an arbitrary value between 0
    and 160µs eg, 75µs

2.  O-RU and O-DU are both in service, ie, M-Plane start-up procedure is
    completed and broadcast channels are being transmitted

3.  Test UE or UE emulator has registered to the network, ie, Radio
    Layer 3 C-Plane establishment procedure is completed

#### 9.6.5.2 Procedure: Nominal test

Performs downlink and uplink data transfer to/from the test UE.

### 9.6.6 Test Requirement (expected result) 

Observe that:

1.  With Fronthaul Protocol Analyzer (connected at the O-DU-end of
    fronthaul interface), observe that the fronthaul C- and U-Plane
    messages transmitted by the O-DU are transmitted within respective
    plane's transmission windows.

2.  With Fronthaul Protocol Analyzer (connected at the O-RU-end of
    fronthaul interface), observe that the fronthaul C- and U-Plane
    messages in downlink direction are received within respective
    plane's reception window by the O-RU.

3.  With the RF Spectrum Analyzer, observe that the air interface
    transmission timing accuracy at the antenna reference point is
    according to requirements as specified in section 9.3.

4.  With Fronthaul Protocol Analyzer (connected at the O-RU-end of
    fronthaul interface), observe that the U-Plane messages transmitted
    by the O-RU (uplink direction) are transmitted within the O-RU's
    transmission window.

## 9.7 Delay Management \#4, larger fronthaul latency then supported

### 9.7.1 Test Description and Applicability

This test case is OPTIONAL.

This is a Radio system level test which is used to validate the radio
system functionalities, performance and multi-vendor interoperability of
the O-DU and O-RU from different vendors connected using the O-RAN WG4
specified FH interface \[2\], \[3\].

This test validates that the O-RU will **[not]{.ul}** transmit anything
on the air interface when the latency in the fronthaul network is larger
than is supported by the O-RU, ie, the C- and U-Plane messages will be
received too late on the O-RU (outside its reception window) and thus be
dropped by the O-RU.

### 9.7.2 Minimum Requirements

Single O-DU (DUT1(O-DU)) and a single O-RU (DUT1(O-RU))

1.  Are connected through the O-RAN FH

```{=html}
<!-- -->
```
101. Are synchronized with the common S-Plane configuration

### 9.7.3 Test Purpose

Validate that the O-RU will not transmit anything OTA when the
configured fronthaul latency is larger than the maximum supported value
as per the corresponding IOT profile.

### 9.7.4 Testability requirements imposed on O-RU and O-DU

Nominal software runs on the O-RU and O-DU.

### 9.7.5 Test Methodology

#### 9.7.5.1 Initial Conditions

1.  The fronthaul latency should be set to a value that is larger than
    the O-DU's category specifies

#### 9.7.5.2 Procedure: Nominal test

\-

### 9.7.6 Test Requirement (expected result) 

Observe that the no cell is being transmitted by the O-RU over the air
interface.

# Annex A (normative): Profiles used for Interoperability Testing

## A.1 General

This Annex contains the IOT Profiles and the IOT Profile Test
Configurations (PTC) within each IOT Profile.

Sometimes the value of existing IOT Profile Test Configuration parameter
will change from one version of the specification to the next.
Therefore, it is necessary to refer to both the IOT Profile Test
Configuration name and the particular version of the WG4 IOT
specification to ensure that the appropriate set of profile parameters
are referenced.

For IOT testing, the Profile Test Configuration serves as entry criteria
for O-DU and O-RU. The terminology used in the IOT profiles is listed in
Table A.1-1.

Table A.1-1: Meaning of terminology used in the IOT profiles.

  **Terminology**   **O-DU entry criterion**                                   **O-RU entry criterion**                                   **Additional information**
  ----------------- ---------------------------------------------------------- ---------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  REQ               Capability is supported                                    Capability is supported                                    Capability is expected to be used in the IOT test but actual usage is not guaranteed
  O-RU REQ          Capability may be supported (not a test entry criterion)   Capability is supported                                    The capability is supported by the O-RU and thus depending on O-DU support, O-DU may use the capability. In the IOT testing, the capability need not be invoked. This allows many O-DU designs to match an O-RU capabilities
  NOT REQ           Capability may be supported (not a test entry criterion)   Capability may be supported (not a test entry criterion)   There is no support requirement on O-DU and O-RU and O-DU is allowed to use the capability in IOT testing if O-RU supports it. This enables a wide variety of equipment to be tested without increasing the number of PTCs
  N/A                                                                                                                                     The capabilities that are not directly relevant to a test configuration or are not expected to be invoked during an IOT test are categorized under N/A

The intent of an IOT Profile Test Configuration is to characterize the
parameters for an interoperability test such that, for a given DUT, the
same result will be obtained irrespective of where the test is conducted
and who conducts the test; future releases of the present document may
amend an IOT Profile Test Configuration description as required to
achieve this intent. In particular, test definitions including parameter
lists as defined by O-RAN shall be complete, and the test creator shall
have no discretion when creating the test but shall follow the test
definitions in the present document exactly. However, in cases where no
IOT Profile Test Configuration matches the needs of the test creator, a
Customized IOT Configuration may be used; see clause 5.1.8 for more
information on the use of Customized IOT Configurations.

The IOT Profiles refer to the specific versions of the CUS-Plane and
M-Plane specifications referenced in clause 2.1 of the present document.

In some cases deployment/implementation specific constraints make it
desirable to customize the parameters in the IOT profiles in this
specification. M-Plane parameters are excluded from customization. To
generate a customized profile, an existing CUS IOT profile is chosen and
Table A.1-2 provides a list of CUS-Plane IOT Profile parameters that may
be modified for the Custom IOT Configuration.

**Table A.1-2: Modifiable and Forbidden CUS-Plane Parameters**

+----------------+----------------+----------------+----------------+
| **Category**   | **Item**       | **Related      |                |
|                |                | O-RAN          |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)**   |                |
+================+================+================+================+
| General        | Radio access   | \-             | Forbidden      |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | Modifiable     |
|                | configuration  |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | Modifiable     |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | Modifiable     |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    | \-             | Modifiable     |
|                | size           |                |                |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | Modifiable     |
|                | bandwidth      |                |                |
+----------------+----------------+----------------+----------------+
|                | Number of      | \-             | Modifiable     |
|                | s              |                |                |
|                | patial/antenna |                |                |
|                | streams        |                |                |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | Modifiable     |
|                | Ethernet link  |                |                |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | Modifiable     |
|                | format         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-RU category  | 4.2.1          | Forbidden      |
+----------------+----------------+----------------+----------------+
|                | LAA            | \-             | Forbidden      |
+----------------+----------------+----------------+----------------+
| \`             | Network delay  | 4.4.4.2        | Forbidden      |
|                | determination  |                |                |
| Delay          |                |                |                |
| management     |                |                |                |
+----------------+----------------+----------------+----------------+
|                | RU adaptation  | 4.4.4.3        | Forbidden      |
|                | of delay       |                |                |
|                | profile        |                |                |
|                | information\   |                |                |
|                | (based on O-DU |                |                |
|                | delay profile  |                |                |
|                | and transport  |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | Forbidden      |
|                | advance type   | Annex B        |                |
+----------------+----------------+----------------+----------------+
|                | T1a_max_up     | 4.4, Annex B   | Forbidden      |
+----------------+----------------+----------------+----------------+
|                | T1a_min_up     | 4.4, Annex B   | Forbidden      |
+----------------+----------------+----------------+----------------+
|                | T2a_max_up     | 4.4, Annex B   | Forbidden      |
+----------------+----------------+----------------+----------------+
|                | T2a_min_up     | 4.4, Annex B   | Forbidden      |
+----------------+----------------+----------------+----------------+
|                | Tcp_adv_dl     | 4.3.2, Annex B | Forbidden      |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Forbidden      |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | Forbidden      |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4, Annex B   | Forbidden      |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4, Annex B   | Forbidden      |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Forbidden      |
|                | (scs=1.25kHz)  |                |                |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | Forbidden      |
|                | (scs=1.25kHz)  |                |                |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4.3-4.4.4,   | Forbidden      |
|                | (scs=1.25kHz)  | Annex B        |                |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4.3-4.4.4,   | Forbidden      |
|                | (scs=1.25kHz)  | Annex B        |                |
+----------------+----------------+----------------+----------------+
|                | T1a_max_cp_ul  | 4.4.3-4.4.4,   | Forbidden      |
|                |                | Annex B        |                |
+----------------+----------------+----------------+----------------+
|                | T1a_min_cp_ul  | 4.4.3-4.4.4,   | Forbidden      |
|                |                | Annex B        |                |
+----------------+----------------+----------------+----------------+
|                | T2a_max_cp_ul  | 4.4.3-4.4.4,   | Forbidden      |
|                |                | Annex B        |                |
+----------------+----------------+----------------+----------------+
|                | T2a_min_cp_ul  | 4.4.3-4.4.4,   | Forbidden      |
|                |                | Annex B        |                |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | Forbidden      |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | Forbidden      |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | Forbidden      |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | Forbidden      |
+----------------+----------------+----------------+----------------+
|                | Non-delay      | 4.4.7          | Forbidden      |
|                | managed        |                |                |
|                | U-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | eAxC ID        | 5.1.3.2.7      | Modifiable     |
| Transport      | DU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | Modifiable     |
|                | BandSector_ID  |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | Modifiable     |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | Modifiable     |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | All other      |                | All other      |
|                | C/U-plane      |                | C/U-plane      |
|                | transport      |                | transport      |
|                | items as       |                | parameters     |
|                | defined in     |                | shall align    |
|                | baseline IOT   |                | with base IOT  |
|                | profile        |                | profile        |
|                |                |                | selected (ie   |
|                |                |                | Forbidden)     |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | Forbidden      |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | All items as   |                | All            |
|                | defined in     |                | Beamforming    |
|                | baseline IOT   |                | parameters     |
|                | profile        |                | shall align    |
|                |                |                | with base IOT  |
|                |                |                | profile        |
|                |                |                | selected (ie   |
|                |                |                | Forbidden)     |
+----------------+----------------+----------------+----------------+
| IQ compression | All items as   |                | All IQ         |
|                | defined in     |                | compression    |
|                | baseline IOT   |                | parameters     |
|                | profile        |                | shall align    |
|                |                |                | with base IOT  |
|                |                |                | profile        |
|                |                |                | selected (ie   |
|                |                |                | Forbidden)     |
+----------------+----------------+----------------+----------------+
| C-Plane        | All items as   |                | All C-plane    |
|                | defined in     |                | parameters     |
|                | baseline IOT   |                | shall align    |
|                | profile        |                | with base IOT  |
|                |                |                | profile        |
|                |                |                | selected (ie   |
|                |                |                | Forbidden)     |
+----------------+----------------+----------------+----------------+
| S-Plane        | All items as   |                | All S-plane    |
|                | defined in     |                | parameters     |
|                | baseline IOT   |                | shall align    |
|                | profile        |                | with base IOT  |
|                |                |                | profile        |
|                |                |                | selected (ie   |
|                |                |                | Forbidden)     |
+----------------+----------------+----------------+----------------+

## A.2 M-Plane IOT Profile

### A.2.1 M-Plane IOT Profile 1 Hierarchical-sudo 

**Table A.2.1-1: Hierarchical-sudo**

+----------------+----------------+----------------+----------------+
| Category       | Item           | Related O-RAN  |                |
|                |                | M-Plane/ YANG  |                |
|                |                | specification  |                |
|                |                | section(s)     |                |
+================+================+================+================+
| High Level     | Architectural  | 5.1.2 M-Plane  | Hierarchical   |
| Description    | models         | architecture   | model          |
|                |                | model          |                |
+----------------+----------------+----------------+----------------+
|                | IP version     | 5.1.3          | IPv4           |
|                |                | Transport      |                |
|                |                | network        |                |
+----------------+----------------+----------------+----------------+
|                | Hash algorithm | 5.4 Security   | HMAC-SHA2-256  |
|                | for data       |                |                |
|                | integrity      |                |                |
+----------------+----------------+----------------+----------------+
|                | Cyphering      | 5.4 Security   | AES128-CTR     |
|                | algorithm      |                |                |
+----------------+----------------+----------------+----------------+
| "Start up"     | O-RU           | 6.2.2 O-RU     | DHCPv4(Option: |
| installation   | identification | identification | 60)            |
|                | by DHCP option | in DHCP        |                |
+----------------+----------------+----------------+----------------+
|                | VLAN Discovery | 6.2.3          | support VLAN   |
|                |                | Management     | SCAN           |
|                |                | plane VLAN     |                |
|                |                | discovery      |                |
|                |                | aspects        |                |
+----------------+----------------+----------------+----------------+
|                | IP address     | 6.2.4 O-RU     | IPv4           |
|                | assignment     | management     | configuration  |
|                |                | plane IP       | using DHCPv4   |
|                |                | address        |                |
|                |                | assignment     |                |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 6.2.5 O-RU     | DHCPv4 option  |
|                | controller     | controller     | 43             |
|                | discovery      | discovery      |                |
+----------------+----------------+----------------+----------------+
|                | DHCP format of | 6.2.5 O-RU     | O-RU           |
|                | O-RU           | controller     | Controller IP  |
|                | controller     | discovery      | Address        |
|                | discovery      |                |                |
+----------------+----------------+----------------+----------------+
|                | NETCONF Call   | 6.3 NETCONF    | call           |
|                | Home           | call home to   | home(port4334) |
|                |                | O-RU           |                |
|                |                | controller(s)  |                |
+----------------+----------------+----------------+----------------+
|                | SSH/TLS        | 6.4 NETCONF    | SSH:           |
|                | Connection     | connection     | password-based |
|                | Establishment  | establishment  | authentication |
+----------------+----------------+----------------+----------------+
|                | TCP port for   | 6.4.1 NETCONF  | SSH: Default   |
|                | SSH/TLS        | security       | (port 830)     |
|                | establishment  |                |                |
|                | (for test      | YANG (4)       |                |
|                | purpose)       | o-ran-m        |                |
|                |                | plane-int.yang |                |
+----------------+----------------+----------------+----------------+
|                | NETCONF        | 6.4.2 NETCONF  | password-based |
|                | Authentication | authentication | authentication |
+----------------+----------------+----------------+----------------+
|                | User Account   | 6.4.3 User     | default sudo   |
|                | Provisioning   | account        |                |
|                |                | provisioning   |                |
+----------------+----------------+----------------+----------------+
|                | sudo           | 6.5 NETCONF    | used           |
|                |                | access control |                |
+----------------+----------------+----------------+----------------+
|                | nms            | 6.5 NETCONF    | not used       |
|                |                | access control |                |
+----------------+----------------+----------------+----------------+
|                | fm-pm          | 6.5 NETCONF    | not used       |
|                |                | access control |                |
+----------------+----------------+----------------+----------------+
|                | swm            | 6.5 NETCONF    | not used       |
|                |                | access control |                |
+----------------+----------------+----------------+----------------+
|                | NETCONF        | 6.6 NETCONF    | yang-library,\ |
|                | capability     | capability     | Wr             |
|                |                | discovery      | itable-running |
|                |                |                | Capability,\   |
|                |                |                | XPATH          |
|                |                |                | capability,\   |
|                |                |                | N              |
|                |                |                | otifications,\ |
|                |                |                | Interleave     |
|                |                |                | capability     |
+----------------+----------------+----------------+----------------+
|                | Watchdog timer | 6.7 Monitoring | used           |
|                |                | NETCONF        |                |
|                |                | connectivity   |                |
+----------------+----------------+----------------+----------------+
| O-RU to O-DU   | VLAN tagging   | 6.2.3          | used for       |
| Interface      | for            | Management     | C/U/M-Plane    |
| Management     | C/U/M-Plane    | plane VLAN     |                |
|                |                | discovery      |                |
|                |                | aspects\       |                |
|                |                | 7.3 C/U-Plane  |                |
|                |                | VLAN           |                |
|                |                | configuration  |                |
+----------------+----------------+----------------+----------------+
|                | C/U-Plane IP   | 7.4 O-RU       | not used       |
|                | Address        | C/U-Plane IP   |                |
|                | Assignment     | address        |                |
|                |                | assignment     |                |
+----------------+----------------+----------------+----------------+
|                | Definition of  | 7.5 Definition | a combination  |
|                | processing     | of processing  | of VLAN        |
|                | elements       | elements       | identity and   |
|                |                |                | MAC address    |
+----------------+----------------+----------------+----------------+
|                | C/U-Plane      | 7.6 O-DU       | Loop-back      |
|                | Transport      | verification   | Protocol       |
|                | Connectivity   | of C/U-Plane   | (LBM/LBR)      |
|                |                | transport      |                |
|                |                | connectivity   |                |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 7.10 O-RU      | not used       |
|                | Monitoring of  | Monitoring of  |                |
|                | C/U-Plane      | C/U-Plane      |                |
|                | Connectivity   | connectivity   |                |
+----------------+----------------+----------------+----------------+
| Configuration  | Baseline       | 9.1 Baseline   | 1 phase        |
| Management     | configuration  | configuration  |                |
+----------------+----------------+----------------+----------------+
| Fault          | subscribe      | 11.3 Manage    | default stream |
| Management     | notification   | alarm          |                |
|                |                | subscription   |                |
|                |                | to NETCONF     |                |
|                |                | clients        |                |
+----------------+----------------+----------------+----------------+
| S              | Sync           | 13.3 Sync      | CLASS_B        |
| ynchronization | Capability     | capability     |                |
| Aspects        | Object         | object         |                |
+----------------+----------------+----------------+----------------+
| Details of     | Activation,    | 15.3.2         | used           |
| O-RU           | deactivation   | Activation,    |                |
| Operations     | and sleep      | deactivation   |                |
|                |                | and sleep      |                |
+----------------+----------------+----------------+----------------+

### A.2.2 M-Plane IOT Profile 2 Hybrid-sudo+nms 

Profile Test Configurations:

-   Hybrid-sudo+nms-\[DHCP\]

-   Hybrid-sudo+nms-\[o-ran-mplane-int.yang\]

**Table A.2.2-1: Hybrid-sudo+nms**

+----------------+----------------+----------------+----------------+
| **Category**   | **Item**       | Related O-RAN  |                |
|                |                | M-Plane/ YANG  |                |
|                |                | specification  |                |
|                |                | section(s)     |                |
+================+================+================+================+
| High Level     | Architectural  | 5.1.2 M-Plane  | Hybrid model   |
| Description    | models         | architecture   |                |
|                |                | model          |                |
+----------------+----------------+----------------+----------------+
|                | IP version     | 5.1.3          | IPv4           |
|                |                | Transport      |                |
|                |                | network        |                |
+----------------+----------------+----------------+----------------+
|                | Hash algorithm | 5.4 Security   | HMAC-SHA2-256  |
|                | for data       |                |                |
|                | integrity      |                |                |
+----------------+----------------+----------------+----------------+
|                | Cyphering      | 5.4 Security   | AES128-CTR     |
|                | algorithm      |                |                |
+----------------+----------------+----------------+----------------+
| "Start up"     | O-RU           | 6.2.2 O-RU     | DHCPv4(Option: |
| installation   | identification | identification | 60)            |
|                | by DHCP option | in DHCP        |                |
+----------------+----------------+----------------+----------------+
|                | VLAN Discovery | 6.2.3          | support VLAN   |
|                |                | Management     | SCAN           |
|                |                | plane VLAN     |                |
|                |                | discovery      |                |
|                |                | aspects        |                |
+----------------+----------------+----------------+----------------+
|                | IP address     | 6.2.4 O-RU     | IPv4           |
|                | assignment     | management     | configuration  |
|                |                | plane IP       | using DHCPv4   |
|                |                | address        |                |
|                |                | assignment     |                |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 6.2.5 O-RU     | Entry 1)       |
|                | controller     | controller     | DHCPv4 option  |
|                | discovery      | discovery      | 43             |
|                |                |                |                |
|                |                |                | Entry 2)       |
|                |                |                | Configured by  |
|                |                |                | o-ran-m        |
|                |                |                | plane-int.yang |
+----------------+----------------+----------------+----------------+
|                | DHCP format of | 6.2.5 O-RU     | O-RU           |
|                | O-RU           | controller     | Controller IP  |
|                | controller     | discovery      | Address        |
|                | discovery      |                |                |
+----------------+----------------+----------------+----------------+
|                | NETCONF Call   | 6.3 NETCONF    | call           |
|                | Home           | call home to   | home(port4334) |
|                |                | O-RU           |                |
|                |                | controller(s)  |                |
+----------------+----------------+----------------+----------------+
|                | SSH/TLS        | 6.4 NETCONF    | SSH:           |
|                | Connection     | connection     | password-based |
|                | Establishment  | establishment  | authentication |
+----------------+----------------+----------------+----------------+
|                | TCP port for   | 6.4.1 NETCONF  | SSH: Default   |
|                | SSH/TLS        | security       | (port 830)     |
|                | establishment  |                |                |
|                | (for test      | YANG (4)       |                |
|                | purpose)       | o-ran-m        |                |
|                |                | plane-int.yang |                |
+----------------+----------------+----------------+----------------+
|                | NETCONF        | 6.4.2NETCONF   | password-based |
|                | Authentication | authentication | authentication |
+----------------+----------------+----------------+----------------+
|                | User Account   | 6.4.3 User     | default sudo   |
|                | Provisioning   | account        |                |
|                |                | provisioning   |                |
+----------------+----------------+----------------+----------------+
|                | sudo           | 6.5 NETCONF    | used           |
|                |                | access control |                |
+----------------+----------------+----------------+----------------+
|                | nms            | 6.5 NETCONF    | used           |
|                |                | access control |                |
+----------------+----------------+----------------+----------------+
|                | fm-pm          | 6.5 NETCONF    | not used       |
|                |                | access control |                |
+----------------+----------------+----------------+----------------+
|                | swm            | 6.5 NETCONF    | not used       |
|                |                | access control |                |
+----------------+----------------+----------------+----------------+
|                | NETCONF        | 6.6 NETCONF    | yang-library,\ |
|                | capability     | capability     | Wr             |
|                |                | discovery      | itable-running |
|                |                |                | Capability,\   |
|                |                |                | XPATH          |
|                |                |                | capability,\   |
|                |                |                | N              |
|                |                |                | otifications,\ |
|                |                |                | Interleave     |
|                |                |                | capability     |
+----------------+----------------+----------------+----------------+
|                | Watchdog timer | 6.7 Monitoring | used           |
|                |                | NETCONF        |                |
|                |                | connectivity   |                |
+----------------+----------------+----------------+----------------+
| O-RU to O-DU   | VLAN tagging   | 6.2.3          | used for       |
| Interface      | for            | Management     | C/U/M-Plane    |
| Management     | C/U/M-Plane    | plane VLAN     |                |
|                |                | discovery      |                |
|                |                | aspects\       |                |
|                |                | 7.3 C/U-Plane  |                |
|                |                | VLAN           |                |
|                |                | configuration  |                |
+----------------+----------------+----------------+----------------+
|                | C/U-Plane IP   | 7.4 O-RU       | not used       |
|                | Address        | C/U-Plane IP   |                |
|                | Assignment     | address        |                |
|                |                | assignment     |                |
+----------------+----------------+----------------+----------------+
|                | Definition of  | 7.5 Definition | a combination  |
|                | processing     | of processing  | of VLAN        |
|                | elements       | elements       | identity and   |
|                |                |                | MAC address    |
+----------------+----------------+----------------+----------------+
|                | C/U-Plane      | 7.6 O-DU       | Loop-back      |
|                | Transport      | verification   | Protocol       |
|                | Connectivity   | of C/U-Plane   | (LBM/LBR)      |
|                |                | transport      |                |
|                |                | connectivity   |                |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 7.10 O-RU      | not used       |
|                | Monitoring of  | monitoring of  |                |
|                | C/U-Plane      | C/U-Plane      |                |
|                | Connectivity   | connectivity   |                |
+----------------+----------------+----------------+----------------+
| Configuration  | Baseline       | 9.1 Baseline   | 1 phase        |
| Management     | configuration  | configuration  |                |
+----------------+----------------+----------------+----------------+
| Fault          | subscribe      | 11.3 Manage    | default stream |
| Management     | notification   | alarm          |                |
|                |                | subscription   |                |
|                |                | to NETCONF     |                |
|                |                | clients        |                |
+----------------+----------------+----------------+----------------+
| S              | Sync           | 13.3 Sync      | CLASS_B        |
| ynchronization | Capability     | capability     |                |
| Aspects        | Object         | object         |                |
+----------------+----------------+----------------+----------------+
| Details of     | Activation,    | 15.3.2         | not used       |
| O-RU           | deactivation   | Activation,    |                |
| Operations     | and sleep      | deactivation   |                |
|                |                | and sleep      |                |
+----------------+----------------+----------------+----------------+

### A.2.3 M-Plane IOT Profile 3 Hierarchical-sudo-IPv6 

Profile Test Configurations:

-   Hierarchical-sudo-IPv6\_\[SSH-IPaddStateFull-SyncENHANCED\]

-   Hierarchical-sudo-IPv6\_\[SSH- IPaddStateless-SyncENHANCED\]

-   Hierarchical-sudo-IPv6\_\[TLS- IPaddStateFull-SyncCLASS_B\]

-   Hierarchical-sudo-IPv6\_\[TLS- IPaddStateless-SyncCLASS_B\]

**Table A.2.3-1:** **Hierarchical-sudo-IPv6**

+----------------+----------------+----------------+----------------+
| Category       | Item           | Related O-RAN  |                |
|                |                | M-Plane/ YANG  |                |
|                |                | specification  |                |
|                |                | section(s)     |                |
+================+================+================+================+
| High Level     | Architectural  | 5.1.2 M-Plane  | Hierarchical   |
| Description    | models         | architecture   | model          |
|                |                | model          |                |
+----------------+----------------+----------------+----------------+
|                | IP version     | 5.1.3          | IPv6           |
|                |                | Transport      |                |
|                |                | network        |                |
+----------------+----------------+----------------+----------------+
|                | Hash algorithm | 5.4 Security   | Entry 1) SSHv2 |
|                | for data       |                | -HMAC-SHA2-256 |
|                | integrity      |                |                |
|                |                |                | Entry 2)       |
|                |                |                | TLS1.2 -       |
|                |                |                | SHA256         |
+----------------+----------------+----------------+----------------+
|                | Cyphering      | 5.4 Security   | Entry 1) SSHv2 |
|                | algorithm      |                | - AES128-CTR   |
|                |                |                |                |
|                |                |                | Entry 2)       |
|                |                |                | TLS1.2         |
|                |                |                | -AES128-GCM    |
+----------------+----------------+----------------+----------------+
| "Start up"     | O-RU           | 6.2.2 O-RU     | DHCPv6         |
| installation   | identification | identification | (Option: 16)   |
|                | by DHCP option | in DHCP        |                |
+----------------+----------------+----------------+----------------+
|                | VLAN Discovery | 6.2.3          | support VLAN   |
|                |                | Management     | SCAN           |
|                |                | plane VLAN     |                |
|                |                | discovery      |                |
|                |                | aspects        |                |
+----------------+----------------+----------------+----------------+
|                | IP address     | 6.2.4 O-RU     | Entry 1)       |
|                | assignment     | management     | State-full     |
|                |                | plane IP       | address        |
|                |                | address        | configuration  |
|                |                | assignment     |                |
|                |                |                | Entry 2)       |
|                |                |                | Stateless      |
|                |                |                | Address        |
|                |                |                | Auto           |
|                |                |                | -Configuration |
|                |                |                | (SLAAC)        |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 6.2.5 O-RU     | DHCPv6         |
|                | controller     | controller     | (Option: 17)   |
|                | discovery      | discovery      |                |
+----------------+----------------+----------------+----------------+
|                | DHCP format of | 6.2.5 O-RU     | O-RU           |
|                | O-RU           | controller     | Controller IP  |
|                | controller     | discovery      | Address        |
|                | discovery      |                |                |
+----------------+----------------+----------------+----------------+
|                | NETCONF Call   | 6.3 NETCONF    | Entry 1) SSH - |
|                | Home           | call home to   | call home      |
|                |                | O-RU           | port:4334      |
|                |                | controller(s)  |                |
|                |                |                | Entry 2) TLS - |
|                |                |                | call home port |
|                |                |                | 4335           |
+----------------+----------------+----------------+----------------+
|                | SSH/TLS        | 6.4 NETCONF    | Entry 1) SSH - |
|                | Connection     | connection     | password-based |
|                | Establishment  | establishment  | authentication |
|                |                |                |                |
|                |                |                | Entry 2) TLS - |
|                |                |                | X.509          |
|                |                |                | Certificate    |
+----------------+----------------+----------------+----------------+
|                | TCP port for   | 6.4.1 NETCONF  | Entry 1) SSH   |
|                | SSH/TLS        | security       | Default (port  |
|                | establishment  |                | 830)           |
|                | (for test      | YANG (4)       |                |
|                | purpose)       | o-ran-m        | Entry 2) TLS   |
|                |                | plane-int.yang | Default (port  |
|                |                |                | 6513)          |
+----------------+----------------+----------------+----------------+
|                | NETCONF        | 6.4.2 NETCONF  | Entry 1) SSH   |
|                | Authentication | authentication | password-based |
|                |                |                | authentication |
|                |                |                |                |
|                |                |                | Entry 2) TLS - |
|                |                |                | X.509          |
|                |                |                | Certificate    |
+----------------+----------------+----------------+----------------+
|                | User Account   | 6.4.3 User     | default sudo   |
|                | Provisioning   | account        |                |
|                |                | provisioning   |                |
+----------------+----------------+----------------+----------------+
|                | sudo           | 6.5 NETCONF    | used           |
|                |                | access control |                |
+----------------+----------------+----------------+----------------+
|                | nms            | 6.5 NETCONF    | not used       |
|                |                | access control |                |
+----------------+----------------+----------------+----------------+
|                | fm-pm          | 6.5 NETCONF    | not used       |
|                |                | access control |                |
+----------------+----------------+----------------+----------------+
|                | swm            | 6.5 NETCONF    | not used       |
|                |                | access control |                |
+----------------+----------------+----------------+----------------+
|                | NETCONF        | 6.6 NETCONF    | yang-library,\ |
|                | capability     | capability     | Wr             |
|                |                | discovery      | itable-running |
|                |                |                | Capability,    |
|                |                |                |                |
|                |                |                | rollback on    |
|                |                |                | error,\        |
|                |                |                | XPATH          |
|                |                |                | capability,\   |
|                |                |                | N              |
|                |                |                | otifications,\ |
|                |                |                | Interleave     |
|                |                |                | capability     |
+----------------+----------------+----------------+----------------+
|                | Watchdog timer | 6.7 Monitoring | used           |
|                |                | NETCONF        |                |
|                |                | connectivity   |                |
+----------------+----------------+----------------+----------------+
| O-RU to O-DU   | VLAN tagging   | 6.2.3          | used for       |
| Interface      | for            | Management     | C/U/M-Plane    |
| Management     | C/U/M-Plane    | plane VLAN     |                |
|                |                | discovery      |                |
|                |                | aspects\       |                |
|                |                | 7.3 C/U-Plane  |                |
|                |                | VLAN           |                |
|                |                | configuration  |                |
+----------------+----------------+----------------+----------------+
|                | C/U-Plane IP   | 7.4 O-RU       | not used       |
|                | Address        | C/U-Plane IP   |                |
|                | Assignment     | address        |                |
|                |                | assignment     |                |
+----------------+----------------+----------------+----------------+
|                | Definition of  | 7.5 Definition | a combination  |
|                | processing     | of processing  | of VLAN        |
|                | elements       | elements       | identity and   |
|                |                |                | MAC address    |
+----------------+----------------+----------------+----------------+
|                | C/U-Plane      | 7.6 O-DU       | Loop-back      |
|                | Transport      | verification   | Protocol       |
|                | Connectivity   | of C/U-Plane   | (LBM/LBR)      |
|                |                | transport      |                |
|                |                | connectivity   |                |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 7.10 O-RU      | not used       |
|                | Monitoring of  | monitoring of  |                |
|                | C/U-Plane      | C/U-Plane      |                |
|                | Connectivity   | connectivity   |                |
+----------------+----------------+----------------+----------------+
| Configuration  | Baseline       | 9.1 Baseline   | 1 phase        |
| Management     | configuration  | configuration  |                |
+----------------+----------------+----------------+----------------+
| Fault          | subscribe      | 11.3 Manage    | default stream |
| Management     | notification   | alarm          |                |
|                |                | subscription   |                |
|                |                | to NETCONF     |                |
|                |                | clients        |                |
+----------------+----------------+----------------+----------------+
| S              | Sync           | 13.3 Sync      | Entry 1:       |
| ynchronization | Capability     | capability     | CLASS_B        |
| Aspects        | Object         | object         |                |
|                |                |                | Entry 2:       |
|                |                |                | ENHANCED       |
+----------------+----------------+----------------+----------------+
| Details of     | Activation,    | 15.3.2         | used           |
| O-RU           | deactivation   | Activation,    |                |
| Operations     | and sleep      | deactivation   |                |
|                |                | and sleep      |                |
+----------------+----------------+----------------+----------------+

### A.2.4 M-Plane IOT Profile 4 Hybrid-sudo+nms-IPv6 

Profile Test Configurations:

-   Hybrid-sudo+nms-IPv6\_\[SSH-IPaddStateFull-SyncENHANCED-DHCP\]

-   Hybrid-sudo+nms-IPv6\_\[SSH- IPaddStateless-SyncENHANCED-DHCP\]

-   Hybrid-sudo+nms-IPv6\_\[TLS- IPaddStateFull-SyncCLASS_B-DHCP\]

-   Hybrid-sudo+nms-IPv6\_\[TLS- IPaddStateless-SyncCLASS_B-DHCP\]

-   Hybrid-sudo+nms-IPv6\_\[TLS- IPaddStateFull-SyncCLASS_B-int.yang\]

**Table A.2.4-1: Hybrid-sudo+nms-IPv6**

+----------------+----------------+----------------+----------------+
| Category       | Item           | Related O-RAN  |                |
|                |                | M-Plane/ YANG  |                |
|                |                | specification  |                |
|                |                | section(s)     |                |
+================+================+================+================+
| High Level     | Architectural  | 5.1.2 M-Plane  | Hybrid model   |
| Description    | models         | architecture   |                |
|                |                | model          |                |
+----------------+----------------+----------------+----------------+
|                | IP version     | 5.1.3          | IPv6           |
|                |                | Transport      |                |
|                |                | network        |                |
+----------------+----------------+----------------+----------------+
|                | Hash algorithm | 5.4 Security   | Entry 1) SSHv2 |
|                | for data       |                | -HMAC-SHA2-256 |
|                | integrity      |                |                |
|                |                |                | Entry 2)       |
|                |                |                | TLS1.2 -       |
|                |                |                | SHA256         |
+----------------+----------------+----------------+----------------+
|                | Cyphering      | 5.4 Security   | Entry 1) SSHv2 |
|                | algorithm      |                | - AES128-CTR   |
|                |                |                |                |
|                |                |                | Entry 2)       |
|                |                |                | TLS1.2         |
|                |                |                | -AES128-GCM    |
+----------------+----------------+----------------+----------------+
| "Start up"     | O-RU           | 6.2.2 O-RU     | DHCPv6         |
| installation   | identification | identification | (Option: 16)   |
|                | by DHCP option | in DHCP        |                |
+----------------+----------------+----------------+----------------+
|                | VLAN Discovery | 6.2.3          | support VLAN   |
|                |                | Management     | SCAN           |
|                |                | plane VLAN     |                |
|                |                | discovery      |                |
|                |                | aspects        |                |
+----------------+----------------+----------------+----------------+
|                | IP address     | 6.2.4 O-RU     | Entry 1)       |
|                | assignment     | Management     | State-full     |
|                |                | plane IP       | address        |
|                |                | address        | configuration  |
|                |                | assignment     |                |
|                |                |                | Entry 2)       |
|                |                |                | Stateless      |
|                |                |                | Address        |
|                |                |                | Auto           |
|                |                |                | -Configuration |
|                |                |                | (SLAAC)        |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 6.2.5 O-RU     | Entry 1)       |
|                | controller     | controller     | DHCPv6         |
|                | discovery      | discovery      | (Option: 17)   |
|                |                |                |                |
|                |                |                | Entry 2)       |
|                |                |                | Configured by  |
|                |                |                | o-ran-m        |
|                |                |                | plane-int.yang |
+----------------+----------------+----------------+----------------+
|                | DHCP format of | 6.2.5 O-RU     | O-RU           |
|                | O-RU           | controller     | Controller IP  |
|                | controller     | discovery      | Address        |
|                | discovery      |                |                |
+----------------+----------------+----------------+----------------+
|                | NETCONF Call   | 6.3 NETCONF    | Entry 1) SSH - |
|                | Home           | call home to   | call home      |
|                |                | O-RU           | port:4334      |
|                |                | controller(s)  |                |
|                |                |                | Entry 2) TLS - |
|                |                |                | call home port |
|                |                |                | 4335           |
+----------------+----------------+----------------+----------------+
|                | SSH/TLS        | 6.4 NETCONF    | Entry 1) SSH - |
|                | Connection     | connection     | password-based |
|                | Establishment  | establishment  | authentication |
|                |                |                |                |
|                |                |                | Entry 2) TLS - |
|                |                |                | X.509          |
|                |                |                | Certificate    |
+----------------+----------------+----------------+----------------+
|                | TCP port for   | 6.4.1 NETCONF  | Entry 1) SSH   |
|                | SSH/TLS        | security       | Default (port  |
|                | establishment  |                | 830)           |
|                | (for test      | YANG (4)       |                |
|                | purpose)       | o-ran-m        | Entry 2) TLS   |
|                |                | plane-int.yang | Default (port  |
|                |                |                | 6513)          |
+----------------+----------------+----------------+----------------+
|                | NETCONF        | 6.4.2 NETCONF  | Entry 1) SSH   |
|                | Authentication | authentication | password-based |
|                |                |                | authentication |
|                |                |                |                |
|                |                |                | Entry 2) TLS - |
|                |                |                | X.509          |
|                |                |                | Certificate    |
+----------------+----------------+----------------+----------------+
|                | User Account   | 6.4.3 User     | default sudo   |
|                | Provisioning   | account        |                |
|                |                | provisioning   |                |
+----------------+----------------+----------------+----------------+
|                | sudo           | 6.5 NETCONF    | used           |
|                |                | access control |                |
+----------------+----------------+----------------+----------------+
|                | nms            | 6.5 NETCONF    | used           |
|                |                | access control |                |
+----------------+----------------+----------------+----------------+
|                | fm-pm          | 6.5 NETCONF    | not used       |
|                |                | access control |                |
+----------------+----------------+----------------+----------------+
|                | swm            | 6.5 NETCONF    | not used       |
|                |                | access control |                |
+----------------+----------------+----------------+----------------+
|                | NETCONF        | 6.6 NETCONF    | yang-library,\ |
|                | capability     | capability     | Wr             |
|                |                | discovery      | itable-running |
|                |                |                | Capability,    |
|                |                |                |                |
|                |                |                | rollback on    |
|                |                |                | error,\        |
|                |                |                | XPATH          |
|                |                |                | capability,\   |
|                |                |                | N              |
|                |                |                | otifications,\ |
|                |                |                | Interleave     |
|                |                |                | capability     |
+----------------+----------------+----------------+----------------+
|                | Watchdog timer | 6.7 Monitoring | used           |
|                |                | NETCONF        |                |
|                |                | connectivity   |                |
+----------------+----------------+----------------+----------------+
| O-RU to O-DU   | VLAN tagging   | 6.2.3          | used for       |
| Interface      | for            | Management     | C/U/M-Plane    |
| Management     | C/U/M-Plane    | plane VLAN     |                |
|                |                | discovery      |                |
|                |                | aspects\       |                |
|                |                | 7.3 C/U-Plane  |                |
|                |                | VLAN           |                |
|                |                | configuration  |                |
+----------------+----------------+----------------+----------------+
|                | C/U-Plane IP   | 7.4 O-RU       | not used       |
|                | Address        | C/U-Plane IP   |                |
|                | Assignment     | address        |                |
|                |                | assignment     |                |
+----------------+----------------+----------------+----------------+
|                | Definition of  | 7.5 Definition | a combination  |
|                | processing     | of processing  | of VLAN        |
|                | elements       | elements       | identity and   |
|                |                |                | MAC address    |
+----------------+----------------+----------------+----------------+
|                | C/U-Plane      | 7.6 O-DU       | Loop-back      |
|                | Transport      | verification   | Protocol       |
|                | Connectivity   | of C/U-Plane   | (LBM/LBR)      |
|                |                | transport      |                |
|                |                | connectivity   |                |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 7.10 O-RU      | not used       |
|                | Monitoring of  | monitoring of  |                |
|                | C/U-Plane      | C/U-Plane      |                |
|                | Connectivity   | connectivity   |                |
+----------------+----------------+----------------+----------------+
| Configuration  | Baseline       | 9.1 Baseline   | 1 phase        |
| Management     | configuration  | configuration  |                |
+----------------+----------------+----------------+----------------+
| Fault          | subscribe      | 11.3 Manage    | default stream |
| Management     | notification   | alarm          |                |
|                |                | subscription   |                |
|                |                | to NETCONF     |                |
|                |                | clients        |                |
+----------------+----------------+----------------+----------------+
| S              | Sync           | 13.3 Sync      | Entry 1:       |
| ynchronization | Capability     | capability     | CLASS_B        |
| Aspects        | Object         | object         |                |
|                |                |                | Entry 2:       |
|                |                |                | ENHANCED       |
+----------------+----------------+----------------+----------------+
| Details of     | Activation,    | 15.3.2         | not used       |
| O-RU           | deactivation   | Activation,    |                |
| Operations     | and sleep      | deactivation   |                |
|                |                | and sleep      |                |
+----------------+----------------+----------------+----------------+

## A.3 CUS-Plane IOT Profiles

### A.3.1 NR TDD 

#### A.3.1.1 NR TDD IOT Profile 1 - NR-TDD-FR1-CAT-A-NoBF

Profile Test Configurations:

-   NR-TDD-FR1-CAT-A-NoBF\_\[ConfigDDDSUUDDDD-4SS-14bitIQ-25Gbpsx1lane-PRACHB4-eAxCID2644-llsC1C2\]

-   NR-TDD-FR1-CAT-A-NoBF\_\[ConfigDDDSUUDDDD-4SS-14bitIQ-25Gbpsx1lane-PRACHF0-eAxCID2644-llsC1C2\]

-   NR-TDD-FR1-CAT-A-NoBF\_\[ConfigDDDSUUDSUU-4SS-14bitIQ-25Gbpsx1lane-PRACHB4-eAxCID2644-llsC1C2\]

-   NR-TDD-FR1-CAT-A-NoBF\_\[ConfigDDDSUUDSUU-4SS-14bitIQ-25Gbpsx1lane-PRACHF0-eAxCID2644-llsC1C2\]

-   NR-TDD-FR1-CAT-A-NoBF\_\[ConfigDDDSUUDDDD-4SS-14bitIQ-10Gbpsx2lane-PRACHC2-eAxCID4246-llsC1C2\]

-   NR-TDD-FR1-CAT-A-NoBF\_\[ConfigDDDDDDDSUU-2SS-8bitIQ-10Gbpsx1lane-PRACHF0-eAxCID2644-llsC1C2\]

-   NR-TDD-FR1-CAT-A-NoBF\_\[ConfigDDDDDDDSUU-4SS-8bitIQ-10Gbpsx1lane-PRACHB4-eAxCID2644-llsC1C2\]

-   NR-TDD-FR1-CAT-A-NoBF\_\[ConfigDDDSUDDDSU-4SS-9bitIQ-10Gbpsx1lane-PRACHC2-eAxCID2644-llsC3\]

**Table A.3.1.1-1: NR TDD IOT Profile 1 - NR-TDD-FR1-CAT-A-NoBF**

+----------------+----------------+----------------+----------------+
| **Category**   | **Item**       | **Related      |                |
|                |                | O-RAN          |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)**   |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR TDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | Entry1:        |
|                | configuration  |                |                |
|                |                |                | pattern1{\     |
|                |                |                | d              |
|                |                |                | l-UL-Transmiss |
|                |                |                | ionPeriodicity |
|                |                |                | ms3\           |
|                |                |                | nro            |
|                |                |                | fDownlinkSlots |
|                |                |                | 3\             |
|                |                |                | nrofD          |
|                |                |                | ownlinkSymbols |
|                |                |                | 6\             |
|                |                |                | n              |
|                |                |                | rofUplinkSlots |
|                |                |                | 2\             |
|                |                |                | nro            |
|                |                |                | fUplinkSymbols |
|                |                |                | 4}\            |
|                |                |                | \              |
|                |                |                | pattern2{\     |
|                |                |                | d              |
|                |                |                | l-UL-Transmiss |
|                |                |                | ionPeriodicity |
|                |                |                | ms2\           |
|                |                |                | nro            |
|                |                |                | fDownlinkSlots |
|                |                |                | 4\             |
|                |                |                | nrofD          |
|                |                |                | ownlinkSymbols |
|                |                |                | 0\             |
|                |                |                | n              |
|                |                |                | rofUplinkSlots |
|                |                |                | 0\             |
|                |                |                | nro            |
|                |                |                | fUplinkSymbols |
|                |                |                | 0}             |
|                |                |                |                |
|                |                |                | Entry2:\       |
|                |                |                | d              |
|                |                |                | l-UL-Transmiss |
|                |                |                | ionPeriodicity |
|                |                |                | ms5\           |
|                |                |                | nro            |
|                |                |                | fDownlinkSlots |
|                |                |                | 7\             |
|                |                |                | nrofD          |
|                |                |                | ownlinkSymbols |
|                |                |                | 6\             |
|                |                |                | n              |
|                |                |                | rofUplinkSlots |
|                |                |                | 2\             |
|                |                |                | nro            |
|                |                |                | fUplinkSymbols |
|                |                |                | 4              |
|                |                |                |                |
|                |                |                | Entry3:        |
|                |                |                |                |
|                |                |                | d              |
|                |                |                | l-UL-Transmiss |
|                |                |                | ionPeriodicity |
|                |                |                | ms2p5          |
|                |                |                |                |
|                |                |                | nro            |
|                |                |                | fDownlinkSlots |
|                |                |                | 3              |
|                |                |                |                |
|                |                |                | nrofD          |
|                |                |                | ownlinkSymbols |
|                |                |                | 10             |
|                |                |                |                |
|                |                |                | n              |
|                |                |                | rofUplinkSlots |
|                |                |                | 1              |
|                |                |                |                |
|                |                |                | nro            |
|                |                |                | fUplinkSymbols |
|                |                |                | 2              |
|                |                |                |                |
|                |                |                | Entry4:        |
|                |                |                |                |
|                |                |                | pattern1{\     |
|                |                |                | d              |
|                |                |                | l-UL-Transmiss |
|                |                |                | ionPeriodicity |
|                |                |                | ms3\           |
|                |                |                | nro            |
|                |                |                | fDownlinkSlots |
|                |                |                | 3\             |
|                |                |                | nrofD          |
|                |                |                | ownlinkSymbols |
|                |                |                | 6\             |
|                |                |                | n              |
|                |                |                | rofUplinkSlots |
|                |                |                | 2\             |
|                |                |                | nro            |
|                |                |                | fUplinkSymbols |
|                |                |                | 4}\            |
|                |                |                | \              |
|                |                |                | pattern2{\     |
|                |                |                | d              |
|                |                |                | l-UL-Transmiss |
|                |                |                | ionPeriodicity |
|                |                |                | ms2\           |
|                |                |                | nro            |
|                |                |                | fDownlinkSlots |
|                |                |                | 1\             |
|                |                |                | nrofD          |
|                |                |                | ownlinkSymbols |
|                |                |                | 10\            |
|                |                |                | n              |
|                |                |                | rofUplinkSlots |
|                |                |                | 2\             |
|                |                |                | nro            |
|                |                |                | fUplinkSymbols |
|                |                |                | 0}             |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 30 kHz         |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | 30 kHz         |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    | \-             | 4096           |
|                | size           |                |                |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | 100MHz x 1CC   |
|                | bandwidth      |                |                |
+----------------+----------------+----------------+----------------+
|                | Number of      | \-             | Entry1: 2      |
|                | s              |                |                |
|                | patial/antenna |                | Entry2: 4      |
|                | streams        |                |                |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | Entry1: 25Gbps |
|                | Ethernet link  |                | x 1lane\       |
|                |                |                | Entry2: 10Gbps |
|                |                |                | x 2lane        |
|                |                |                |                |
|                |                |                | Entry3: 10Gbps |
|                |                |                | x 1lane        |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | Entry1: B4\    |
|                | format         |                | Entry2: C2     |
|                |                |                |                |
|                |                |                | Entry3: Long   |
|                |                |                | preamble F0    |
+----------------+----------------+----------------+----------------+
|                | RU category    | 4.2.1          | Category A     |
+----------------+----------------+----------------+----------------+
|                | LAA            | \-             | FALSE          |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4.2        | Defined        |
| management     | determination  |                | Transport      |
|                |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | RU adaptation  | 4.4.4.3        | FALSE          |
|                | of delay       |                |                |
|                | profile        |                |                |
|                | information\   |                |                |
|                | (based on O-DU |                |                |
|                | delay profile  |                |                |
|                | and transport  |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | Fixed Timing   |
|                | advance type   | Annex B        | Advance        |
+----------------+----------------+----------------+----------------+
|                | T1a_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 345us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 294us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 345us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 134us |
+----------------+----------------+----------------+----------------+
|                | Tcp_adv_dl     | 4.3.2, Annex B | 125 us         |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 171us |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 50us  |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 331us |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 50us  |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                | (scs=1.25kHz)  |                | equal to       |
|                |                |                | 1650us         |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                | (scs=1.25kHz)  |                | equal to 827us |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4.3-4.4.4,   | More than or   |
|                | (scs=1.25kHz)  | Annex B        | equal to       |
|                |                |                | 1810us         |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4.3-4.4.4,   | Less than or   |
|                | (scs=1.25kHz)  | Annex B        | equal to 827us |
+----------------+----------------+----------------+----------------+
|                | T1a_max_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 336us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 285us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 336us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 125us |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | Non-delay      | 4.4.7          | FALSE          |
|                | managed        |                |                |
|                | U-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | eCPRI          |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5              | FALSE          |
|                | concatenation  | .1.3.1-5.1.3.2 |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | Entry1: 2\     |
|                | DU_Port_ID     |                | Entry2: 4      |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | Entry1: 6\     |
|                | BandSector_ID  |                | Entry2: 2      |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | 4              |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | Entry1: 4\     |
|                | RU_Port_ID     |                | Entry2: 6      |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | priority       |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | False (Default |
|                | prioritization |                | U-Plane        |
|                | within U-Plane |                | priority       |
|                |                |                | applies)       |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID        |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | FALSE          |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0dB            |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | RU beamforming | 4.2.1..(10.1)  | No beamforming |
|                | type           |                |                |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.3, Annex J   | Beamforming ID |
|                | control method |                | based (always  |
|                |                |                | \"0\")         |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | Block floating |
|                | compression    |                | point          |
|                | method         |                |                |
+----------------+----------------+----------------+----------------+
|                | U-Plane data   | 8, Annex D     | Entry1: 8      |
|                | IQ bitwidth    |                |                |
|                |                |                | Entry2: 14     |
|                |                |                |                |
|                |                |                | Entry3: 9      |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | TRUE           |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | FALSE (always  |
|                | flag           |                | set to \'0\')  |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | Single C-Plane |
|                | PRACH formats  |                | message        |
|                | with preamble  |                |                |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | FALSE          |
|                | extension 1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | FALSE          |
|                | extension 2    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | FALSE          |
|                | extension 3    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | FALSE          |
|                | extension 4    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | FALSE          |
|                | extension 5    |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | TRUE           |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | FALSE          |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | FALSE          |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2         | Entry1: lls-C1 |
|                | configuration  |                | (can also      |
|                |                | 10, 11.2.3     | apply lls-C2)  |
|                |                | (for PLFS)     |                |
|                |                |                | Entry2: lls-C3 |
+----------------+----------------+----------------+----------------+

#### A.3.1.2 NR TDD IOT Profile 2 - NR-TDD-FR1-CAT-A-DBF

Profile Test Configurations:

-   NR-TDD-FR1-CAT-A-DBF\_\[ConfigDDDSUUDDDD-100MHz-PRACHB4-llsC1C2\]

-   NR-TDD-FR1-CAT-A-DBF\_\[ConfigDDDSUUDDDD-100MHz- PRACHF0-llsC1C2\]

-   NR-TDD-FR1-CAT-A-DBF\_\[ConfigDDDSUUDSUU-100MHz-PRACHB4-llsC1C2\]

-   NR-TDD-FR1-CAT-A-DBF\_\[ConfigDDDSUUDSUU-100MHz- PRACHF0-llsC1C2\]

-   NR-TDD-FR1-CAT-A-DBF\_\[ConfigDDDSUUDDDD- 80MHz-PRACHB4-llsC3\]

**Table A.3.1.2-1: NR TDD IOT Profile 2 - NR-TDD-FR1-CAT-A-DBF**

+----------------+----------------+----------------+----------------+
| **Category**   | **Item**       | **Related      |                |
|                |                | O-RAN          |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)**   |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR TDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | Entry1:        |
|                | configuration  |                |                |
|                |                |                | pattern1{\     |
|                |                |                | d              |
|                |                |                | l-UL-Transmiss |
|                |                |                | ionPeriodicity |
|                |                |                | ms3\           |
|                |                |                | nro            |
|                |                |                | fDownlinkSlots |
|                |                |                | 3\             |
|                |                |                | nrofD          |
|                |                |                | ownlinkSymbols |
|                |                |                | 6\             |
|                |                |                | n              |
|                |                |                | rofUplinkSlots |
|                |                |                | 2\             |
|                |                |                | nro            |
|                |                |                | fUplinkSymbols |
|                |                |                | 4}\            |
|                |                |                | \              |
|                |                |                | pattern2{\     |
|                |                |                | d              |
|                |                |                | l-UL-Transmiss |
|                |                |                | ionPeriodicity |
|                |                |                | ms2\           |
|                |                |                | nro            |
|                |                |                | fDownlinkSlots |
|                |                |                | 4\             |
|                |                |                | nrofD          |
|                |                |                | ownlinkSymbols |
|                |                |                | 0\             |
|                |                |                | n              |
|                |                |                | rofUplinkSlots |
|                |                |                | 0\             |
|                |                |                | nro            |
|                |                |                | fUplinkSymbols |
|                |                |                | 0}             |
|                |                |                |                |
|                |                |                | Entry2:        |
|                |                |                |                |
|                |                |                | pattern1{\     |
|                |                |                | d              |
|                |                |                | l-UL-Transmiss |
|                |                |                | ionPeriodicity |
|                |                |                | ms3\           |
|                |                |                | nro            |
|                |                |                | fDownlinkSlots |
|                |                |                | 3              |
|                |                |                |                |
|                |                |                | nrofD          |
|                |                |                | ownlinkSymbols |
|                |                |                | 6\             |
|                |                |                | n              |
|                |                |                | rofUplinkSlots |
|                |                |                | 2\             |
|                |                |                | nro            |
|                |                |                | fUplinkSymbols |
|                |                |                | 4}\            |
|                |                |                | \              |
|                |                |                | pattern2{\     |
|                |                |                | d              |
|                |                |                | l-UL-Transmiss |
|                |                |                | ionPeriodicity |
|                |                |                | ms2\           |
|                |                |                | nro            |
|                |                |                | fDownlinkSlots |
|                |                |                | 1\             |
|                |                |                | nrofD          |
|                |                |                | ownlinkSymbols |
|                |                |                | 10\            |
|                |                |                | n              |
|                |                |                | rofUplinkSlots |
|                |                |                | 2\             |
|                |                |                | nro            |
|                |                |                | fUplinkSymbols |
|                |                |                | 0}             |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 30 kHz         |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | 30 kHz         |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    | \-             | 4096           |
|                | size           |                |                |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | Entry1: 100MHz |
|                | bandwidth      |                | x 1CC          |
|                |                |                |                |
|                |                |                | Entry2: 80MHz  |
|                |                |                | x 1CC          |
+----------------+----------------+----------------+----------------+
|                | Number of      | \-             | 4              |
|                | s              |                |                |
|                | patial/antenna |                |                |
|                | streams        |                |                |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 25Gbps x 1lane |
|                | Ethernet link  |                |                |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | Entry1: B4     |
|                | format         |                |                |
|                |                |                | Entry2: Long   |
|                |                |                | preamble F0    |
+----------------+----------------+----------------+----------------+
|                | RU category    | 4.2.1          | Category A     |
+----------------+----------------+----------------+----------------+
|                | LAA            | \-             | FALSE          |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4.2        | Defined        |
| management     | determination  |                | Transport      |
|                |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | RU adaptation  | 4.4.4.3        | FALSE          |
|                | of delay       |                |                |
|                | profile        |                |                |
|                | information\   |                |                |
|                | (based on O-DU |                |                |
|                | delay profile  |                |                |
|                | and transport  |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | Fixed Timing   |
|                | advance type   | Annex B        | Advance        |
+----------------+----------------+----------------+----------------+
|                | T1a_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 345us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 294us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 345us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 134us |
+----------------+----------------+----------------+----------------+
|                | Tcp_adv_dl     | 4.3.2, Annex B | 125 us         |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 171us |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 50us  |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 331us |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 50us  |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                | (scs=1.25kHz)  |                | equal to       |
|                |                |                | 1650us         |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                | (scs=1.25kHz)  |                | equal to 827us |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4.3-4.4.4,   | More than or   |
|                | (scs=1.25kHz)  | Annex B        | equal to       |
|                |                |                | 1810us         |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4.3-4.4.4,   | Less than or   |
|                | (scs=1.25kHz)  | Annex B        | equal to 827us |
+----------------+----------------+----------------+----------------+
|                | T1a_max_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 336us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 285us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 336us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 125us |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | Non-delay      | 4.4.7          | FALSE          |
|                | managed        |                |                |
|                | U-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | eCPRI          |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5              | FALSE          |
|                | concatenation  | .1.3.1-5.1.3.2 |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 2              |
|                | DU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 6              |
|                | BandSector_ID  |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | 4              |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 4              |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | priority       |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | False (Default |
|                | prioritization |                | U-Plane        |
|                | within U-Plane |                | priority       |
|                |                |                | applies)       |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID        |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | FALSE          |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0dB            |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | RU beamforming | 4.2.1..(10.1)  | Digital        |
|                | type           |                | beamforming    |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.3, Annex J   | Beamforming ID |
|                | control method |                | based          |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | Block floating |
|                | compression    |                | point          |
|                | method         |                |                |
+----------------+----------------+----------------+----------------+
|                | U-Plane data   | 8, Annex D     | 14             |
|                | IQ bitwidth    |                |                |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | TRUE           |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | FALSE (always  |
|                | flag           |                | set to \'0\')  |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | Single C-Plane |
|                | PRACH formats  |                | message        |
|                | with preamble  |                |                |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | FALSE          |
|                | extension 1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | FALSE          |
|                | extension 2    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | FALSE          |
|                | extension 3    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | FALSE          |
|                | extension 4    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | FALSE          |
|                | extension 5    |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | TRUE           |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | FALSE          |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | FALSE          |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2         | Entry1: lls-C1 |
|                | configuration  |                | (can also      |
|                |                | 10, 11.2.3     | apply lls-C2)  |
|                |                | (for PLFS)     |                |
|                |                |                | Entry2: lls-C3 |
+----------------+----------------+----------------+----------------+

#### A.3.1.3 NR TDD IOT Profile 3 - NR-TDD-FR2-CAT-A-ABF 

Profile Test Configurations:

-   NR-TDD-FR2-CAT-A-ABF\_\[100MHz-SSB240kHz&PRACHC0-eAxCID2644-llsC1C2\]

-   NR-TDD-FR2-CAT-A-ABF\_\[200MHz-SSB240kHz&PRACHC0-eAxCID2644-llsC1C2\]

-   NR-TDD-FR2-CAT-A-ABF\_\[300MHz-SSB240kHz&PRACHC0-eAxCID2644-llsC1C2\]

-   NR-TDD-FR2-CAT-A-ABF\_\[400MHz-SSB240kHz&PRACHC0-eAxCID2644-llsC1C2\]

-   NR-TDD-FR2-CAT-A-ABF\_\[100MHz-SSB120kHz&PRACHA3-eAxCID2644-llsC1C2\]

-   NR-TDD-FR2-CAT-A-ABF\_\[200MHz-SSB120kHz&PRACHA3-eAxCID2644-llsC1C2\]

-   NR-TDD-FR2-CAT-A-ABF\_\[300MHz-SSB120kHz&PRACHA3-eAxCID2644-llsC1C2\]

-   NR-TDD-FR2-CAT-A-ABF\_\[400MHz-SSB120kHz&PRACHA3-eAxCID2644-llsC1C2\]

-   NR-TDD-FR2-CAT-A-ABF\_\[800MHz-SSB120kHz&PRACHA3-eAxCID2644-llsC1C2\]

-   NR-TDD-FR2-CAT-A-ABF\_\[100MHz-SSB240kHz&PRACHC2-eAxCID4246-llsC1C2\]

-   NR-TDD-FR2-CAT-A-ABF\_\[200MHz-SSB240kHz&PRACHC2-eAxCID4246-llsC1C2\]

-   NR-TDD-FR2-CAT-A-ABF\_\[400MHz-SSB240kHz&PRACHC2-eAxCID4246-llsC1C2\]

-   NR-TDD-FR2-CAT-A-ABF\_\[600MHz-SSB240kHz&PRACHC2-eAxCID4246-llsC1C2\]

-   NR-TDD-FR2-CAT-A-ABF\_\[800MHz-SSB240kHz&PRACHC2-eAxCID4246-llsC1C2\]

-   NR-TDD-FR2-CAT-A-ABF\_\[200MHz-SSB120kHz&PRACHA3-eAxCID2644-llsC3\]

-   NR-TDD-FR2-CAT-A-ABF\_\[400MHz-SSB120kHz&PRACHA3-eAxCID2644-llsC3\]

-   NR-TDD-FR2-CAT-A-ABF\_\[600MHz-SSB120kHz&PRACHA3-eAxCID2644-llsC3\]

-   NR-TDD-FR2-CAT-A-ABF\_\[800MHz-SSB120kHz&PRACHA3-eAxCID2644-llsC3\]

**Table A.3.1.3-1: NR TDD IOT Profile 3 - NR-TDD-FR2-CAT-A-ABF**

+----------------+----------------+----------------+----------------+
| **Category**   | **Item**       | **Related      |                |
|                |                | O-RAN          |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)**   |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR TDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | dl             |
|                | configuration  |                | -UL-Transmissi |
|                |                |                | onPeriodicity: |
|                |                |                | ms0p625\       |
|                |                |                | nrof           |
|                |                |                | DownlinkSlots: |
|                |                |                | 3\             |
|                |                |                | nrofDo         |
|                |                |                | wnlinkSymbols: |
|                |                |                | 10\            |
|                |                |                | nr             |
|                |                |                | ofUplinkSlots: |
|                |                |                | 1\             |
|                |                |                | nrof           |
|                |                |                | UplinkSymbols: |
|                |                |                | 2              |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 120 kHz        |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | Entry1:        |
|                | sub-carrier    |                | 240kHz\        |
|                | spacing        |                | Entry2: 120KHz |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    | \-             | 1024           |
|                | size           |                |                |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | Entry1: 100MHz |
|                | bandwidth      |                | x 1CC\         |
|                |                |                | Entry2: 100MHz |
|                |                |                | x 2CC\         |
|                |                |                | Entry3: 100MHz |
|                |                |                | x 3CC\         |
|                |                |                | Entry4: 100MHz |
|                |                |                | x 4CC\         |
|                |                |                | Entry5: 100MHz |
|                |                |                | x 6CC\         |
|                |                |                | Entry6: 100MHz |
|                |                |                | x 8CC          |
+----------------+----------------+----------------+----------------+
|                | Number of      | \-             | 2              |
|                | s              |                |                |
|                | patial/antenna |                |                |
|                | streams        |                |                |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 25Gbps x 1lane |
|                | Ethernet link  |                | for 100MHz x   |
|                |                |                | 1,2,3,4CC,\    |
|                |                |                | 25Gbps x 2lane |
|                |                |                | for 100MHz x   |
|                |                |                | 6,8CC          |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | Entry1: C0\    |
|                | format         |                | Entry2: A3\    |
|                |                |                | Entry3: C2     |
+----------------+----------------+----------------+----------------+
|                | RU category    | 4.2.1          | Category A     |
+----------------+----------------+----------------+----------------+
|                | LAA            | \-             | FALSE          |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4.2        | Defined        |
| management     | determination  |                | Transport      |
|                |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | RU adaptation  | 4.4.4.3        | FALSE          |
|                | of delay       |                |                |
|                | profile        |                |                |
|                | information\   |                |                |
|                | (based on O-DU |                |                |
|                | delay profile  |                |                |
|                | and transport  |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | Fixed Timing   |
|                | advance type   | Annex B        | Advance        |
+----------------+----------------+----------------+----------------+
|                | T1a_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 264us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 213us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 264us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 53us  |
+----------------+----------------+----------------+----------------+
|                | Tcp_adv_dl     | 4.3.2, Annex B | 63 us          |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 90us  |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 20us  |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 250us |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 20us  |
+----------------+----------------+----------------+----------------+
|                | T1a_max_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 274us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 223us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 274us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 63us  |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | Non-delay      | 4.4.7          | FALSE          |
|                | managed        |                |                |
|                | U-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | eCPRI          |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5              | FALSE          |
|                | concatenation  | .1.3.1-5.1.3.2 |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | Entry1: 2\     |
|                | DU_Port_ID     |                | Entry2: 4      |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | Entry1: 6\     |
|                | BandSector_ID  |                | Entry2: 2      |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | 4              |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | Entry1: 4\     |
|                | RU_Port_ID     |                | Entry2: 6      |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | priority       |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | False (Default |
|                | prioritization |                | U-Plane        |
|                | within U-Plane |                | priority       |
|                |                |                | applies)       |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID        |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | FALSE          |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0dB            |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | RU beamforming | 4.2.1..(10.1)  | Analog         |
|                | type           |                | beamforming    |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.3, Annex J   | Beamforming ID |
|                | control method |                | based          |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | Block floating |
|                | compression    |                | point          |
|                | method         |                |                |
+----------------+----------------+----------------+----------------+
|                | U-Plane data   | 8, Annex D     | 14             |
|                | IQ bitwidth    |                |                |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | TRUE           |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | FALSE (always  |
|                | flag           |                | set to \'0\')  |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | Single C-Plane |
|                | PRACH formats  |                | message        |
|                | with preamble  |                |                |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | FALSE          |
|                | extension 1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | FALSE          |
|                | extension 2    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | FALSE          |
|                | extension 3    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | FALSE          |
|                | extension 4    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | FALSE          |
|                | extension 5    |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 7.2.3, 10.1,   | TRUE           |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | FALSE          |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 11      | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2         | Entry1: lls-C1 |
|                | configuration  |                | (can also      |
|                |                | 10, 11.2.3     | apply lls-C2)  |
|                |                | (for PLFS)     |                |
|                |                |                | Entry2: lls-C3 |
+----------------+----------------+----------------+----------------+

#### A.3.1.4 NR TDD IOT M-MIMO Profile 1 - NR-TDD-FR1-CAT-B-mMIMO-RTWeights-BFP

Profile Test Configurations:

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-BFP\_\[ConfigDDDFUUDDDD-100MHz1CC-8SS-25Gbpsx2lane-PRACHF0-noJumbo-BFW.12bitFP-llsC1-SE1_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-BFP\_\[ConfigDDDFUUDDDD-100MHz1CC-8SS-25Gbpsx2lane-PRACHC2-Jumbo-BFW.12bitFP-llsC1noPLFS-SE11_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-BFP\_\[ConfigDDDFUUDDDD-100MHz1CC-16SS-25Gbpsx2lane-PRACHF0-noJumbo-BFW.9bitBFP-llsC1noPLFS-SE11_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-BFP\_\[ConfigDDDFUUDDDD-100MHz1CC-16SS-25Gbpsx2lane-PRACHB4-noJumbo-BFW.12bitFP-llsC3-SE1_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-BFP\_\[ConfigDDDFU-100MHz1CC-8SS-25Gbpsx2lane-PRACHF0-noJumbo-BFW.12bitFP-llsC1noPLFS-SE1\]
    \_DM1

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-BFP\_\[ConfigDDDFU-100MHz1CC-8SS-25Gbpsx2lane-PRACHB4-noJumbo-BFW.9bitBFP-llsC1-SE11\]
    \_DM1

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-BFP\_\[ConfigDDDFU-100MHz1CC-16SS-25Gbpsx2lane-PRACHF0-noJumbo-BFW.12bitFP-llsC1-SE1_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-BFP\_\[ConfigDDDFU-100MHz1CC-16SS-25Gbpsx2lane-PRACHC2-Jumbo-BFW.12bitFP-llsC3-SE11_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-BFP\_\[ConfigDDDFUUDDDD-100MHz1CC-16SS-25Gbpsx2lane-PRACHF0-noJumbo-BFW.9bitBFP-llsC1noPLFS-SE11_DM2\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-BFP\_\[ConfigDDDFU-100MHz1CC-8SS-25Gbpsx2lane-PRACHB4-noJumbo-BFW.9bitBFP-llsC1-SE11_DM2\]

**Table A.3.1.4-1: NR TDD IOT M-MIMO Profile 1 -
NR-TDD-FR1-CAT-B-mMIMO-RTWeights-BFP**

+----------------+----------------+----------------+----------------+
| **Category**   | **Item**       | **Related      |                |
|                |                | O-RAN          |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)**   |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR TDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | Entry1:        |
|                | configuration  |                | DDDFUUDDDD\    |
|                |                |                | Entry2: DDDFU  |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    | \-             | 4              |
|                | size           |                | 096(100MHz_BW) |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | 100MHz x 1 CC  |
|                | bandwidth      |                |                |
+----------------+----------------+----------------+----------------+
|                | Number of      | \-             | Entry1: 8L     |
|                | s              |                | (DL), 8        |
|                | patial/antenna |                | streams (UL)\  |
|                | streams        |                | Entry2: 16L    |
|                |                |                | (DL), 16       |
|                |                |                | streams (UL)   |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 25Gbps x 2     |
|                | Ethernet link  |                | lane (16L,     |
|                |                |                | 1CC)           |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | Entry1: Long   |
|                | format         |                | preamble F0\   |
|                |                |                | Entry2: B4\    |
|                |                |                | Entry3: C2     |
+----------------+----------------+----------------+----------------+
|                | RU category    | 4.2.1          | Category B     |
+----------------+----------------+----------------+----------------+
|                | LAA            | \-             | FALSE          |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4.2        | Defined        |
| management     | determination  |                | Transport      |
|                |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | RU adaptation  | 4.4.4.3        | FALSE          |
|                | of delay       |                |                |
|                | profile        |                |                |
|                | information    |                |                |
+----------------+----------------+----------------+----------------+
|                | (based on O-DU |                |                |
|                | delay profile  |                |                |
|                | and transport  |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | Fixed timing   |
|                | advance type   | Annex B        | Advance        |
+----------------+----------------+----------------+----------------+
|                | T1a_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1:345us\  |
|                |                |                | Entry2: 475us  |
|                |                |                |                |
|                |                |                | (Note 2)       |
+----------------+----------------+----------------+----------------+
|                | T1a_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 294us\ |
|                |                |                | Entry2: 400us  |
+----------------+----------------+----------------+----------------+
|                | T1a_max_cp_dl  | 4.4, Annex B   | Less than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 669us  |
|                |                |                |                |
|                |                |                | Entry2: 971us  |
+----------------+----------------+----------------+----------------+
|                | T1a_min_cp_dl  | 4.4, Annex B   | More than or   |
|                |                |                | equal t\       |
|                |                |                | Entry1: 419us\ |
|                |                |                | Entry2: 550us  |
+----------------+----------------+----------------+----------------+
|                | T2a_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 345us\ |
|                |                |                | Entry2: 475us  |
+----------------+----------------+----------------+----------------+
|                | T2a_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 134us\ |
|                |                |                | Entry2: 240us  |
+----------------+----------------+----------------+----------------+
|                | T2a_max_cp_dl  | 4.3.2, Annex B | More than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 669us\ |
|                |                |                | Entry2: 971us  |
+----------------+----------------+----------------+----------------+
|                | T2a_min_cp_dl  | 4.4, Annex B   | Less than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 259us  |
|                |                |                |                |
|                |                |                | Entry2: 390us  |
+----------------+----------------+----------------+----------------+
|                | Tcp_adv_dl     | 4.4, Annex B   | Entry1: 125us\ |
|                |                |                | Entry2: 150us  |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 171us\ |
|                |                |                | Entry2: 280us  |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 50us  |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 331us\ |
|                |                |                | Entry2: 440us  |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 50us  |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                | (scs=1.25kHz)  |                | equal to       |
|                |                |                | 1650us         |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                | (scs=1.25kHz)  |                | equal to 827us |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4.3-4.4.4,   | More than or   |
|                | (scs=1.25kHz)  | Annex B        | equal to       |
|                |                |                | 1810us         |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4.3-4.4.4,   | Less than or   |
|                | (scs=1.25kHz)  | Annex B        | equal to 827us |
+----------------+----------------+----------------+----------------+
|                | T1a_max_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to\      |
|                |                |                | Entry1: 535us\ |
|                |                |                | Entry2: 840us  |
+----------------+----------------+----------------+----------------+
|                | T1a_min_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to\      |
|                |                |                | Entry1: 285us\ |
|                |                |                | Entry2: 419us  |
+----------------+----------------+----------------+----------------+
|                | T2a_max_cp_ul  | 4.4, Annex B   | More than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 535us\ |
|                |                |                | Entry2: 840us  |
+----------------+----------------+----------------+----------------+
|                | T2a_min_cp_ul  | 4.4, Annex B   | Less than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 125us\ |
|                |                |                | Entry2: 259us  |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
|                | Non-delay      | 4.4.7          | Support        |
|                | managed        |                |                |
|                | U-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | Entry1: TRUE\  |
|                |                |                | Entry2: FALSE  |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | eCPRI          |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5              | FALSE          |
|                | concatenation  | .1.3.1-5.1.3.2 |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 5              |
|                | DU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 1              |
|                | BandSector_ID  |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | 2              |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 8              |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | Priority       |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | TRUE           |
|                | prioritization |                |                |
|                | within U-Plane |                |                |
+----------------+----------------+----------------+----------------+
|                | Seperation of  | 5.4            | VLAN ID        |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | FALSE          |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0 dB           |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | O-RU           | 4.2.1..(10.1)  | Digital        |
|                | beamforming    |                | beamforming    |
|                | type           |                |                |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.3, Annex J   | RT Weights     |
|                | control method |                | (Frequency     |
|                |                |                | Domain)        |
+----------------+----------------+----------------+----------------+
|                | BFW IQ         | 7.4, Annex J   | Entry 1: Fixed |
|                |                |                | Point, 12-bit\ |
|                |                |                | Entry 2: BFP,  |
|                |                |                | 9-bit          |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | BFP            |
|                | compression    |                |                |
|                | method         |                |                |
+----------------+----------------+----------------+----------------+
|                | U-Plane        | 8, Annex D     | 9              |
|                | (DL/UL) data   |                |                |
|                | IQ bitwidth    |                |                |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | TRUE           |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | FALSE (always  |
|                | flag           |                | set to \"0\")  |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | Single C-Plane |
|                | PRACH formats  |                | message        |
|                | with preamble  |                |                |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | Entry 1: FALSE |
|                | extension 1    |                |                |
|                | (beamforming   |                | Entry 2: TRUE  |
|                | weights)       |                |                |
|                |                |                | (Note 1)       |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | FALSE          |
|                | extension 2    |                |                |
|                | (beamforming   |                |                |
|                | attributes)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | FALSE          |
|                | extension 3    |                |                |
|                | (DL Precoding  |                |                |
|                | configuration  |                |                |
|                | parameters and |                |                |
|                | indications)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | FALSE          |
|                | extension 4    |                |                |
|                | (modulation    |                |                |
|                | compr. params) |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | FALSE          |
|                | extension 5    |                |                |
|                | (modulation    |                |                |
|                | compression    |                |                |
|                | additional     |                |                |
|                | scaling        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.6          | FALSE          |
|                | extension 6    |                |                |
|                | (              |                |                |
|                | Non-contiguous |                |                |
|                | PRB            |                |                |
|                | allocation)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.7          | FALSE          |
|                | extension 7    |                |                |
|                | (Multiple-eAxC |                |                |
|                | designation)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.8          | FALSE          |
|                | extension 8    |                |                |
|                | (              |                |                |
|                | regularization |                |                |
|                | factor)        |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.9          | FALSE          |
|                | extension 9    |                |                |
|                | (Dynamic       |                |                |
|                | Spectrum       |                |                |
|                | Sharing        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.10         | FALSE          |
|                | extension 10   |                |                |
|                | (Multiple      |                |                |
|                | ports          |                |                |
|                | grouping)      |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.11         | Entry 1: TRUE  |
|                | extension 11   |                |                |
|                | (Flexible BF   |                | Entry 2: FALSE |
|                | weights)       |                |                |
|                |                |                | (Note 1)       |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.12         | FALSE          |
|                | extension 12   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.13         | FALSE          |
|                | extension 13   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.14         | FALSE          |
|                | extension 14   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.15         | FALSE          |
|                | extension 15   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.16         | FALSE          |
|                | extension 16   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.17         | FALSE          |
|                | extension 17   |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | TRUE           |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | FALSE          |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | FALSE          |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2\        | Entry 1)       |
|                | configuration  | 10, 11.2.3     | lls-C1 (can    |
|                |                | (for PLFS)     | also apply     |
|                |                |                | lls-C2)\       |
|                |                |                | Entry 2)       |
|                |                |                | lls-C1 (PLFS   |
|                |                |                | not required   |
|                |                |                | by O-RU)\      |
|                |                |                | Entry 3)       |
|                |                |                | lls-C3         |
+----------------+----------------+----------------+----------------+

Note 1: Either Section extension 1 or Section extension 11 should be
used for IOT (ie, (FALSE, TRUE) or (TRUE, FALSE)).

Note 2: When two entries are present for parameters in section 'Delay
Management', DM1 refers to Entry1 and DM2 to Entry2. DM1/2 are used as
identifiers in list "Profile Test Configurations".

#### A.3.1.5 NR TDD IOT M-MIMO Profile 2 - NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp

Profile Test Configurations:

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFUUDDDD-100MHz1CC-8SS-25Gbpsx2lane-PRACHF0-noJumbo-12bitFP.BFW-llsC1-SE1-SE4_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFUUDDDD-100MHz1CC-8SS-25Gbpsx2lane-PRACHC2-Jumbo-12bitFP.BFW-llsC1noPLFS-SE11-SE5_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFUUDDDD-100MHz1CC-16SS-25Gbpsx2lane-PRACHF0-noJumbo-9bitBFP.BFW-llsC1noPLFS-SE11-SE5_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFUUDDDD-100MHz1CC-16SS-25Gbpsx2lane-PRACHB4-noJumbo-12bitFP.BFW-llsC3-SE1-SE5_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFUUDDDD-100MHz1CC-16SS-25Gbpsx2lane-PRACHF0-Jumbo-9bitBFP.BFW-llsC1-SE11-SE4_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFUUDDDD-100MHz2CC-8SS-25Gbpsx3lane-PRACHF0-noJumbo-12bitFP.BFW-llsC1-SE1-SE4_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFUUDDDD-100MHz2CC-8SS-25Gbpsx3lane-PRACHC2-Jumbo-12bitFP.BFW-llsC1noPLFS-SE11-SE5_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFUUDDDD-100MHz2CC-16SS-25Gbpsx3lane-PRACHF0-noJumbo-9bitBFP.BFW-llsC1noPLFS-SE11-SE5_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFUUDDDD-100MHz2CC-16SS-25Gbpsx3lane-PRACHB4-noJumbo-12bitFP.BFW-llsC3-SE1-SE4_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFU-100MHz1CC-8SS-25Gbpsx2lane-PRACHF0-noJumbo-12bitFP.BFW-llsC1noPLFS-SE1-SE5_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFU-100MHz1CC-8SS-25Gbpsx2lane-PRACHB4-noJumbo-9bitBFP.BFW-llsC1-SE11-SE5_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFU-100MHz1CC-16SS-25Gbpsx2lane-PRACHF0-noJumbo-12bitFP.BFW-llsC1-SE1-SE4_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFU-100MHz1CC-16SS-25Gbpsx2lane-PRACHC2-Jumbo-12bitFP.BFW-llsC3-SE11-SE5_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFU-100MHz1CC-16SS-25Gbpsx2lane-PRACHF0-Jumbo-9bitBFP.BFW-llsC1noPLFS-SE11-SE4_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFU-100MHz2CC-8SS-25Gbpsx3lane-PRACHF0-noJumbo-12bitFP.BFW-llsC1noPLFS-SE1-SE4_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFU-100MHz2CC-8SS-25Gbpsx3lane-PRACHB4-noJumbo-9bitBFP.BFW-llsC1-SE11-SE5_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFU-100MHz2CC-16SS-25Gbpsx3lane-PRACHF0-noJumbo-12bitFP.BFW-llsC1-SE1-SE4_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFU-100MHz2CC-16SS-25Gbpsx3lane-PRACHC2-Jumbo-12bitFP.BFW-llsC3-SE11-SE5_DM1\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFUUDDDD-100MHz1CC-16SS-25Gbpsx2lane-PRACHF0-noJumbo-9bitBFP.BFW-llsC1noPLFS-SE11-SE5_DM2\]

-   NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp\_\[ConfigDDDFU-100MHz1CC-8SS-25Gbpsx2lane-PRACHB4-noJumbo-9bitBFP.BFW-llsC1-SE11-SE5_DM2\]

**Table A.3.1.5-1: NR TDD IOT M-MIMO Profile 2 -
NR-TDD-FR1-CAT-B-mMIMO-RTWeights-ModComp**

+----------------+----------------+----------------+----------------+
| **Category**   | **Item**       | **Related      |                |
|                |                | O-RAN          |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)**   |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR TDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | Entry1:        |
|                | configuration  |                | DDDFUUDDDD\    |
|                |                |                | Entry2: DDDFU  |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    | \-             | 4              |
|                | size           |                | 096(100MHz_BW) |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | Entry1: 100MHz |
|                | bandwidth      |                | x 1 CC\        |
|                |                |                | Entry2: 100    |
|                |                |                | MHz x 2 CC     |
+----------------+----------------+----------------+----------------+
|                | Number of      | \-             | Entry1: 8L     |
|                | s              |                | (DL), 8        |
|                | patial/antenna |                | streams (UL)\  |
|                | streams        |                | Entry2: 16L    |
|                |                |                | (DL), 16       |
|                |                |                | streams (UL)   |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | Entry1: 25Gbps |
|                | Ethernet link  |                | x 2 lane (16L, |
|                |                |                | 1CC)\          |
|                |                |                | Entry2: 25Gbps |
|                |                |                | x 3 lane (16L, |
|                |                |                | 2CC)           |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | Entry1: Long   |
|                | format         |                | preamble F0\   |
|                |                |                | Entry2: B4\    |
|                |                |                | Entry3: C2     |
+----------------+----------------+----------------+----------------+
|                | O-RU category  | 4.2.1          | Category B     |
+----------------+----------------+----------------+----------------+
|                | LAA            | \-             | FALSE          |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4.2        | Defined        |
| management     | determination  |                | Transport      |
|                |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 4.4.4.3        | FALSE          |
|                | adaptation of  |                |                |
|                | delay profile  |                |                |
|                | information    |                |                |
|                | (based on      |                |                |
|                | lls-CU delay   |                |                |
|                | profile and    |                |                |
|                | transport      |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | Fixed timing   |
|                | advance type   | Annex B        | Advance        |
+----------------+----------------+----------------+----------------+
|                | T1a_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 345us\ |
|                |                |                | Entry2: 475us  |
|                |                |                |                |
|                |                |                | (Note 3)       |
+----------------+----------------+----------------+----------------+
|                | T1a_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 294us\ |
|                |                |                | Entry2: 400us  |
+----------------+----------------+----------------+----------------+
|                | T1a_max_cp_dl  | 4.4, Annex B   | Less than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 669us\ |
|                |                |                | Entry2: 971us  |
+----------------+----------------+----------------+----------------+
|                | T1a_min_cp_dl  | 4.4, Annex B   | More than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 419us\ |
|                |                |                | Entry2: 550us  |
+----------------+----------------+----------------+----------------+
|                | T2a_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 345us\ |
|                |                |                | Entry2: 475us  |
+----------------+----------------+----------------+----------------+
|                | T2a_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 134us\ |
|                |                |                | Entry2: 240us  |
+----------------+----------------+----------------+----------------+
|                | T2a_max_cp_dl  | 4.3.2, Annex B | More than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 669us\ |
|                |                |                | Entry2: 971us  |
+----------------+----------------+----------------+----------------+
|                | T2a_min_cp_dl  | 4.4, Annex B   | Less than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 259us\ |
|                |                |                | Entry2: 390us  |
+----------------+----------------+----------------+----------------+
|                | Tcp_adv_dl     | 4.4, Annex B   | Entry1: 125us\ |
|                |                |                | Entry2: 150us  |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 171us\ |
|                |                |                | Entry2: 280us  |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 50us  |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 331us\ |
|                |                |                | Entry2: 440us  |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 50us  |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                | (scs=1.25kHz)  |                | equal to       |
|                |                |                | 1650us         |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                | (scs=1.25kHz)  |                | equal to 827us |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4.3-4.4.4,   | More than or   |
|                | (scs=1.25kHz)  | Annex B        | equal to       |
|                |                |                | 1810us         |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4.3-4.4.4,   | Less than or   |
|                | (scs=1.25kHz)  | Annex B        | equal to 827us |
+----------------+----------------+----------------+----------------+
|                | T1a_max_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to\      |
|                |                |                | Entry1: 535us\ |
|                |                |                | Entry2: 840us  |
+----------------+----------------+----------------+----------------+
|                | T1a_min_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to\      |
|                |                |                | Entry1: 285us\ |
|                |                |                | Entry2: 419us  |
+----------------+----------------+----------------+----------------+
|                | T2a_max_cp_ul  | 4.4, Annex B   | More than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 535us\ |
|                |                |                | Entry2: 840us  |
+----------------+----------------+----------------+----------------+
|                | T2a_min_cp_ul  | 4.4, Annex B   | Less than or   |
|                |                |                | equal to\      |
|                |                |                | Entry1: 125us\ |
|                |                |                | Entry2: 259us  |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
|                | Non-delay      | 4.4.7          | Support        |
|                | managed        |                |                |
|                | U-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | Entry1: TRUE\  |
|                |                |                | Entry2: FALSE  |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | eCPRI          |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5              | FALSE          |
|                | concatenation  | .1.3.1-5.1.3.2 |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 5              |
|                | DU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 1              |
|                | BandSector_ID  |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | 2              |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 8              |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | Priority       |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | TRUE           |
|                | prioritization |                |                |
|                | within U-Plane |                |                |
+----------------+----------------+----------------+----------------+
|                | Seperation of  | 5.4            | VLAN ID        |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | FALSE          |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0 dB           |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | O-RU           | 4.2.1..(10.1)  | Digital        |
|                | beamforming    |                | beamforming    |
|                | type           |                |                |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.4, Annex J   | RT Weights     |
|                | control method |                | (Frequency     |
|                |                |                | Domain)        |
+----------------+----------------+----------------+----------------+
|                | BFW IQ         | 7.4, Annex J   | Entry 1: Fixed |
|                |                |                | Point, 12-bit\ |
|                |                |                | Entry 2: BFP,  |
|                |                |                | 9-bit          |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | DL: Mod COMP,  |
|                | compression    |                | UL: BFP        |
|                | method         |                |                |
+----------------+----------------+----------------+----------------+
|                | U-Plane        | 8, Annex D     | DL: Mod COMP,  |
|                | (DL/UL) data   |                | 4 bits (max)\  |
|                | IQ bitwidth    |                | UL: BFP, 9     |
|                |                |                | bits           |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | TRUE           |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | FALSE (always  |
|                | flag           |                | set to \"0\")  |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | Single C-Plane |
|                | PRACH formats  |                | message        |
|                | with preamble  |                |                |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | Entry 1: FALSE |
|                | extension 1    |                |                |
|                | (beamforming   |                | Entry 2: TRUE  |
|                | weights)       |                |                |
|                |                |                | (Note 1)       |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | FALSE          |
|                | extension 2    |                |                |
|                | (beamforming   |                |                |
|                | attributes)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | FALSE          |
|                | extension 3    |                |                |
|                | (DL Precoding  |                |                |
|                | configuration  |                |                |
|                | parameters and |                |                |
|                | indications)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | Entry 1: TRUE  |
|                | extension 4    |                |                |
|                | (modulation    |                | Entry 2: FALSE |
|                | compr. params) |                |                |
|                |                |                | (Note 2)       |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | Entry 1: FALSE |
|                | extension 5    |                |                |
|                | (modulation    |                | Entry 2: TRUE  |
|                | compression    |                |                |
|                | additional     |                | (Note 2)       |
|                | scaling        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.6          | FALSE          |
|                | extension 6    |                |                |
|                | (              |                |                |
|                | Non-contiguous |                |                |
|                | PRB            |                |                |
|                | allocation)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.7          | FALSE          |
|                | extension 7    |                |                |
|                | (Multiple-eAxC |                |                |
|                | designation)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.8          | FALSE          |
|                | extension 8    |                |                |
|                | (              |                |                |
|                | regularization |                |                |
|                | factor)        |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.9          | FALSE          |
|                | extension 9    |                |                |
|                | (Dynamic       |                |                |
|                | Spectrum       |                |                |
|                | Sharing        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.10         | FALSE          |
|                | extension 10   |                |                |
|                | (Multiple      |                |                |
|                | ports          |                |                |
|                | grouping)      |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.11         | Entry 1: TRUE  |
|                | extension 11   |                |                |
|                | (Flexible BF   |                | Entry 2: FALSE |
|                | weights)       |                |                |
|                |                |                | (Note 1)       |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.12         | FALSE          |
|                | extension 12   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.13         | FALSE          |
|                | extension 13   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.14         | FALSE          |
|                | extension 14   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.15         | FALSE          |
|                | extension 15   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.16         | FALSE          |
|                | extension 16   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.17         | FALSE          |
|                | extension 17   |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | TRUE           |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | FALSE          |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | FALSE          |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2\        | Entry 1)       |
|                | configuration  | 10, 11.2.3     | lls-C1 (can    |
|                |                | (for PLFS)     | also apply     |
|                |                |                | lls-C2)\       |
|                |                |                | Entry 2)       |
|                |                |                | lls-C1 (PLFS   |
|                |                |                | not required   |
|                |                |                | by O-RU)\      |
|                |                |                | Entry 3)       |
|                |                |                | lls-C3         |
+----------------+----------------+----------------+----------------+

Note 1: Either Section extension 1 or Section extension 11 should be
used for IOT (ie, (FALSE, TRUE) or (TRUE, FALSE)).

Note 2: Either Section extension 4 or Section extension 5 should be used
for IOT (ie, (FALSE, TRUE) or (TRUE, FALSE)).

Note 3: When two entries are present for parameters in section 'Delay
Management', DM1 refers to Entry1 and DM2 to Entry2. DM1/2 are used as
identifiers in list "Profile Test Configurations"

#### A.3.1.6 NR TDD IOT M-MIMO Profile 3 - NR-TDD-FR1-CAT-B-mMIMO-ChInfo-BFP

Profile Test Configurations:

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-BFP\_\[ConfigDDDFUUDDDD-100MHz1CC-16SS-25Gbpsx2lane-PRACHF0-Jumbo-llsC1noPLFS\]

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-BFP\_\[ConfigDDDFUUDDDD-100MHz1CC-8SS-25Gbpsx2lane-PRACHC2-noJumbo-llsC1\]

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-BFP\_\[ConfigDDDFUUDDDD-100MHz1CC-16SS-25Gbpsx2lane-PRACHB4-Jumbo-llsC3\]

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-BFP\_\[ConfigDDDFU-100MHz1CC-16SS-25Gbpsx2lane-PRACHF0-noJumbo-llsC1\]

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-BFP\_\[ConfigDDDFU-100MHz1CC-8SS-25Gbpsx2lane-PRACHB4-noJumbo-llsC1noPLFS\]

```{=html}
<!-- -->
```
-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-BFP\_\[ConfigDDDFU-100MHz1CC-16SS-25Gbpsx2lane-PRACHC2-Jumbo-llsC3\]

**Table A.3.1.6-1: NR TDD IOT M-MIMO Profile 3 -
NR-TDD-FR1(30kHzSRS)-CAT-B-mMIMO-ChInfo-BFP**

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Category**            **Item**                                                                                           **Related O-RAN CUS-Plane specification section(s)**   
  ----------------------- -------------------------------------------------------------------------------------------------- ------------------------------------------------------ ----------------------------------------------
  General                 Radio access technology                                                                            \-                                                     NR TDD

                          TDD configuration                                                                                  \-                                                     Entry1: DDDFUUDDDD\
                                                                                                                                                                                    Entry2: DDDFU

                          Nominal sub-carrier spacing                                                                        \-                                                     30kHz

                          SSB sub-carrier spacing                                                                            \-                                                     30kHz

                          Nominal FFT size                                                                                   \-                                                     4096(100MHz_BW)

                          Total channel bandwidth                                                                            \-                                                     100MHz x 1 CC

                          Number of spatial/antenna streams                                                                  \-                                                     Entry1: 8L (DL), 8 streams (UL)\
                                                                                                                                                                                    Entry2: 16L (DL), 16 streams (UL)

                          Fronthaul Ethernet link                                                                            \-                                                     25Gbps x 2 lane (16L, 1CC)

                          PRACH preamble format                                                                              \-                                                     Entry1: Long preamble F0\
                                                                                                                                                                                    Entry2: B4\
                                                                                                                                                                                    Entry3: C2

                          O-RU category                                                                                      4.2.1                                                  Category B

                          LAA                                                                                                \-                                                     FALSE

  Delay management        Network delay determination                                                                        4.4.4.2                                                Defined Transport Method

                          O-RU adaptation of delay profile information (based on lls-CU delay profile and transport delay)   4.4.4.3                                                FALSE

                          O-DU timing advance type                                                                           4.4.5-4.4.6, Annex B                                   Fixed timing Advance

                          T1a_max_up                                                                                         4.4, Annex B                                           Less than or equal to 345us

                          T1a_min_up                                                                                         4.4, Annex B                                           More than or equal to 294us

                          T1a_max_cp_dl                                                                                      4.4, Annex B                                           Less than or equal to 820us

                          T1a_min_cp_dl                                                                                      4.4, Annex B                                           More than or equal to 769us

                          T2a_max_up                                                                                         4.4, Annex B                                           More than or equal to 345us

                          T2a_min_up                                                                                         4.4, Annex B                                           Less than or equal to 134us

                          T2a_max_cp_dl                                                                                      4.3.2, Annex B                                         More than or equal to 820us

                          T2a_min_cp_dl                                                                                      4.4, Annex B                                           Less than or equal to 609us

                          Tcp_adv_dl                                                                                         4.4, Annex B                                           475us

                          Ta3_max_up                                                                                         4.4, Annex B                                           Less than or equal to 171us

                          Ta3_min_up                                                                                         4.4, Annex B                                           More than or equal to 50us

                          Ta4_max_up                                                                                         4.4, Annex B                                           More than or equal to 331us

                          Ta4_min_up                                                                                         4.4, Annex B                                           Less than or equal to 50us

                          Ta3_max_up (scs=1.25kHz)                                                                           4.4, Annex B                                           Less than or equal to 1650us

                          Ta3_min_up (scs=1.25kHz)                                                                           4.4, Annex B                                           More than or equal to 827us

                          Ta4_max_up (scs=1.25kHz)                                                                           4.4.3-4.4.4, Annex B                                   More than or equal to 1810us

                          Ta4_min_up (scs=1.25kHz)                                                                           4.4.3-4.4.4, Annex B                                   Less than or equal to 827us

                          T1a_max_cp_ul                                                                                      4.4.3-4.4.4, Annex B                                   Less than or equal to 336us

                          T1a_min_cp_ul                                                                                      4.4.3-4.4.4, Annex B                                   More than or equal to 285us

                          T2a_max_cp_ul                                                                                      4.4, Annex B                                           More than or equal to 336us

                          T2a_min_cp_ul                                                                                      4.4, Annex B                                           Less than or equal to 125us

                          T12_max                                                                                            4.4, Annex B                                           160us

                          T12_min                                                                                            4.4, Annex B                                           0us

                          T34_max                                                                                            4.4, Annex B                                           160us

                          T34_min                                                                                            4.4, Annex B                                           0us

                          Non-delay managed U-Plane traffic                                                                  4.4.7                                                  Support

  C/U-Plane transport     Transport encapsulation                                                                            5.1.1-5.1.2                                            Ethernet

                          Jumbo frames                                                                                       5.1.2                                                  Entry1: TRUE\
                                                                                                                                                                                    Entry2: FALSE

                          Transport header                                                                                   5.1.3                                                  eCPRI

                          eCPRI concatenation                                                                                5.1.3.1-5.1.3.2                                        FALSE

                          eAxC ID DU_Port_ID bitwidth                                                                        5.1.3.2.7                                              5

                          eAxC ID BandSector_ID bitwidth                                                                     5.1.3.2.7                                              1

                          eAxC ID CC_ID bitwidth                                                                             5.1.3.2.7                                              2

                          eAxC ID RU_Port_ID bitwidth                                                                        5.1.3.2.7                                              8

                          Fragmentation                                                                                      5.5                                                    Application layer fragmentation

                          Transport prioritization across C/U/S/M-Plane                                                      5.3                                                    Default L2 CoS Priority

                          Transport prioritization within U-Plane                                                            5.3                                                    TRUE

                          Seperation of C/U-Plane and M-Plane traffic                                                        5.4                                                    VLAN ID

                          Transport-based separation within C/U-Plane traffic                                                5.4                                                    FALSE

  Digital Power Scaling   UL gain_correction                                                                                 8.1.3.2                                                0 dB

  Beamforming             O-RU beamforming type                                                                              4.2.1..(10.1)                                          Digital beamforming

                          Beamforming control method                                                                         7.4, Annex J                                           Chan Info (Frequency Domain)

                          BFW IQ                                                                                             7.4, Annex J                                           NA

  IQ compression          U-Plane data compression method                                                                    8, Annex A                                             BFP

                          U-Plane (DL/UL) data IQ bitwidth                                                                   8, Annex D                                             9

                          IQ data frame format not including udCompHdr field                                                 8.3.3.13                                               TRUE

  C-Plane                 Section Type 0                                                                                     7.4.2                                                  TRUE

                          Section Type 1                                                                                     7.4.3                                                  TRUE

                          Section Type 3                                                                                     7.4.5                                                  TRUE

                          Section Type 5                                                                                     7.4.7                                                  TRUE

                          Section Type 6                                                                                     7.4.8                                                  TRUE

                          Section Type 7                                                                                     7.4.9                                                  FALSE

                          \"symInc\" flag                                                                                    7.5.3.3                                                FALSE (always set to \"0\")

                          C-Plane for PRACH formats with preamble repetition                                                 7.2.3.4                                                Single C-Plane message

                          Section extension 1 (beamforming weights)                                                          7.7.1                                                  FALSE

                          Section extension 2 (beamforming attributes)                                                       7.7.2                                                  FALSE

                          Section extension 3 (DL Precoding configuration parameters and indications)                        7.7.3                                                  FALSE

                          Section extension 4 (modulation compr. params)                                                     7.7.4                                                  FALSE

                          Section extension 5 (modulation compression additional scaling parameters)                         7.7.5                                                  FALSE

                          Section extension 6 (Non-contiguous PRB allocation)                                                7.7.6                                                  FALSE

                          Section extension 7 (Multiple-eAxC designation)                                                    7.7.7                                                  FALSE

                          Section extension 8 (regularization factor)                                                        7.7.8                                                  FALSE

                          Section extension 9 (Dynamic Spectrum Sharing parameters)                                          7.7.9                                                  FALSE

                          Section extension 10 (Multiple ports grouping)                                                     7.7.10                                                 TRUE

                          Section extension 11 (Flexible BF weights)                                                         7.7.11                                                 FALSE

                          Section extension 12                                                                               7.7.12                                                 FALSE

                          Section extension 13                                                                               7.7.13                                                 FALSE

                          Section extension 14                                                                               7.7.14                                                 FALSE

                          Section extension 15                                                                               7.7.15                                                 FALSE

                          Section extension 16                                                                               7.7.16                                                 TRUE

                          Section extension 17                                                                               7.7.17                                                 FALSE

  S-Plane                 PTP Full Timing Support (G.8275.1)                                                                 5.2.3, 10.1, 11                                        TRUE

                          PTP Partial Timing Support (G.8275.2)                                                              5.2.3, 10.1, 11                                        FALSE

                          Local PRTC                                                                                         5.2.3, 10.1, 11                                        FALSE

                          Topology configuration                                                                             11.2.2\                                                Entry 1) lls-C1 (can also apply lls-C2)\
                                                                                                                             10, 11.2.3 (for PLFS)                                  Entry 2) lls-C1 (PLFS not required by O-RU)\
                                                                                                                                                                                    Entry 3) lls-C3
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### A.3.1.7 NR TDD IOT M-MIMO Profile 4 - NR-TDD-FR1-CAT-B-mMIMO-ChInfo-ModComp

Profile Test Configurations:

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-ModComp\_\[ConfigDDDFUUDDDD-100MHz1CC-16SS-25Gbpsx2lane-PRACHF0-Jumbo-llsC1noPLFS\]

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-ModComp\_\[ConfigDDDFUUDDDD-100MHz1CC-8SS-25Gbpsx2lane-PRACHC2-noJumbo-llsC1\]

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-ModComp\_\[ConfigDDDFUUDDDD-100MHz1CC-16SS-25Gbpsx2lane-PRACHB4-Jumbo-llsC3\]

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-ModComp\_\[ConfigDDDFUUDDDD-100MHz2CC-16SS-25Gbpsx3lane-PRACHF0-Jumbo-llsC1noPLFS\]

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-ModComp\_\[ConfigDDDFUUDDDD-100MHz2CC-8SS-25Gbpsx3lane-PRACHC2-noJumbo-llsC1\]

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-ModComp\_\[ConfigDDDFUUDDDD-100MHz2CC-16SS-25Gbpsx3lane-PRACHB4-Jumbo-llsC3\]

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-ModComp\_\[ConfigDDDFU-100MHz1CC-16SS-25Gbpsx2lane-PRACHF0-noJumbo-llsC1\]

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-ModComp\_\[ConfigDDDFU-100MHz1CC-8SS-25Gbpsx2lane-PRACHB4-noJumbo-llsC1noPLFS\]

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-ModComp\_\[ConfigDDDFU-100MHz1CC-16SS-25Gbpsx2lane-PRACHC2-Jumbo-llsC3\]

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-ModComp\_\[ConfigDDDFU-100MHz2CC-16SS-25Gbpsx3lane-PRACHF0-noJumbo-llsC1\]

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-ModComp\_\[ConfigDDDFU-100MHz2CC-8SS-25Gbpsx3lane-PRACHB4-noJumbo-llsC1noPLFS\]

-   NR-TDD-FR1-CAT-B-mMIMO-ChInfo-ModComp\_\[ConfigDDDFU-100MHz2CC-16SS-25Gbpsx3lane-PRACHC2-Jumbo-llsC3\]

**Table A.3.1.7-1: NR TDD IOT M-MIMO Profile 4 -
NR-TDD-FR1-CAT-B-mMIMO-ChInfo-ModComp**

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Category**            **Item**                                                                                           **Related O-RAN CUS-Plane specification section(s)**   
  ----------------------- -------------------------------------------------------------------------------------------------- ------------------------------------------------------ ----------------------------------------------
  General                 Radio access technology                                                                            \-                                                     NR TDD

                          TDD configuration                                                                                  \-                                                     Entry1: DDDFUUDDDD\
                                                                                                                                                                                    Entry2: DDDFU

                          Nominal sub-carrier spacing                                                                        \-                                                     30kHz

                          SSB sub-carrier spacing                                                                            \-                                                     30kHz

                          Nominal FFT size                                                                                   \-                                                     4096(100MHz_BW)

                          Total channel bandwidth                                                                            \-                                                     Entry1: 100MHz x 1 CC\
                                                                                                                                                                                    Entry2: 100 MHz x 2 CC

                          Number of spatial/antenna streams                                                                  \-                                                     Entry1: 8L (DL), 8 streams (UL)\
                                                                                                                                                                                    Entry2: 16L (DL), 16 streams (UL)

                          Fronthaul Ethernet link                                                                            \-                                                     Entry1: 25Gbps x 2 lane (16L, 1CC)\
                                                                                                                                                                                    Entry2: 25Gbps x 3 lane (16L, 2CC)

                          PRACH preamble format                                                                              \-                                                     Entry1: Long preamble F0\
                                                                                                                                                                                    Entry2: B4\
                                                                                                                                                                                    Entry3: C2

                          O-RU category                                                                                      4.2.1                                                  Category B

                          LAA                                                                                                \-                                                     FALSE

  Delay management        Network delay determination                                                                        4.4.4.2                                                Defined Transport Method

                          O-RU adaptation of delay profile information (based on lls-CU delay profile and transport delay)   4.4.4.3                                                FALSE

                          O-DU timing advance type                                                                           4.4.5-4.4.6, Annex B                                   Fixed timing Advance

                          T1a_max_up                                                                                         4.4, Annex B                                           Less than or equal to 345us

                          T1a_min_up                                                                                         4.4, Annex B                                           More than or equal to 294us

                          T1a_max_cp_dl                                                                                      4.4, Annex B                                           Less than or equal to 820us

                          T1a_min_cp_dl                                                                                      4.4, Annex B                                           More than or equal to 769us

                          T2a_max_up                                                                                         4.4, Annex B                                           More than or equal to 345us

                          T2a_min_up                                                                                         4.4, Annex B                                           Less than or equal to 134us

                          T2a_max_cp_dl                                                                                      4.3.2, Annex B                                         More than or equal to 820us

                          T2a_min_cp_dl                                                                                      4.4, Annex B                                           Less than or equal to 609us

                          Tcp_adv_dl                                                                                         4.4, Annex B                                           475us

                          Ta3_max_up                                                                                         4.4, Annex B                                           Less than or equal to 171us

                          Ta3_min_up                                                                                         4.4, Annex B                                           More than or equal to 50us

                          Ta4_max_up                                                                                         4.4, Annex B                                           More than or equal to 331us

                          Ta4_min_up                                                                                         4.4, Annex B                                           Less than or equal to 50us

                          Ta3_max_up (scs=1.25kHz)                                                                           4.4, Annex B                                           Less than or equal to 1650us

                          Ta3_min_up (scs=1.25kHz)                                                                           4.4, Annex B                                           More than or equal to 827us

                          Ta4_max_up (scs=1.25kHz)                                                                           4.4.3-4.4.4, Annex B                                   More than or equal to 1810us

                          Ta4_min_up (scs=1.25kHz)                                                                           4.4.3-4.4.4, Annex B                                   Less than or equal to 827us

                          T1a_max_cp_ul                                                                                      4.4.3-4.4.4, Annex B                                   Less than or equal to 336us

                          T1a_min_cp_ul                                                                                      4.4.3-4.4.4, Annex B                                   More than or equal to 285us

                          T2a_max_cp_ul                                                                                      4.4, Annex B                                           More than or equal to 336us

                          T2a_min_cp_ul                                                                                      4.4, Annex B                                           Less than or equal to 125us

                          T12_max                                                                                            4.4, Annex B                                           160us

                          T12_min                                                                                            4.4, Annex B                                           0us

                          T34_max                                                                                            4.4, Annex B                                           160us

                          T34_min                                                                                            4.4, Annex B                                           0us

                          Non-delay managed U-Plane traffic                                                                  4.4.7                                                  Support

  C/U-Plane transport     Transport encapsulation                                                                            5.1.1-5.1.2                                            Ethernet

                          Jumbo frames                                                                                       5.1.2                                                  Entry1: TRUE\
                                                                                                                                                                                    Entry2: FALSE

                          Transport header                                                                                   5.1.3                                                  eCPRI

                          eCPRI concatenation                                                                                5.1.3.1-5.1.3.2                                        FALSE

                          eAxC ID DU_Port_ID bitwidth                                                                        5.1.3.2.7                                              5

                          eAxC ID BandSector_ID bitwidth                                                                     5.1.3.2.7                                              1

                          eAxC ID CC_ID bitwidth                                                                             5.1.3.2.7                                              2

                          eAxC ID RU_Port_ID bitwidth                                                                        5.1.3.2.7                                              8

                          Fragmentation                                                                                      5.5                                                    Application layer fragmentation

                          Transport prioritization across C/U/S/M-Plane                                                      5.3                                                    Default L2 CoS Priority

                          Transport prioritization within U-Plane                                                            5.3                                                    TRUE

                          Seperation of C/U-Plane and M-Plane traffic                                                        5.4                                                    VLAN ID

                          Transport-based separation within C/U-Plane traffic                                                5.4                                                    FALSE

  Digital Power Scaling   UL gain_correction                                                                                 8.1.3.2                                                0 dB

  Beamforming             O-RU beamforming type                                                                              4.2.1..(10.1)                                          Digital beamforming

                          Beamforming control method                                                                         7.4, Annex J                                           Chan Info (Frequency Domain)

                          BFW IQ                                                                                             7.4, Annex J                                           NA

  IQ compression          U-Plane data compression method                                                                    8, Annex A                                             DL: Mod COMP, UL: BFP

                          U-Plane (DL/UL) data IQ bitwidth                                                                   8, Annex D                                             DL: Mod COMP, 4 bits (max)\
                                                                                                                                                                                    UL: BFP, 9 bits

                          IQ data frame format not including udCompHdr field                                                 8.3.3.13                                               TRUE

  C-Plane                 Section Type 0                                                                                     7.4.2                                                  TRUE

                          Section Type 1                                                                                     7.4.3                                                  TRUE

                          Section Type 3                                                                                     7.4.5                                                  TRUE

                          Section Type 5                                                                                     7.4.7                                                  TRUE

                          Section Type 6                                                                                     7.4.8                                                  TRUE

                          Section Type 7                                                                                     7.4.9                                                  FALSE

                          \"symInc\" flag                                                                                    7.5.3.3                                                FALSE (always set to \"0\")

                          C-Plane for PRACH formats with preamble repetition                                                 7.2.3.4                                                Single C-Plane message

                          Section extension 1 (beamforming weights)                                                          7.7.1                                                  FALSE

                          Section extension 2 (beamforming attributes)                                                       7.7.2                                                  FALSE

                          Section extension 3 (DL Precoding configuration parameters and indications)                        7.7.3                                                  FALSE

                          Section extension 4 (modulation compr. params)                                                     7.7.4                                                  FALSE

                          Section extension 5 (modulation compression additional scaling parameters)                         7.7.5                                                  TRUE

                          Section extension 6 (Non-contiguous PRB allocation)                                                7.7.6                                                  FALSE

                          Section extension 7 (Multiple-eAxC designation)                                                    7.7.7                                                  FALSE

                          Section extension 8 (regularization factor)                                                        7.7.8                                                  FALSE

                          Section extension 9 (Dynamic Spectrum Sharing parameters)                                          7.7.9                                                  FALSE

                          Section extension 10 (Multiple ports grouping)                                                     7.7.10                                                 TRUE

                          Section extension 11 (Flexible BF weights)                                                         7.7.11                                                 FALSE

                          Section extension 12                                                                               7.7.12                                                 FALSE

                          Section extension 13                                                                               7.7.13                                                 FALSE

                          Section extension 14                                                                               7.7.14                                                 FALSE

                          Section extension 15                                                                               7.7.15                                                 FALSE

                          Section extension 16                                                                               7.7.16                                                 TRUE

                          Section extension 17                                                                               7.7.17                                                 FALSE

  S-Plane                 PTP Full Timing Support (G.8275.1)                                                                 5.2.3, 10.1, 11                                        TRUE

                          PTP Partial Timing Support (G.8275.2)                                                              5.2.3, 10.1, 11                                        FALSE

                          Local PRTC                                                                                         5.2.3, 10.1, 11                                        FALSE

                          Topology configuration                                                                             11.2.2\                                                Entry 1) lls-C1 (can also apply lls-C2)\
                                                                                                                             10, 11.2.3 (for PLFS)                                  Entry 2) lls-C1 (PLFS not required by O-RU)\
                                                                                                                                                                                    Entry 3) lls-C3
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### A.3.1.8 NR TDD IOT M-MIMO Profile 5 - NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Base

Table A.3.1.8-1 describes the base profile. The following PTCs are
defined.

1\) NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Base_PTC1\_\[12bitFP.BFW\]

2\) NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Base_PTC2\_\[8bitBFP.BFW\]

**Table A.3.1.8-1: NR TDD IOT M-MIMO Profile 5:
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Base**

+----------------+----------------+----------------+----------------+
| Category       | Item           | Related O-RAN  |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)     |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR TDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | DDDSUUDDDD     |
|                | configuration  |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    |                | 4096           |
|                | size           |                |                |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | 100MHz x 1 CC  |
|                | bandwidth      |                |                |
+----------------+----------------+----------------+----------------+
|                | Number of user | \-             | DL: 2 -- 16    |
|                | layers         |                |                |
|                |                |                | UL: 2 -- 8     |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 25Gbps x 1     |
|                | Ethernet link  |                | lane           |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | O-RU REQ: F0   |
|                | format         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-RU category  | 4.2.1          | Category B     |
+----------------+----------------+----------------+----------------+
|                | LAA            | 7.2.5          | N/A            |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4          | Defined        |
| management,    | determination  |                | Transport      |
| general        |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 4.4.4.3        | NOT REQ        |
|                | adaptation of  |                |                |
|                | delay profile  |                |                |
|                | information    |                |                |
|                | (based on      |                |                |
|                | lls-CU delay   |                |                |
|                | profile and    |                |                |
|                | transport      |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | REQ: Fixed     |
|                | advance type   | Annex B        | timing Advance |
+----------------+----------------+----------------+----------------+
|                | SRS transfer   | 4.4.7          | REQ: Non-delay |
|                |                |                | managed        |
|                |                |                | U-Plane        |
+----------------+----------------+----------------+----------------+
| Delay          | Delay Sets for |                | REQ: Table     |
| management,    | timing         |                | A.4.1-1        |
| default        | parameters     |                |                |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
| Delay          | non-default    | 12.6.3         | REQ:           |
| management,    | beamforming    |                | DMRS-BF-EQ     |
| non default    | methods \#1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Delay Sets for |                | REQ: Table     |
|                | timing         |                | A.4.3-1        |
|                | parameters     |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | REQ: eCPRI     |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5.1.3.2        | NOT REQ        |
|                | concatenation  |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 3    |
|                | DU_Port_ID     |                | and 2          |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 2    |
|                | BandSector_ID  |                | and 3          |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | O-RU REQ: 3    |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 8    |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
|                |                |                | REQ            |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | Priority REQ   |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | NOT REQ        |
|                | prioritization |                |                |
|                | within U-Plane |                |                |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID REQ    |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | NOT REQ        |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0 dB           |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
|                | (not           |                |                |
|                | applicable to  |                |                |
|                | DMRS-BF-EQ)    |                |                |
+----------------+----------------+----------------+----------------+
|                | equalizatio    | 12.6.3.5       | REQ:           |
|                | n-data-scaling |                | Sca            |
|                |                |                | ling-function1 |
|                |                |                | or             |
|                |                |                | Sca            |
|                |                |                | ling-function2 |
+----------------+----------------+----------------+----------------+
| Beamforming    | O-RU           | 4.2.1          | REQ: Digital   |
|                | beamforming    |                | beamforming    |
|                | type           |                |                |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.2.1, 12.6,   | DL: REQ: WDBF  |
|                | control method | Annex J        | and PDBF       |
|                |                |                |                |
|                |                |                | UL: REQ:       |
|                |                |                | DMRS-BF for    |
|                |                |                | PUSCH, WDBF or |
|                |                |                | PDBF for       |
|                |                |                | non-PUSCH      |
+----------------+----------------+----------------+----------------+
|                | BFW IQ         | 7.7.1, Annex J | REQ            |
|                |                |                |                |
|                |                |                | PTC1: Fixed    |
|                |                |                | point, 12 bits |
|                |                |                |                |
|                |                |                | PTC2: BFP, 8   |
|                |                |                | bits           |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | REQ: BFP       |
|                | compression    |                |                |
|                | method         |                |                |
+----------------+----------------+----------------+----------------+
|                | U-Plane        | 8, Annex D     | DL: REQ: 9     |
|                | (DL/UL) data   |                | bits           |
|                | IQ bitwidth    |                |                |
|                |                |                | UL: REQ: 8 and |
|                |                |                | 9 bits         |
|                |                |                | (PUSCH), 9     |
|                |                |                | bits for other |
|                |                |                | UL channels    |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | REQ            |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | REQ (for PRACH |
|                |                |                | )              |
+----------------+----------------+----------------+----------------+
|                | Section Type 4 | 7.4.6          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | REQ (for       |
|                |                |                | DMRS-BF)       |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | N/A            |
+----------------+----------------+----------------+----------------+
|                | Section Type 8 | 7.4.10         | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 9 | 7.4.11         | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section Type   | 7.4.12         | REQ            |
|                | 10             |                |                |
+----------------+----------------+----------------+----------------+
|                | Section Type   | 7.4.13         | O-RU REQ       |
|                | 11             |                |                |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | NOT REQ        |
|                | flag           |                |                |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | REQ: Single    |
|                | PRACH formats  |                | C-Plane        |
|                | with preamble  |                | message        |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | REQ            |
|                | extension 1    |                |                |
|                | (beamforming   |                |                |
|                | weights)       |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | NOT REQ        |
|                | extension 2    |                |                |
|                | (beamforming   |                |                |
|                | attributes)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | NOT REQ        |
|                | extension 3    |                |                |
|                | (DL Precoding  |                |                |
|                | configuration  |                |                |
|                | parameters and |                |                |
|                | indications)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | NOT REQ        |
|                | extension 4    |                |                |
|                | (modulation    |                |                |
|                | compr. params) |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | NOT REQ        |
|                | extension 5    |                |                |
|                | (modulation    |                |                |
|                | compression    |                |                |
|                | additional     |                |                |
|                | scaling        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.6          | NOT REQ        |
|                | extension 6    |                |                |
|                | (              |                |                |
|                | Non-contiguous |                |                |
|                | PRB            |                |                |
|                | allocation)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.7          | NOT REQ        |
|                | extension 7    |                |                |
|                | (Multiple-eAxC |                |                |
|                | designation)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.8          | NOT REQ        |
|                | extension 8    |                |                |
|                | (              |                |                |
|                | regularization |                |                |
|                | factor)        |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.9          | NOT REQ        |
|                | extension 9    |                |                |
|                | (Dynamic       |                |                |
|                | Spectrum       |                |                |
|                | Sharing        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.10         | REQ (for       |
|                | extension 10   |                | DMRS-BF)       |
|                | (Multiple      |                |                |
|                | ports          |                |                |
|                | grouping)      |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.11         | NOT REQ        |
|                | extension 11   |                |                |
|                | (Flexible BF   |                |                |
|                | weights)       |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.12         | NOT REQ        |
|                | extension 12   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.13         | NOT REQ        |
|                | extension 13   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.14         | NOT REQ        |
|                | extension 14   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.15         | NOT REQ        |
|                | extension 15   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.16         | NOT REQ        |
|                | extension 16   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.17         | NOT REQ        |
|                | extension 17   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.18         | NOT REQ        |
|                | extension 18   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.19         | NOT REQ        |
|                | extension 19   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.20         | NOT REQ        |
|                | extension 20   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.21         | NOT REQ        |
|                | extension 21   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.22         | NOT REQ        |
|                | extension 22   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.23         | NOT REQ        |
|                | extension 23   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.24         | REQ            |
|                | extension 24   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.25         | NOT REQ        |
|                | extension 25   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.26         | NOT REQ        |
|                | extension 26   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.27         | NOT REQ        |
|                | extension 27   |                |                |
+----------------+----------------+----------------+----------------+
| DMRS-BF        | Port reduced   | 12.6.3.1       | O-RU REQ       |
|                | DMRS data      |                |                |
|                | sending        |                |                |
+----------------+----------------+----------------+----------------+
|                | User group     | 7.7.24         | NOT REQ        |
|                | self assembly  |                |                |
+----------------+----------------+----------------+----------------+
|                | Per-window     | 7.7.25,        | NOT REQ        |
|                | symbol         | 12.6.1.5       |                |
|                | reordering     |                |                |
|                | with DMRS      |                |                |
|                | sending        |                |                |
+----------------+----------------+----------------+----------------+
|                | Per section    | 7.7.25,        | NOT REQ        |
|                | tx-window      | 12.6.1.5       |                |
|                | reassignment   |                |                |
+----------------+----------------+----------------+----------------+
|                | symbolid       | 7.7.25         | N/A            |
|                | meaining when  |                |                |
|                | reordering     |                |                |
|                | (up-symbolId-t |                |                |
|                | ype-supported) |                |                |
+----------------+----------------+----------------+----------------+
|                | Transform      | 7.7.24         | O-RU REQ       |
|                | precoding      |                |                |
|                | supported      |                |                |
+----------------+----------------+----------------+----------------+
|                | PUSCH and DMRS | 7.7.24         | NOT REQ        |
|                | mux supported  |                |                |
+----------------+----------------+----------------+----------------+
|                | DMRS           | 7.7.24,        | REQ: Type 1    |
|                | configuration  | 7.7.24.14      | (dType=0)      |
|                | Type (dType)   |                |                |
+----------------+----------------+----------------+----------------+
|                | dmrsSymbolMask | 7.7.24         | REQ: 1+1       |
|                |                |                | (symbol        |
|                |                |                | location: 2,   |
|                |                |                | 11)            |
+----------------+----------------+----------------+----------------+
|                | different-t    | 7.7.24         | NOT REQ        |
|                | ransform-preco |                |                |
|                | ding-in-user-g |                |                |
|                | roup-supported |                |                |
+----------------+----------------+----------------+----------------+
|                | differen       | 7.7.24         | NOT REQ        |
|                | t-cdm-without- |                |                |
|                | data-in-user-g |                |                |
|                | roup-supported |                |                |
+----------------+----------------+----------------+----------------+
| Measurements   | SINR reporting | 7.2.11, 7.4.11 | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | MEAS-UE-TAE    | 9.2.1          | O-RU REQ       |
|                | (UE timing     |                |                |
|                | advance error) |                |                |
+----------------+----------------+----------------+----------------+
|                | MEAS-          | 9.2.1          | O-RU REQ       |
|                | UE-LAYER-POWER |                |                |
+----------------+----------------+----------------+----------------+
|                | MEAS-          | 9.2.1          | O-RU REQ       |
|                | UE-FREQ-OFFSET |                |                |
+----------------+----------------+----------------+----------------+
|                | MEAS-IPN-ALLOC | 9.2.1          | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | ME             | 9.2.1          | O-RU REQ       |
|                | AS-IPN-UNALLOC |                |                |
+----------------+----------------+----------------+----------------+
|                | MEA            | 9.2.1          | NOT REQ        |
|                | S-ANT-DMRS-SNR |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | REQ            |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | NOT REQ        |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | N/A            |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2,\       | REQ: LLS-C1 or |
|                | configuration  | 11.2.3 (for    | LLS-C3         |
|                |                | PLFS)          |                |
+----------------+----------------+----------------+----------------+

Table A.3.1.8-2 lists "to be reported" and "to be validated"
capabilities in radio layer 3 C-plane establishment and initial radio
U-plane data transfer test. Table A.3.1.8-3 lists "to be reported" and
"to be validated" capabilities in U-plane DL data transfer test. Table
A.3.1.8-4 lists "to be reported" and "to be validated" capabilities in
U-plane UL data transfer test.

Table A.3.1.8-2: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 5 in radio layer 3 C-Plane establishment and initial
radio U-Plane data transfer test

  PTCs   
  ------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: WDBF for DL, DMRS-BF-EQ for PUSCH
         Capabilities to be reported: PDBF for DL, BFW Fixed point 12 bits, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Non-delay managed U-plane for SRS transfer
  PTC2   Capabilities to be validated: WDBF for DL, DMRS-BF-EQ for PUSCH
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Non-delay managed U-plane for SRS transfer

**Table A.3.1.8-3: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 5 in U-Plane DL data transfer test**

  PTCs   
  ------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: WDBF for DL
         Capabilities to be reported: PDBF for DL, BFW Fixed point 12 bits, DMRS-BF-EQ for PUSCH, Non-delay managed U-plane for SRS transfer, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits)
  PTC2   Capabilities to be validated: WDBF for DL
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, DMRS-BF-EQ for PUSCH, Non-delay managed U-plane for SRS transfer, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits)

**Table A.3.1.8-4: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 5 in U-Plane data UL transfer test**

  PTCs   
  ------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: DMRS-BF-EQ for PUSCH
         Capabilities to be reported: WDBF or PDBF for DL, BFW Fixed point 12 bits, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Non-delay managed U-plane for SRS transfer
  PTC2   Capabilities to be validated: DMRS-BF-EQ for PUSCH
         Capabilities to be reported: WDBF or PDBF for DL, BFW BFP 8 bits, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Non-delay managed U-plane for SRS transfer

#### A.3.1.9 NR TDD IOT M-MIMO Profile 6 - NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-NEQ-Base

Table A.3.1.9-1 describes the base profile. The following PTCs are
defined.

1\) NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-NEQ-Base_PTC1\_\[12bitFP.BFW\]

2\) NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-NEQ-Base_PTC2\_\[8bitBFP.BFW\]

**Table A.3.1.9-1: NR TDD IOT M-MIMO Profile 6:
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-NEQ-Base**

+----------------+----------------+----------------+----------------+
| Category       | Item           | Related O-RAN  |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)     |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR TDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | DDDSUUDDDD     |
|                | configuration  |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    |                | 4096           |
|                | size           |                |                |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | 100MHz x 1 CC  |
|                | bandwidth      |                |                |
+----------------+----------------+----------------+----------------+
|                | Number of user | \-             | DL: 2 -- 16    |
|                | layers         |                |                |
|                |                |                | UL: 2 -- 8     |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 25Gbps x 1     |
|                | Ethernet link  |                | lane           |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | O-RU REQ: F0   |
|                | format         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-RU category  | 4.2.1          | Category B     |
+----------------+----------------+----------------+----------------+
|                | LAA            | 7.2.5          | N/A            |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4          | Defined        |
| management,    | determination  |                | Transport      |
| general        |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 4.4.4.3        | NOT REQ        |
|                | adaptation of  |                |                |
|                | delay profile  |                |                |
|                | information    |                |                |
|                | (based on      |                |                |
|                | lls-CU delay   |                |                |
|                | profile and    |                |                |
|                | transport      |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | REQ: Fixed     |
|                | advance type   | Annex B        | timing Advance |
+----------------+----------------+----------------+----------------+
|                | SRS transfer   | 4.4.7          | REQ: Non-delay |
|                |                |                | managed        |
|                |                |                | U-Plane        |
+----------------+----------------+----------------+----------------+
| Delay          | Delay Sets for |                | REQ: Table     |
| management,    | timing         |                | A.4.1-1        |
| default        | parameters     |                |                |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
| Delay          | non-default    | 12.6.3         | REQ:           |
| management,    | beamforming    |                | DMRS-BF-NEQ    |
| non default    | methods \#1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Delay Sets for |                | REQ: Table     |
|                | timing         |                | A.4.3-1        |
|                | parameters     |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | REQ: eCPRI     |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5.1.3.2        | NOT REQ        |
|                | concatenation  |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 3    |
|                | DU_Port_ID     |                | and 2          |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 2    |
|                | BandSector_ID  |                | and 3          |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | O-RU REQ: 3    |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 8    |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
|                |                |                | REQ            |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | Priority REQ   |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | NOT REQ        |
|                | prioritization |                |                |
|                | within U-Plane |                |                |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID REQ    |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | NOT REQ        |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0 dB           |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
|                | (not           |                |                |
|                | applicable to  |                |                |
|                | DMRS-BF-EQ)    |                |                |
+----------------+----------------+----------------+----------------+
|                | equalizatio    | 12.6.3.5       | N/A            |
|                | n-data-scaling |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | O-RU           | 4.2.1          | REQ: Digital   |
|                | beamforming    |                | beamforming    |
|                | type           |                |                |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.2.1, 12.6,   | DL: REQ: WDBF  |
|                | control method | Annex J        | and PDBF       |
|                |                |                |                |
|                |                |                | UL: REQ:       |
|                |                |                | DMRS-BF for    |
|                |                |                | PUSCH, WDBF or |
|                |                |                | PDBF for       |
|                |                |                | non-PUSCH      |
+----------------+----------------+----------------+----------------+
|                | BFW IQ         | 7.7.1, Annex J | REQ            |
|                |                |                |                |
|                |                |                | PTC1: Fixed    |
|                |                |                | point, 12 bits |
|                |                |                |                |
|                |                |                | PTC2: BFP, 8   |
|                |                |                | bits           |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | REQ: BFP       |
|                | compression    |                |                |
|                | method         |                |                |
+----------------+----------------+----------------+----------------+
|                | U-Plane        | 8, Annex D     | DL: REQ: 9     |
|                | (DL/UL) data   |                | bits           |
|                | IQ bitwidth    |                |                |
|                |                |                | UL: REQ: 9     |
|                |                |                | bits           |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | REQ            |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | REQ (for PRACH |
|                |                |                | )              |
+----------------+----------------+----------------+----------------+
|                | Section Type 4 | 7.4.6          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | REQ (for       |
|                |                |                | DMRS-BF)       |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | N/A            |
+----------------+----------------+----------------+----------------+
|                | Section Type 8 | 7.4.10         | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 9 | 7.4.11         | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type   | 7.4.12         | NOT REQ        |
|                | 10             |                |                |
+----------------+----------------+----------------+----------------+
|                | Section Type   | 7.4.13         | NOT REQ        |
|                | 11             |                |                |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | NOT REQ        |
|                | flag           |                |                |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | REQ: Single    |
|                | PRACH formats  |                | C-Plane        |
|                | with preamble  |                | message        |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | REQ            |
|                | extension 1    |                |                |
|                | (beamforming   |                |                |
|                | weights)       |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | NOT REQ        |
|                | extension 2    |                |                |
|                | (beamforming   |                |                |
|                | attributes)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | NOT REQ        |
|                | extension 3    |                |                |
|                | (DL Precoding  |                |                |
|                | configuration  |                |                |
|                | parameters and |                |                |
|                | indications)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | NOT REQ        |
|                | extension 4    |                |                |
|                | (modulation    |                |                |
|                | compr. params) |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | NOT REQ        |
|                | extension 5    |                |                |
|                | (modulation    |                |                |
|                | compression    |                |                |
|                | additional     |                |                |
|                | scaling        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.6          | NOT REQ        |
|                | extension 6    |                |                |
|                | (              |                |                |
|                | Non-contiguous |                |                |
|                | PRB            |                |                |
|                | allocation)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.7          | NOT REQ        |
|                | extension 7    |                |                |
|                | (Multiple-eAxC |                |                |
|                | designation)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.8          | NOT REQ        |
|                | extension 8    |                |                |
|                | (              |                |                |
|                | regularization |                |                |
|                | factor)        |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.9          | NOT REQ        |
|                | extension 9    |                |                |
|                | (Dynamic       |                |                |
|                | Spectrum       |                |                |
|                | Sharing        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.10         | REQ (for       |
|                | extension 10   |                | DMRS-BF)       |
|                | (Multiple      |                |                |
|                | ports          |                |                |
|                | grouping)      |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.11         | NOT REQ        |
|                | extension 11   |                |                |
|                | (Flexible BF   |                |                |
|                | weights)       |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.12         | NOT REQ        |
|                | extension 12   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.13         | NOT REQ        |
|                | extension 13   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.14         | NOT REQ        |
|                | extension 14   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.15         | NOT REQ        |
|                | extension 15   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.16         | NOT REQ        |
|                | extension 16   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.17         | NOT REQ        |
|                | extension 17   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.18         | NOT REQ        |
|                | extension 18   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.19         | NOT REQ        |
|                | extension 19   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.20         | NOT REQ        |
|                | extension 20   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.21         | NOT REQ        |
|                | extension 21   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.22         | NOT REQ        |
|                | extension 22   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.23         | NOT REQ        |
|                | extension 23   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.24         | REQ            |
|                | extension 24   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.25         | NOT REQ        |
|                | extension 25   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.26         | NOT REQ        |
|                | extension 26   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.27         | NOT REQ        |
|                | extension 27   |                |                |
+----------------+----------------+----------------+----------------+
| DMRS-BF        | Port reduced   | 12.6.3.1       | REQ            |
|                | DMRS data      |                |                |
|                | sending        |                |                |
+----------------+----------------+----------------+----------------+
|                | User group     | 7.7.24         | N/A            |
|                | self assembly  |                |                |
+----------------+----------------+----------------+----------------+
|                | Per-window     | 7.7.25,        | NOT REQ        |
|                | symbol         | 12.6.1.5       |                |
|                | reordering     |                |                |
|                | with DMRS      |                |                |
|                | sending        |                |                |
+----------------+----------------+----------------+----------------+
|                | Per section    | 7.7.25,        | NOT REQ        |
|                | tx-window      | 12.6.1.5       |                |
|                | reassignment   |                |                |
+----------------+----------------+----------------+----------------+
|                | symbolid       | 7.7.25         | N/A            |
|                | meaining when  |                |                |
|                | reordering     |                |                |
|                | (up-symbolId-t |                |                |
|                | ype-supported) |                |                |
+----------------+----------------+----------------+----------------+
|                | Transform      | 7.7.24         | O-RU REQ       |
|                | precoding      |                |                |
|                | supported      |                |                |
+----------------+----------------+----------------+----------------+
|                | PUSCH and DMRS | 7.7.24         | NOT REQ        |
|                | mux supported  |                |                |
+----------------+----------------+----------------+----------------+
|                | DMRS           | 7.7.24,        | REQ: Type 1    |
|                | configuration  | 7.7.24.14      | (dType=0)      |
|                | Type (dType)   |                |                |
+----------------+----------------+----------------+----------------+
|                | dmrsSymbolMask | 7.7.24         | REQ: 1+1       |
|                |                |                | (symbol        |
|                |                |                | location: 2,   |
|                |                |                | 11)            |
+----------------+----------------+----------------+----------------+
|                | different-t    | 7.7.24         | NOT REQ        |
|                | ransform-preco |                |                |
|                | ding-in-user-g |                |                |
|                | roup-supported |                |                |
+----------------+----------------+----------------+----------------+
|                | differen       | 7.7.24         | NOT REQ        |
|                | t-cdm-without- |                |                |
|                | data-in-user-g |                |                |
|                | roup-supported |                |                |
+----------------+----------------+----------------+----------------+
| Measurements   | SINR reporting | 7.2.11, 7.4.11 | N/A            |
+----------------+----------------+----------------+----------------+
|                | MEAS-UE-TAE    | 9.2.1          | NOT REQ.       |
|                | (UE timing     |                |                |
|                | advance error) |                | O-RU declares  |
|                |                |                | feature        |
|                |                |                | DMRS-BF-NEQ-   |
|                |                |                | UNALTERED-TAE. |
+----------------+----------------+----------------+----------------+
|                | MEAS-          | 9.2.1          | NOT REQ        |
|                | UE-LAYER-POWER |                |                |
+----------------+----------------+----------------+----------------+
|                | MEAS-          | 9.2.1          | NOT REQ.       |
|                | UE-FREQ-OFFSET |                |                |
|                |                |                | O-RU declares  |
|                |                |                | feature        |
|                |                |                | DMRS-B         |
|                |                |                | F-NEQ-UNALTERE |
|                |                |                | D-FREQ-OFFSET. |
+----------------+----------------+----------------+----------------+
|                | MEAS-IPN-ALLOC | 9.2.1          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | ME             | 9.2.1          | NOT REQ        |
|                | AS-IPN-UNALLOC |                |                |
+----------------+----------------+----------------+----------------+
|                | MEA            | 9.2.1          | NOT REQ        |
|                | S-ANT-DMRS-SNR |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | REQ            |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | NOT REQ        |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | N/A            |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2,\       | REQ: LLS-C1 or |
|                | configuration  | 11.2.3 (for    | LLS-C3         |
|                |                | PLFS)          |                |
+----------------+----------------+----------------+----------------+

Table A.3.1.9-2 lists "to be reported" and "to be validated"
capabilities in radio layer 3 C-plane establishment and initial radio
U-plane data transfer test. Table A.3.1.9-3 lists "to be reported" and
"to be validated" capabilities in U-plane DL data transfer test. Table
A.3.1.9-4 lists "to be reported" and "to be validated" capabilities in
U-plane UL data transfer test.

Table A.3.1.9-2: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 6 in radio layer 3 C-Plane establishment and initial
radio U-Plane data transfer test

  PTCs   
  ------ ----------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: WDBF for DL, DMRS-BF-NEQ for PUSCH
         Capabilities to be reported: PDBF for DL, BFW Fixed point 12 bits, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer
  PTC2   Capabilities to be validated: WDBF for DL, DMRS-BF-NEQ for PUSCH
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer

Table A.3.1.9-3: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 6 in U-Plane DL data transfer test

  PTCs   
  ------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: WDBF for DL
         Capabilities to be reported: PDBF for DL, BFW Fixed point 12 bits, DMRS-BF-NEQ for PUSCH, Non-delay managed U-plane for SRS transfer, eAxC-ID format (3238 or 2338)
  PTC2   Capabilities to be validated: WDBF for DL
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, DMRS-BF-NEQ for PUSCH, Non-delay managed U-plane for SRS transfer, eAxC-ID format (3238 or 2338)

Table A.3.1.9-4: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 5 in U-Plane data UL transfer test

  PTCs   
  ------ ------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: DMRS-BF-NEQ for PUSCH
         Capabilities to be reported: WDBF or PDBF for DL, BFW Fixed point 12 bits, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer
  PTC2   Capabilities to be validated: DMRS-BF-NEQ for PUSCH
         Capabilities to be reported: WDBF or PDBF for DL, BFW BFP 8 bits, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer

#### A.3.1.10 NR TDD IOT M-MIMO Profile 7 - NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Enhanced

Table A.3.1.10-1 describes the base profile. The following PTCs are
defined.

1\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Enh_PTC1\_\[12bitFP.BFW-nondelay.SRS-SE4.ModComp-noSE5-noSE6-noSE11-noSE12-noSE23-noSE27-noSelRE-noSA\]

2\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Enh_PTC2\_\[8bitBFP.BFW-nondelay.SRS-SE4.ModComp-noSE5-noSE6-noSE11-noSE12-noSE23-noSE27-noSelRE-noSA\]

3\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Enh_PTC3\_\[8bitBFP.BFW-nondelay.SRS-SE4.SE5.ModComp-SE6-SE11-SE12-noSE23-noSE27-noSelRE-noSA\]

4\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Enh_PTC4\_\[8bitBFP.BFW-MplaneTxWindow.SRS-SE4.ModComp-noSE5-SE6-SE11-SE12-noSE23-noSE27-noSelRE-noSA\]

5\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Enh_PTC5\_\[8bitBFP.BFW-MplaneTxWindow.SRS-SE4.ModComp-noSE5-SE6-SE11-SE12-noSE23-SE27-noSelRE-noSA\]

6\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Enh_PTC6\_\[8bitBeamSpaceII.8bitBFP.BFW-MplaneTxWindow.SRS-SE4.SE5.ModComp-SE6-SE11-SE12-SE23-noSE27-SelRE-SAID\]

Table A.3.1.10-1: NR TDD IOT M-MIMO Profile 7:
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Enhanced

+----------------+----------------+----------------+----------------+
| Category       | Item           | Related O-RAN  |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)     |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR TDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | DDDSUUDDDD     |
|                | configuration  |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    |                | 4096           |
|                | size           |                |                |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | 100MHz x 1 CC  |
|                | bandwidth      |                |                |
+----------------+----------------+----------------+----------------+
|                | Number of user | \-             | DL: 2 -- 16    |
|                | layers         |                |                |
|                |                |                | UL: 2 -- 8     |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 25Gbps x 1     |
|                | Ethernet link  |                | lane           |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | O-RU REQ: F0   |
|                | format         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-RU category  | 4.2.1          | Category B     |
+----------------+----------------+----------------+----------------+
|                | LAA            | 7.2.5          | N/A            |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4          | Defined        |
| management,    | determination  |                | Transport      |
| general        |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 4.4.4.3        | NOT REQ        |
|                | adaptation of  |                |                |
|                | delay profile  |                |                |
|                | information    |                |                |
|                | (based on      |                |                |
|                | lls-CU delay   |                |                |
|                | profile and    |                |                |
|                | transport      |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | REQ: Fixed     |
|                | advance type   | Annex B        | timing Advance |
+----------------+----------------+----------------+----------------+
|                | SRS transfer   | 4.4.7, 4.6.4   | PTC4, PTC5,    |
|                |                |                | PTC6: M-Plane  |
|                |                |                | static window  |
|                |                |                | control        |
|                |                |                | (STATIC-       |
|                |                |                | TRANSMISSION-W |
|                |                |                | INDOW-CONTROL) |
|                |                |                | REQ            |
|                |                |                |                |
|                |                |                | PTC1, PTC2,    |
|                |                |                | PTC3:          |
|                |                |                | Non-delay      |
|                |                |                | managed        |
|                |                |                | U-Plane REQ    |
+----------------+----------------+----------------+----------------+
| Delay          | Delay Sets for |                | REQ: Table     |
| management,    | timing         |                | A.4.1-1        |
| default        | parameters     |                |                |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
| Delay          | non-default    | 12.6.3         | REQ:           |
| management,    | beamforming    |                | DMRS-BF-EQ     |
| non default    | methods \#1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Delay Sets for |                | REQ: Table     |
|                | timing         |                | A.4.3-1        |
|                | parameters     |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | REQ: eCPRI     |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5.1.3.2        | NOT REQ        |
|                | concatenation  |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 3    |
|                | DU_Port_ID     |                | and 2          |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 2    |
|                | BandSector_ID  |                | and 3          |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | O-RU REQ: 3    |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 8    |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
|                |                |                | REQ            |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | Priority REQ   |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | NOT REQ        |
|                | prioritization |                |                |
|                | within U-Plane |                |                |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID REQ    |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | NOT REQ        |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0 dB           |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
|                | (not           |                |                |
|                | applicable to  |                |                |
|                | DMRS-BF-EQ)    |                |                |
+----------------+----------------+----------------+----------------+
|                | equalizatio    | 12.6.3.5       | REQ:           |
|                | n-data-scaling |                | Sca            |
|                |                |                | ling-function1 |
|                |                |                | or             |
|                |                |                | Sca            |
|                |                |                | ling-function2 |
+----------------+----------------+----------------+----------------+
| Beamforming    | O-RU           | 4.2.1          | REQ: Digital   |
|                | beamforming    |                | beamforming    |
|                | type           |                |                |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.2.1, 12.6,   | DL: REQ: WDBF  |
|                | control method | Annex J        | and PDBF       |
|                |                |                |                |
|                |                |                | UL: REQ:       |
|                |                |                | DMRS-BF for    |
|                |                |                | PUSCH, WDBF or |
|                |                |                | PDBF for       |
|                |                |                | non-PUSCH      |
+----------------+----------------+----------------+----------------+
|                | BFW IQ         | 7.7.1, Annex J | REQ:           |
|                |                |                |                |
|                |                |                | PTC1: Fixed    |
|                |                |                | point, 12 bits |
|                |                |                |                |
|                |                |                | PTC2, PTC3,    |
|                |                |                | PTC4, PTC5:    |
|                |                |                | BFP, 8 bits    |
|                |                |                |                |
|                |                |                | O-RU REQ:      |
|                |                |                |                |
|                |                |                | PTC6:          |
|                |                |                | Beamspace      |
|                |                |                | compression    |
|                |                |                | Type II (8     |
|                |                |                | bits) and BFP  |
|                |                |                | (8 bits)       |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | DL: O-RU REQ   |
|                | compression    |                |                |
|                | method         |                | PTC1, PTC2,    |
|                |                |                | PTC3, PTC4,    |
|                |                |                | PTC5: Mod      |
|                |                |                | Comp, no sel   |
|                |                |                | RE             |
|                |                |                |                |
|                |                |                | PTC6: Mod      |
|                |                |                | Comp, with sel |
|                |                |                | RE.            |
|                |                |                |                |
|                |                |                | UL: REQ BFP    |
+----------------+----------------+----------------+----------------+
|                | U-Plane        | 8, Annex D     | REQ            |
|                | (DL/UL) data   |                |                |
|                | IQ bitwidth    |                | for Mod Comp   |
|                |                |                | in DL: 4 bits  |
|                |                |                |                |
|                |                |                | for BFP in UL: |
|                |                |                | 8 and 9 bits   |
|                |                |                | for DMRS-BF    |
|                |                |                | and 9 bits for |
|                |                |                | other BF       |
|                |                |                | methods        |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | REQ            |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | REQ (for PRACH |
|                |                |                | )              |
+----------------+----------------+----------------+----------------+
|                | Section Type 4 | 7.4.6          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | REQ (for       |
|                |                |                | DMRS-BF)       |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | N/A            |
+----------------+----------------+----------------+----------------+
|                | Section Type 8 | 7.4.10         | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 9 | 7.4.11         | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section Type   | 7.4.12         | REQ            |
|                | 10             |                |                |
+----------------+----------------+----------------+----------------+
|                | Section Type   | 7.4.13         | O-RU REQ       |
|                | 11             |                |                |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | NOT REQ        |
|                | flag           |                |                |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | REQ: Single    |
|                | PRACH formats  |                | C-Plane        |
|                | with preamble  |                | message        |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | REQ            |
|                | extension 1    |                |                |
|                | (beamforming   |                |                |
|                | weights)       |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | NOT REQ        |
|                | extension 2    |                |                |
|                | (beamforming   |                |                |
|                | attributes)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | NOT REQ        |
|                | extension 3    |                |                |
|                | (DL Precoding  |                |                |
|                | configuration  |                |                |
|                | parameters and |                |                |
|                | indications)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | O-RU REQ       |
|                | extension 4    |                |                |
|                | (modulation    |                |                |
|                | compr. params) |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | PTC1, PTC2,    |
|                | extension 5    |                | PTC,4, PTC5:   |
|                | (modulation    |                | NOT REQ        |
|                | compression    |                |                |
|                | additional     |                | PTC3, PTC6:    |
|                | scaling        |                | O-RU REQ       |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.6          | PTC1, PTC2:    |
|                | extension 6    |                | NOT REQ        |
|                | (              |                |                |
|                | Non-contiguous |                | PTC3, PTC4,    |
|                | PRB            |                | PTC5, PTC6:    |
|                | allocation)    |                | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.7          | NOT REQ        |
|                | extension 7    |                |                |
|                | (Multiple-eAxC |                |                |
|                | designation)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.8          | NOT REQ        |
|                | extension 8    |                |                |
|                | (              |                |                |
|                | regularization |                |                |
|                | factor)        |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.9          | NOT REQ        |
|                | extension 9    |                |                |
|                | (Dynamic       |                |                |
|                | Spectrum       |                |                |
|                | Sharing        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.10         | REQ (for       |
|                | extension 10   |                | DMRS-BF)       |
|                | (Multiple      |                |                |
|                | ports          |                |                |
|                | grouping)      |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.11         | PTC1, PTC2:    |
|                | extension 11   |                | NOT REQ        |
|                | (Flexible BF   |                |                |
|                | weights)       |                | PTC3, PTC4,    |
|                |                |                | PTC5, PTC6:    |
|                |                |                | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.12         | PTC1, PTC2:    |
|                | extension 12   |                | NOT REQ        |
|                |                |                |                |
|                |                |                | PTC3, PTC4,    |
|                |                |                | PTC5, PTC6:    |
|                |                |                | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.13         | NOT REQ        |
|                | extension 13   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.14         | NOT REQ        |
|                | extension 14   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.15         | NOT REQ        |
|                | extension 15   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.16         | NOT REQ        |
|                | extension 16   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.17         | NOT REQ        |
|                | extension 17   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.18         | NOT REQ        |
|                | extension 18   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.19         | NOT REQ        |
|                | extension 19   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.20         | NOT REQ        |
|                | extension 20   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.21         | NOT REQ        |
|                | extension 21   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.22         | NOT REQ        |
|                | extension 22   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.23         | PTC1, PTC2,    |
|                | extension 23   |                | PTC3, PTC4,    |
|                |                |                | PTC5: NOT REQ  |
|                |                |                |                |
|                |                |                | PTC6: O-RU REQ |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.24         | REQ            |
|                | extension 24   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.25         | NOT REQ        |
|                | extension 25   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.26         | O-RU REQ       |
|                | extension 26   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.27         | PTC1, PTC2,    |
|                | extension 27   |                | PTC3, PTC4,    |
|                |                |                | PTC6: NOT REQ  |
|                |                |                |                |
|                |                |                | PTC5: REQ      |
+----------------+----------------+----------------+----------------+
| DMRS-BF        | Port reduced   | 12.6.3.1       | O-RU REQ       |
|                | DMRS data      |                |                |
|                | sending        |                |                |
+----------------+----------------+----------------+----------------+
|                | User group     | 7.7.24         | PTC1, PTC2,    |
|                | self assembly  |                | PTC3, PTC4,    |
|                |                |                | PTC5: NOT REQ  |
|                |                |                | (no            |
|                |                |                | self-assembly  |
|                |                |                | = noSA)        |
|                |                |                |                |
|                |                |                | PTC6: O-RU     |
|                |                |                | REQ: SAID      |
|                |                |                | (self assembly |
|                |                |                | with id)       |
+----------------+----------------+----------------+----------------+
|                | Per-window     | 7.7.25,        | NOT REQ        |
|                | symbol         | 12.6.1.5       |                |
|                | reordering     |                |                |
|                | with DMRS      |                |                |
|                | sending        |                |                |
+----------------+----------------+----------------+----------------+
|                | Per section    | 7.7.25,        | NOT REQ        |
|                | tx-window      | 12.6.1.5       |                |
|                | reassignment   |                |                |
+----------------+----------------+----------------+----------------+
|                | symbolid       | 7.7.25         | N/A            |
|                | meaining when  |                |                |
|                | reordering     |                |                |
|                | (up-symbolId-  |                |                |
|                | type-supporte) |                |                |
+----------------+----------------+----------------+----------------+
|                | Transform      | 7.7.24         | O-RU REQ       |
|                | precoding      |                |                |
|                | supported      |                |                |
+----------------+----------------+----------------+----------------+
|                | PUSCH and DMRS | 7.7.24         | O-RU REQ       |
|                | mux supported  |                |                |
+----------------+----------------+----------------+----------------+
|                | DMRS           | 7.7.24,        | REQ: Type 1    |
|                | configuration  | 7.7.24.14      | (dType=0)      |
|                | Type (dType)   |                |                |
+----------------+----------------+----------------+----------------+
|                | dmrsSymbolMask | 7.7.24         | REQ: 1+1       |
|                |                |                | (symbol        |
|                |                |                | location: 2,   |
|                |                |                | 11)            |
+----------------+----------------+----------------+----------------+
|                | different-t    | 7.7.24         | NOT REQ        |
|                | ransform-preco |                |                |
|                | ding-in-user-g |                |                |
|                | roup-supported |                |                |
+----------------+----------------+----------------+----------------+
|                | differen       | 7.7.24         | NOT REQ        |
|                | t-cdm-without- |                |                |
|                | data-in-user-g |                |                |
|                | roup-supported |                |                |
+----------------+----------------+----------------+----------------+
| Measurements   | SINR reporting | 7.2.11, 7.4.11 | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | MEAS-UE-TAE    | 9.2.1          | O-RU REQ       |
|                | (UE timing     |                |                |
|                | advance error) |                |                |
+----------------+----------------+----------------+----------------+
|                | MEAS-          | 9.2.1          | O-RU REQ       |
|                | UE-LAYER-POWER |                |                |
+----------------+----------------+----------------+----------------+
|                | MEAS-          | 9.2.1          | O-RU REQ       |
|                | UE-FREQ-OFFSET |                |                |
+----------------+----------------+----------------+----------------+
|                | MEAS-IPN-ALLOC | 9.2.1          | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | ME             | 9.2.1          | O-RU REQ       |
|                | AS-IPN-UNALLOC |                |                |
+----------------+----------------+----------------+----------------+
|                | MEA            | 9.2.1          | NOT REQ        |
|                | S-ANT-DMRS-SNR |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | REQ            |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | NOT REQ        |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | N/A            |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2,\       | REQ: LLS-C1 or |
|                | configuration  | 11.2.3 (for    | LLS-C3         |
|                |                | PLFS)          |                |
+----------------+----------------+----------------+----------------+

Table A.3.1.10-2 lists "to be reported" and "to be validated"
capabilities in radio layer 3 C-plane establishment and initial radio
U-plane data transfer test. Table A.3.1.10-3 lists "to be reported" and
"to be validated" capabilities in U-plane DL data transfer test. Table
A.3.1.10-4 lists "to be reported" and "to be validated" capabilities in
U-plane UL data transfer test.

Table A.3.1.10-2: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 7 in radio layer 3 C-Plane establishment and initial
radio U-Plane data transfer test

  PTCs   
  ------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: WDBF for DL, DMRS-BF-EQ for PUSCH, modulation compression
         Capabilities to be reported: PDBF for DL, BFW Fixed point 12 bits, SE4, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Non-delay managed U-plane for SRS transfer
  PTC2   Capabilities to be validated: WDBF for DL, DMRS-BF-EQ for PUSCH, modulation compression
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, SE4, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Non-delay managed U-plane for SRS transfer
  PTC3   Capabilities to be validated: WDBF for DL, DMRS-BF-EQ for PUSCH, modulation compression
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, SE4, SE5, SE6, SE12, SE11, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Non-delay managed U-plane for SRS transfer
  PTC4   Capabilities to be validated: WDBF for DL, DMRS-BF-EQ for PUSCH, modulation compression
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, SE4, SE6, SE12, SE11, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), M-Plane static window control for SRS transfer
  PTC5   Capabilities to be validated: WDBF for DL, DMRS-BF-EQ for PUSCH, modulation compression
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, SE4, SE6,.SE12, SE11, SE27, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), M-Plane static window control for SRS transfer
  PTC6   Capabilities to be validated: WDBF for DL, DMRS-BF-EQ for PUSCH, modulation compression
         Capabilities to be reported: PDBF for DL, BFW Beamspace II + BFP 8 bits, SE4, SE5, SE6, SE12, SE11, SE23, Selective RE sending, User group self assembly, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), M-Plane static window control for SRS transfer

Table A.3.1.10-3: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 7 in U-Plane DL data transfer test

  PTCs   
  ------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, PUSCH-BF-EQ for PUSCH, Non-delay managed U-plane for SRS transfer, BFW Fixed point 12 bits, SE4, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits)
  PTC2   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, PUSCH-BF-EQ for PUSCH, Non-delay managed U-plane for SRS transfer, BFW BFP 8 bits, SE4, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits)
  PTC3   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, PUSCH-BF-EQ for PUSCH, Non-delay managed U-plane for SRS transfer, BFW BFP 8 bits, SE4, SE5, SE6, SE12, SE11, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits)
  PTC4   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, PUSCH-BF-EQ for PUSCH, M-Plane static window control for SRS transfer, BFW BFP 8 bits, SE4, SE6, SE12, SE11, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits)
  PTC5   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, PUSCH-BF-EQ for PUSCH, M-Plane static window control for SRS transfer, BFW BFP 8 bits, SE4, SE6, SE12, SE11, SE27, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits)
  PTC6   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, PUSCH-BF-EQ for PUSCH, M-Plane static window control for SRS transfer, BFW Beamspace II + BFP 8 bits, SE4, SE5, SE6, SE12, SE11, SE23, Selective RE sending, User group self assembly, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits)

Table A.3.1.10-4: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 7 in U-Plane data UL transfer test

  PTCs   
  ------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: DMRS-BF-EQ for PUSCH, modulation compression
         Capabilities to be reported: WDBF or PDBF for DL, BFW Fixed point 12 bits, SE4, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Non-delay managed U-plane for SRS transfer
  PTC2   Capabilities to be validated: DMRS-BF-EQ for PUSCH, modulation compression
         Capabilities to be reported: WDBF or PDBF for DL, BFW BFP 8 bits, SE4, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Non-delay managed U-plane for SRS transfer
  PTC3   Capabilities to be validated: DMRS-BF-EQ for PUSCH, modulation compression
         Capabilities to be reported: WDBF or PDBF for DL, BFW BFP 8 bits, SE4, SE5, SE6, SE12, SE11, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Non-delay managed U-plane for SRS transfer
  PTC4   Capabilities to be validated: DMRS-BF-EQ for PUSCH, modulation compression
         Capabilities to be reported: WDBF or PDBF for DL, BFW BFP 8 bits, SE4, SE6, SE12, SE11, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), M-Plane static window control for SRS transfer
  PTC5   Capabilities to be validated: DMRS-BF-EQ for PUSCH, modulation compression
         Capabilities to be reported: WDBF or PDBF for DL, BFW BFP 8 bits, SE4, SE6, SE12, SE11, SE27, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), M-Plane static window control for SRS transfer
  PTC6   Capabilities to be validated: DMRS-BF-EQ for PUSCH, modulation compression
         Capabilities to be reported: WDBF or PDBF for DL, BFW Beamspace II + BFP 8 bits, SE4, SE5, SE6, SE12, SE11, SE23, Selective RE sending, User group self assembly, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), M-Plane static window control for SRS transfer

#### A.3.1.11 NR TDD IOT M-MIMO Profile 8 - NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-NEQ-Enhanced

Table A.3.1.11-1 describes the base profile. The following PTCs are
defined.

1\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-NEQ-Enh_PTC1\_\[12bitFP.BFW-nondelay.SRS-SE4.ModComp-noSE5-noSE6-noSE11-noSE12-noSE23-noSE27-noSelRE-noSA\]

2\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-NEQ-Enh_PTC2\_\[8bitBFP.BFW-nondelay.SRS-SE4.ModComp-noSE5-noSE6-noSE11-noSE12-noSE23-noSE27-noSelRE-noSA\]

3\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-NEQ-Enh_PTC3\_\[8bitBFP.BFW-nondelay.SRS-SE4.SE5.ModComp-SE6-SE11-SE12\--noSE23-noSE27-noSelRE-noSA\]

4\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-NEQ-Enh_PTC4\_\[8bitBFP.BFW-MplaneTxWindow.SRS-SE4.ModComp-noSE5-SE6-SE11-SE12-noSE23-noSE27-noSelRE-noSA\]

5\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-NEQ-Enh_PTC5\_\[8bitBFP.BFW-MplaneTxWindow.SRS-SE4.ModComp-noSE5-SE6-SE11-SE12-noSE23-SE27-noSelRE-noSA\]

6\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-NEQ-Enh_PTC6\_\[8bitBeamSpaceII.8bitBFP.BFW-MplaneTxWindow.SRS-SE4.SE5.ModComp-SE6-SE11-SE12-SE23-noSE27-SelRE-SAID\]

Table A.3.1.11-1: NR TDD IOT M-MIMO Profile 8:
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-NEQ-Enhanced

+----------------+----------------+----------------+----------------+
| Category       | Item           | Related O-RAN  |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)     |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR TDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | DDDSUUDDDD     |
|                | configuration  |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    |                | 4096           |
|                | size           |                |                |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | 100MHz x 1 CC  |
|                | bandwidth      |                |                |
+----------------+----------------+----------------+----------------+
|                | Number of user | \-             | DL: 2 -- 16    |
|                | layers         |                |                |
|                |                |                | UL: 2 -- 8     |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 25Gbps x 1     |
|                | Ethernet link  |                | lane           |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | O-RU REQ: F0   |
|                | format         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-RU category  | 4.2.1          | Category B     |
+----------------+----------------+----------------+----------------+
|                | LAA            | 7.2.5          | N/A            |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4          | Defined        |
| management,    | determination  |                | Transport      |
| general        |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 4.4.4.3        | NOT REQ        |
|                | adaptation of  |                |                |
|                | delay profile  |                |                |
|                | information    |                |                |
|                | (based on      |                |                |
|                | lls-CU delay   |                |                |
|                | profile and    |                |                |
|                | transport      |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | REQ: Fixed     |
|                | advance type   | Annex B        | timing Advance |
+----------------+----------------+----------------+----------------+
|                | SRS transfer   | 4.4.7, 4.6.4   | PTC4, PTC5,    |
|                |                |                | PTC6: M-Plane  |
|                |                |                | static window  |
|                |                |                | control        |
|                |                |                | (STATIC-       |
|                |                |                | TRANSMISSION-W |
|                |                |                | INDOW-CONTROL) |
|                |                |                | REQ            |
|                |                |                |                |
|                |                |                | PTC1, PTC2,    |
|                |                |                | PTC3:          |
|                |                |                | Non-delay      |
|                |                |                | managed        |
|                |                |                | U-Plane REQ    |
+----------------+----------------+----------------+----------------+
| Delay          | Delay Sets for |                | REQ: Table     |
| management,    | timing         |                | A.4.1-1        |
| default        | parameters     |                |                |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
| Delay          | non-default    | 12.6.3         | REQ:           |
| management,    | beamforming    |                | DMRS-BF-NEQ    |
| non default    | methods \#1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Delay Sets for |                | REQ: Table     |
|                | timing         |                | A.4.3-1        |
|                | parameters     |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | REQ: eCPRI     |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5.1.3.2        | NOT REQ        |
|                | concatenation  |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 3    |
|                | DU_Port_ID     |                | and 2          |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 2    |
|                | BandSector_ID  |                | and 3          |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | O-RU REQ: 3    |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 8    |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
|                |                |                | REQ            |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | Priority REQ   |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | NOT REQ        |
|                | prioritization |                |                |
|                | within U-Plane |                |                |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID REQ    |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | NOT REQ        |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0 dB           |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
|                | (not           |                |                |
|                | applicable to  |                |                |
|                | DMRS-BF-EQ)    |                |                |
+----------------+----------------+----------------+----------------+
|                | equalizatio    | 12.6.3.5       | N/A            |
|                | n-data-scaling |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | O-RU           | 4.2.1          | REQ: Digital   |
|                | beamforming    |                | beamforming    |
|                | type           |                |                |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.2.1, 12.6,   | DL: REQ: WDBF  |
|                | control method | Annex J        | and PDBF       |
|                |                |                |                |
|                |                |                | UL: REQ:       |
|                |                |                | DMRS-BF for    |
|                |                |                | PUSCH, WDBF or |
|                |                |                | PDBF for       |
|                |                |                | non-PUSCH      |
+----------------+----------------+----------------+----------------+
|                | BFW IQ         | 7.7.1, Annex J | REQ            |
|                |                |                |                |
|                |                |                | PTC1: Fixed    |
|                |                |                | point, 12 bits |
|                |                |                |                |
|                |                |                | PTC2, PTC3,    |
|                |                |                | PTC4, PTC5:    |
|                |                |                | BFP, 8 bits    |
|                |                |                |                |
|                |                |                | O-RU REQ       |
|                |                |                |                |
|                |                |                | PTC6:          |
|                |                |                | Beamspace      |
|                |                |                | compression    |
|                |                |                | Type II (8     |
|                |                |                | bits) and BFP  |
|                |                |                | (8 bits)       |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | DL: O-RU REQ   |
|                | compression    |                |                |
|                | method         |                | PTC1, PTC2,    |
|                |                |                | PTC3, PTC4,    |
|                |                |                | PTC5: Mod      |
|                |                |                | Comp, no sel   |
|                |                |                | RE             |
|                |                |                |                |
|                |                |                | PTC6: Mod      |
|                |                |                | Comp, with sel |
|                |                |                | RE.            |
|                |                |                |                |
|                |                |                | UL: REQ BFP    |
+----------------+----------------+----------------+----------------+
|                | U-Plane        | 8, Annex D     | DL: REQ: Mod   |
|                | (DL/UL) data   |                | Comp with 4    |
|                | IQ bitwidth    |                | bits           |
|                |                |                |                |
|                |                |                | UL: REQ: BFP   |
|                |                |                | with 9 bits    |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | REQ            |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | REQ (for PRACH |
|                |                |                | )              |
+----------------+----------------+----------------+----------------+
|                | Section Type 4 | 7.4.6          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | REQ (for       |
|                |                |                | DMRS-BF)       |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | N/A            |
+----------------+----------------+----------------+----------------+
|                | Section Type 8 | 7.4.10         | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 9 | 7.4.11         | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type   | 7.4.12         | NOT REQ        |
|                | 10             |                |                |
+----------------+----------------+----------------+----------------+
|                | Section Type   | 7.4.13         | NOT REQ        |
|                | 11             |                |                |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | NOT REQ        |
|                | flag           |                |                |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | REQ: Single    |
|                | PRACH formats  |                | C-Plane        |
|                | with preamble  |                | message        |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | REQ            |
|                | extension 1    |                |                |
|                | (beamforming   |                |                |
|                | weights)       |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | NOT REQ        |
|                | extension 2    |                |                |
|                | (beamforming   |                |                |
|                | attributes)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | NOT REQ        |
|                | extension 3    |                |                |
|                | (DL Precoding  |                |                |
|                | configuration  |                |                |
|                | parameters and |                |                |
|                | indications)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | O-RU REQ       |
|                | extension 4    |                |                |
|                | (modulation    |                |                |
|                | compr. params) |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | PTC1, PTC2,    |
|                | extension 5    |                | PTC4, PTC5:    |
|                | (modulation    |                | NOT REQ        |
|                | compression    |                |                |
|                | additional     |                | PTC3, PTC6:    |
|                | scaling        |                | O-RU REQ       |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.6          | PTC1, PTC2:    |
|                | extension 6    |                | NOT REQ        |
|                | (              |                |                |
|                | Non-contiguous |                | PTC3, PTC4,    |
|                | PRB            |                | PTC5, PTC6:    |
|                | allocation)    |                | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.7          | NOT REQ        |
|                | extension 7    |                |                |
|                | (Multiple-eAxC |                |                |
|                | designation)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.8          | NOT REQ        |
|                | extension 8    |                |                |
|                | (              |                |                |
|                | regularization |                |                |
|                | factor)        |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.9          | NOT REQ        |
|                | extension 9    |                |                |
|                | (Dynamic       |                |                |
|                | Spectrum       |                |                |
|                | Sharing        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.10         | REQ (for       |
|                | extension 10   |                | DMRS-BF)       |
|                | (Multiple      |                |                |
|                | ports          |                |                |
|                | grouping)      |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.11         | PTC1, PTC2:    |
|                | extension 11   |                | NOT REQ        |
|                | (Flexible BF   |                |                |
|                | weights)       |                | PTC3, PTC4,    |
|                |                |                | PTC5, PTC6:    |
|                |                |                | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.12         | PTC1, PTC2:    |
|                | extension 12   |                | NOT REQ        |
|                |                |                |                |
|                |                |                | PTC3, PTC4,    |
|                |                |                | PTC5, PTC6:    |
|                |                |                | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.13         | NOT REQ        |
|                | extension 13   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.14         | NOT REQ        |
|                | extension 14   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.15         | NOT REQ        |
|                | extension 15   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.16         | NOT REQ        |
|                | extension 16   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.17         | NOT REQ        |
|                | extension 17   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.18         | NOT REQ        |
|                | extension 18   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.19         | NOT REQ        |
|                | extension 19   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.20         | NOT REQ        |
|                | extension 20   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.21         | NOT REQ        |
|                | extension 21   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.22         | NOT REQ        |
|                | extension 22   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.23         | PTC1, PTC2,    |
|                | extension 23   |                | PTC3, PTC4,    |
|                |                |                | PTC5: NOT REQ  |
|                |                |                |                |
|                |                |                | PTC6: O-RU REQ |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.24         | REQ            |
|                | extension 24   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.25         | NOT REQ        |
|                | extension 25   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.26         | O-RU REQ       |
|                | extension 26   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.27         | PTC1, PTC2,    |
|                | extension 27   |                | PTC3, PTC4,    |
|                |                |                | PTC6: NOT REQ  |
|                |                |                |                |
|                |                |                | PTC5: REQ      |
+----------------+----------------+----------------+----------------+
| DMRS-BF        | Port reduced   | 12.6.3.1       | REQ            |
|                | DMRS data      |                |                |
|                | sending        |                |                |
+----------------+----------------+----------------+----------------+
|                | User group     | 7.7.24         | PTC1, PTC2,    |
|                | self assembly  |                | PTC3, PTC4,    |
|                |                |                | PTC5: NOT REQ  |
|                |                |                | (no            |
|                |                |                | self-assembly  |
|                |                |                | = noSA)        |
|                |                |                |                |
|                |                |                | PTC6: O-RU     |
|                |                |                | REQ: SAID      |
|                |                |                | (self assembly |
|                |                |                | with id)       |
+----------------+----------------+----------------+----------------+
|                | Per-window     | 7.7.25,        | NOT REQ        |
|                | symbol         | 12.6.1.5       |                |
|                | reordering     |                |                |
|                | with DMRS      |                |                |
|                | sending        |                |                |
+----------------+----------------+----------------+----------------+
|                | Per section    | 7.7.25,        | NOT REQ        |
|                | tx-window      | 12.6.1.5       |                |
|                | reassignment   |                |                |
+----------------+----------------+----------------+----------------+
|                | symbolid       | 7.7.25         | N/A            |
|                | meaining when  |                |                |
|                | reordering     |                |                |
|                | (up-symbolId-  |                |                |
|                | type-supporte) |                |                |
+----------------+----------------+----------------+----------------+
|                | Transform      | 7.7.24         | O-RU REQ       |
|                | precoding      |                |                |
|                | supported      |                |                |
+----------------+----------------+----------------+----------------+
|                | PUSCH and DMRS | 7.7.24         | O-RU REQ       |
|                | mux supported  |                |                |
+----------------+----------------+----------------+----------------+
|                | DMRS           | 7.7.24,        | REQ: Type 1    |
|                | configuration  | 7.7.24.14      | (dType=0)      |
|                | Type (dType)   |                |                |
+----------------+----------------+----------------+----------------+
|                | dmrsSymbolMask | 7.7.24         | REQ: 1+1       |
|                |                |                | (symbol        |
|                |                |                | location: 2,   |
|                |                |                | 11)            |
+----------------+----------------+----------------+----------------+
|                | different-t    | 7.7.24         | NOT REQ        |
|                | ransform-preco |                |                |
|                | ding-in-user-g |                |                |
|                | roup-supported |                |                |
+----------------+----------------+----------------+----------------+
|                | differen       | 7.7.24         | NOT REQ        |
|                | t-cdm-without- |                |                |
|                | data-in-user-g |                |                |
|                | roup-supported |                |                |
+----------------+----------------+----------------+----------------+
| Measurements   | SINR reporting | 7.2.11, 7.4.11 | N/A            |
+----------------+----------------+----------------+----------------+
|                | MEAS-UE-TAE    | 9.2.1          | NOT REQ.       |
|                | (UE timing     |                |                |
|                | advance error) |                | O-RU declares  |
|                |                |                | feature        |
|                |                |                | DMRS-BF-NEQ-   |
|                |                |                | UNALTERED-TAE. |
+----------------+----------------+----------------+----------------+
|                | MEAS-          | 9.2.1          | NOT REQ        |
|                | UE-LAYER-POWER |                |                |
+----------------+----------------+----------------+----------------+
|                | MEAS-          | 9.2.1          | NOT REQ.       |
|                | UE-FREQ-OFFSET |                |                |
|                |                |                | O-RU declares  |
|                |                |                | feature        |
|                |                |                | DMRS-B         |
|                |                |                | F-NEQ-UNALTERE |
|                |                |                | D-FREQ-OFFSET. |
+----------------+----------------+----------------+----------------+
|                | MEAS-IPN-ALLOC | 9.2.1          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | ME             | 9.2.1          | NOT REQ        |
|                | AS-IPN-UNALLOC |                |                |
+----------------+----------------+----------------+----------------+
|                | MEA            | 9.2.1          | NOT REQ        |
|                | S-ANT-DMRS-SNR |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | REQ            |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | NOT REQ        |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | N/A            |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2,\       | REQ: LLS-C1 or |
|                | configuration  | 11.2.3 (for    | LLS-C3         |
|                |                | PLFS)          |                |
+----------------+----------------+----------------+----------------+

Table A.3.1.11-2 lists "to be reported" and "to be validated"
capabilities in radio layer 3 C-plane establishment and initial radio
U-plane data transfer test. Table A.3.1.11-3 lists "to be reported" and
"to be validated" capabilities in U-plane DL data transfer test. Table
A.3.1.11-4 lists "to be reported" and "to be validated" capabilities in
U-plane UL data transfer test.

Table A.3.1.11-2: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 8 in radio layer 3 C-Plane establishment and initial
radio U-Plane data transfer test

  PTCs   
  ------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: WDBF for DL, DMRS-BF-NEQ for PUSCH, modulation compression
         Capabilities to be reported: PDBF for DL, BFW Fixed point 12 bits, SE4, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer
  PTC2   Capabilities to be validated: WDBF for DL, DMRS-BF-NEQ for PUSCH, modulation compression
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, SE4, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer
  PTC3   Capabilities to be validated: WDBF for DL, DMRS-BF-NEQ for PUSCH, modulation compression
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, SE4, SE5, SE6, SE12, SE11, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer
  PTC4   Capabilities to be validated: WDBF for DL, DMRS-BF-NEQ for PUSCH, modulation compression
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, SE4, SE6, SE12, SE11, eAxC-ID format (3238 or 2338), M-Plane static window control for SRS transfer
  PTC5   Capabilities to be validated: WDBF for DL, DMRS-BF-NEQ for PUSCH, modulation compression
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, SE4, SE6, SE12, SE11, SE27, eAxC-ID format (3238 or 2338), M-Plane static window control for SRS transfer
  PTC6   Capabilities to be validated: WDBF for DL, DMRS-BF-NEQ for PUSCH, modulation compression
         Capabilities to be reported: PDBF for DL, BFW Beamspace II + BFP 8 bits, SE4, SE5, SE6, SE12, SE11, SE23, Selective RE sending, User group self assembly, eAxC-ID format (3238 or 2338), M-Plane static window control for SRS transfer

Table A.3.1.11-3: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 8 in U-Plane DL data transfer test

  PTCs   
  ------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, DMRS-BF-NEQ for PUSCH, Non-delay managed U-plane for SRS transfer, BFW Fixed point 12 bits, SE4, eAxC-ID format (3238 or 2338)
  PTC2   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, DMRS-BF-NEQ for PUSCH, Non-delay managed U-plane for SRS transfer, BFW BFP 8 bits, SE4, eAxC-ID format (3238 or 2338)
  PTC3   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, DMRS-BF-NEQ for PUSCH, Non-delay managed U-plane for SRS transfer, BFW BFP 8 bits, SE4, SE5, SE6, SE12, SE11, eAxC-ID format (3238 or 2338)
  PTC4   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, DMRS-BF-NEQ for PUSCH, M-Plane static window control for SRS transfer, BFW BFP 8 bits, SE4, SE6, SE12, SE11, eAxC-ID format (3238 or 2338)
  PTC5   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, DMRS-BF-NEQ for PUSCH, M-Plane static window control for SRS transfer, BFW BFP 8 bits, SE4, SE6, SE12, SE11, SE27, eAxC-ID format (3238 or 2338)
  PTC6   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, DMRS-BF-NEQ for PUSCH, M-Plane static window control for SRS transfer, BFW Beamspace II + BFP 8 bits, SE4, SE5, SE6, SE12, SE11, SE23, Selective RE sending, User group self assembly, eAxC-ID format (3238 or 2338)

Table A.3.1.11-4: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 8 in U-Plane data UL transfer test

  PTCs   
  ------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: DMRS-BF-NEQ for PUSCH, modulation compression
         Capabilities to be reported: WDBF or PDBF for DL, BFW Fixed point 12 bits, SE4, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer
  PTC2   Capabilities to be validated: DMRS-BF-NEQ for PUSCH, modulation compression
         Capabilities to be reported: WDBF or PDBF for DL, BFW BFP 8 bits, SE4, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer
  PTC3   Capabilities to be validated: DMRS-BF-NEQ for PUSCH, modulation compression
         Capabilities to be reported: WDBF or PDBF for DL, BFW BFP 8 bits, SE4, SE5, SE6, SE12, SE11, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer
  PTC4   Capabilities to be validated: DMRS-BF-NEQ for PUSCH, modulation compression
         Capabilities to be reported: WDBF or PDBF for DL, BFW BFP 8 bits, SE4, SE6, SE12, SE11, eAxC-ID format (3238 or 2338), M-Plane static window control for SRS transfer
  PTC5   Capabilities to be validated: DMRS-BF-NEQ for PUSCH, modulation compression
         Capabilities to be reported: WDBF or PDBF for DL, BFW BFP 8 bits, SE4, SE6, SE12, SE11, SE27, eAxC-ID format (3238 or 2338), M-Plane static window control for SRS transfer
  PTC6   Capabilities to be validated: DMRS-BF-NEQ for PUSCH, modulation compression
         Capabilities to be reported: WDBF or PDBF for DL, BFW Beamspace II + BFP 8 bits, SE4, SE5, SE6, SE12, SE11, SE23, Selective RE sending, User group self assembly, eAxC-ID format (3238 or 2338), M-Plane static window control for SRS transfer

#### A.3.1.12 NR TDD IOT M-MIMO Profile 9 - NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Reordering

Table A.3.1.12-1 shows the base profile. It is expected that re-ordering
feature is used when using reordering PTCs for IOT testing. The
following PTCs are defined.

1\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Reordering_PTC1\_\[8bitBFP.BFW-nondelay.SRS-PerWindows.reord-onair.upsymbolId-SE4.ModComp-noSE5-noJumbo\]

2\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Reordering_PTC2\_\[8bitBFP.BFW-nondelay.SRS-PerWindow.reord-txwindow.upsymbolId-SE4.SE5.ModComp-noJumbo\]

3\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Reordering_PTC3\_\[8bitBFP.BFW-MplaneTxWindow.SRS-PerWindows.reord-txwindow.upsymbolId-noModComp-noJumbo\]

4\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Reordering_PTC4\_\[12bitFP.BFW-nondelay.SRS-PerSection.reord-onair.upsymbolId-SE4.ModComp-noSE5-Jumbo\]

5\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Reordering_PTC5\_\[8bitBFP.BFW-MplaneTxWindow.SRS-PerSection.reord-onair.upsymbolId-SE4.ModComp-noSE5-Jumbo\]

Table A.3.1.12-1: NR TDD IOT M-MIMO Profile 9:
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-EQ-Reordering

+----------------+----------------+----------------+----------------+
| Category       | Item           | Related O-RAN  |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)     |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR TDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | DDDSUUDDDD     |
|                | configuration  |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    |                | 4096           |
|                | size           |                |                |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | 100MHz x 1 CC  |
|                | bandwidth      |                |                |
+----------------+----------------+----------------+----------------+
|                | Number of user | \-             | DL: 2 -- 16    |
|                | layers         |                |                |
|                |                |                | UL: 2 -- 8     |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 25Gbps x 1     |
|                | Ethernet link  |                | lane           |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | O-RU REQ: F0   |
|                | format         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-RU category  | 4.2.1          | Category B     |
+----------------+----------------+----------------+----------------+
|                | LAA            | 7.2.5          | N/A            |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4          | Defined        |
| management,    | determination  |                | Transport      |
| general        |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 4.4.4.3        | NOT REQ        |
|                | adaptation of  |                |                |
|                | delay profile  |                |                |
|                | information    |                |                |
|                | (based on      |                |                |
|                | lls-CU delay   |                |                |
|                | profile and    |                |                |
|                | transport      |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | REQ: Fixed     |
|                | advance type   | Annex B        | timing Advance |
+----------------+----------------+----------------+----------------+
|                | SRS transfer   | 4.4.7, 4.6.4   | PTC3, PTC5:    |
|                |                |                | M-Plane static |
|                |                |                | window control |
|                |                |                | (STATIC-       |
|                |                |                | TRANSMISSION-W |
|                |                |                | INDOW-CONTROL) |
|                |                |                | REQ            |
|                |                |                |                |
|                |                |                | PTC1, PTC2,    |
|                |                |                | PTC4:          |
|                |                |                | Non-delay      |
|                |                |                | managed        |
|                |                |                | U-Plane REQ    |
+----------------+----------------+----------------+----------------+
| Delay          | Delay Sets for |                | REQ: Table     |
| management,    | timing         |                | A.4.1-1        |
| default        | parameters     |                |                |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
| Delay          | non-default    | 12.6.3         | REQ:           |
| management,    | beamforming    |                | DMRS-BF-EQ     |
| non default    | methods \#1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Delay Sets for |                | REQ: Table     |
|                | timing         |                | A.4.3-1        |
|                | parameters     |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | PTC4, PTC5:    |
|                |                |                | O-RU REQ       |
|                |                |                |                |
|                |                |                | PTC1, PTC2,    |
|                |                |                | PTC3: NOT REQ  |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | REQ: eCPRI     |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5.1.3.2        | NOT REQ        |
|                | concatenation  |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 3    |
|                | DU_Port_ID     |                | and 2          |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 2    |
|                | BandSector_ID  |                | and 3          |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | O-RU REQ: 3    |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 8    |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
|                |                |                | REQ            |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | Priority REQ   |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | NOT REQ        |
|                | prioritization |                |                |
|                | within U-Plane |                |                |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID REQ    |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | NOT REQ        |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0 dB           |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
|                | (not           |                |                |
|                | applicable to  |                |                |
|                | DMRS-BF-EQ)    |                |                |
+----------------+----------------+----------------+----------------+
|                | equalizatio    | 12.6.3.5       | REQ:           |
|                | n-data-scaling |                | Sca            |
|                |                |                | ling-function1 |
|                |                |                | or             |
|                |                |                | Sca            |
|                |                |                | ling-function2 |
+----------------+----------------+----------------+----------------+
| Beamforming    | O-RU           | 4.2.1          | REQ: Digital   |
|                | beamforming    |                | beamforming    |
|                | type           |                |                |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.2.1, 12.6,   | DL: REQ: WDBF  |
|                | control method | Annex J        | and PDBF       |
|                |                |                |                |
|                |                |                | UL: REQ:       |
|                |                |                | DMRS-BF for    |
|                |                |                | PUSCH, WDBF or |
|                |                |                | PDBF for       |
|                |                |                | non-PUSCH      |
+----------------+----------------+----------------+----------------+
|                | BFW IQ         | 7.7.1, Annex J | REQ:           |
|                |                |                |                |
|                |                |                | PTC4: Fixed    |
|                |                |                | point, 12 bits |
|                |                |                |                |
|                |                |                | PTC1, PTC2,    |
|                |                |                | PTC3, PTC5:    |
|                |                |                | BFP, 8 bits    |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | DL: O-RU REQ   |
|                | compression    |                |                |
|                | method         |                | PTC1, PTC2,    |
|                |                |                | PTC4, PTC5:    |
|                |                |                | Mod Comp, no   |
|                |                |                | sel RE         |
|                |                |                |                |
|                |                |                | PTC3: BFP      |
|                |                |                |                |
|                |                |                | UL: REQ: BFP   |
+----------------+----------------+----------------+----------------+
|                | U-Plane        | 8, Annex D     | DL: O-RU REQ   |
|                | (DL/UL) data   |                |                |
|                | IQ bitwidth    |                | PTC1, PTC2,    |
|                |                |                | PTC4, PTC5: 4  |
|                |                |                | bits (Mod      |
|                |                |                | Comp)          |
|                |                |                |                |
|                |                |                | PTC3: 9 bits,  |
|                |                |                | BFP            |
|                |                |                |                |
|                |                |                | UL: REQ: 9     |
|                |                |                | bits           |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | REQ            |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | REQ (for PRACH |
|                |                |                | )              |
+----------------+----------------+----------------+----------------+
|                | Section Type 4 | 7.4.6          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | REQ (for       |
|                |                |                | DMRS-BF)       |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | N/A            |
+----------------+----------------+----------------+----------------+
|                | Section Type 8 | 7.4.10         | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 9 | 7.4.11         | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section Type   | 7.4.12         | REQ            |
|                | 10             |                |                |
+----------------+----------------+----------------+----------------+
|                | Section Type   | 7.4.13         | O-RU REQ       |
|                | 11             |                |                |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | NOT REQ        |
|                | flag           |                |                |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | REQ: Single    |
|                | PRACH formats  |                | C-Plane        |
|                | with preamble  |                | message        |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | REQ            |
|                | extension 1    |                |                |
|                | (beamforming   |                |                |
|                | weights)       |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | NOT REQ        |
|                | extension 2    |                |                |
|                | (beamforming   |                |                |
|                | attributes)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | NOT REQ        |
|                | extension 3    |                |                |
|                | (DL Precoding  |                |                |
|                | configuration  |                |                |
|                | parameters and |                |                |
|                | indications)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | PTC3: NOT REQ  |
|                | extension 4    |                |                |
|                | (modulation    |                | PTC1, PTC2,    |
|                | compr. params) |                | PTC4, PTC5:    |
|                |                |                | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | PTC1, PTC3,    |
|                | extension 5    |                | PTC4, PTC5:    |
|                | (modulation    |                | NOT REQ        |
|                | compression    |                |                |
|                | additional     |                | PTC2: O-RU REQ |
|                | scaling        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.6          | NOT REQ        |
|                | extension 6    |                |                |
|                | (              |                |                |
|                | Non-contiguous |                |                |
|                | PRB            |                |                |
|                | allocation)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.7          | NOT REQ        |
|                | extension 7    |                |                |
|                | (Multiple-eAxC |                |                |
|                | designation)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.8          | NOT REQ        |
|                | extension 8    |                |                |
|                | (              |                |                |
|                | regularization |                |                |
|                | factor)        |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.9          | NOT REQ        |
|                | extension 9    |                |                |
|                | (Dynamic       |                |                |
|                | Spectrum       |                |                |
|                | Sharing        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.10         | REQ (for       |
|                | extension 10   |                | DMRS-BF)       |
|                | (Multiple      |                |                |
|                | ports          |                |                |
|                | grouping)      |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.11         | O-RU REQ       |
|                | extension 11   |                |                |
|                | (Flexible BF   |                |                |
|                | weights)       |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.12         | NOT REQ        |
|                | extension 12   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.13         | NOT REQ        |
|                | extension 13   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.14         | NOT REQ        |
|                | extension 14   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.15         | NOT REQ        |
|                | extension 15   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.16         | NOT REQ        |
|                | extension 16   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.17         | NOT REQ        |
|                | extension 17   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.18         | NOT REQ        |
|                | extension 18   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.19         | NOT REQ        |
|                | extension 19   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.20         | NOT REQ        |
|                | extension 20   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.21         | NOT REQ        |
|                | extension 21   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.22         | NOT REQ        |
|                | extension 22   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.23         | NOT REQ        |
|                | extension 23   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.24         | REQ            |
|                | extension 24   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.25         | REQ            |
|                | extension 25   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.26         | O-RU REQ       |
|                | extension 26   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.27         | NOT REQ        |
|                | extension 27   |                |                |
+----------------+----------------+----------------+----------------+
| DMRS-BF        | Port reduced   | 12.6.3.1       | O-RU REQ       |
|                | DMRS data      |                |                |
|                | sending        |                |                |
+----------------+----------------+----------------+----------------+
|                | User group     | 7.7.24         | NOT REQ        |
|                | self assembly  |                |                |
+----------------+----------------+----------------+----------------+
|                | Per-window     | 7.7.25,        | PTC4, PTC5:    |
|                | symbol         | 12.6.1.5       | NOT REQ        |
|                | reordering     |                |                |
|                |                |                | PTC1, PTC2,    |
|                |                |                | PTC3: REQ      |
|                |                |                |                |
|                |                |                | If             |
|                |                |                | \"per-window   |
|                |                |                | symbol         |
|                |                |                | reordering\"   |
|                |                |                | is used, then  |
|                |                |                | \"per-section  |
|                |                |                | tx-window      |
|                |                |                | reassignment\" |
|                |                |                | is not used.   |
+----------------+----------------+----------------+----------------+
|                | Per section    | 7.7.25,        | PTC1, PTC2,    |
|                | tx-window      | 12.6.1.5       | PTC3: NOT REQ  |
|                | reassignment   |                |                |
|                |                |                | PTC4, PTC5:    |
|                |                |                | REQ            |
|                |                |                |                |
|                |                |                | If             |
|                |                |                | \"per-section  |
|                |                |                | tx-window      |
|                |                |                | reassignment\" |
|                |                |                | is used, then  |
|                |                |                | \"per-window   |
|                |                |                | symbol         |
|                |                |                | reordering\"   |
|                |                |                | is not used.   |
+----------------+----------------+----------------+----------------+
|                | symbolid       | 7.7.25         | REQ            |
|                | meaining when  |                |                |
|                | reordering     |                | PTC2, PTC3:    |
|                | (up-symbolId-t |                | Transmission   |
|                | ype-supported) |                | window number  |
|                |                |                |                |
|                |                |                | PTC1, PTC4,    |
|                |                |                | PTC5: on-air   |
|                |                |                | symbol number  |
+----------------+----------------+----------------+----------------+
|                | Transform      | 7.7.24         | O-RU REQ       |
|                | precoding      |                |                |
|                | supported      |                |                |
+----------------+----------------+----------------+----------------+
|                | PUSCH and DMRS | 7.7.24         | O-RU REQ       |
|                | mux supported  |                |                |
+----------------+----------------+----------------+----------------+
|                | DMRS           | 7.7.24,        | REQ: Type 1    |
|                | configuration  | 7.7.24.14      | (dType=0)      |
|                | Type (dType)   |                |                |
+----------------+----------------+----------------+----------------+
|                | dmrsSymbolMask | 7.7.24         | REQ: 1+1       |
|                |                |                | (symbol        |
|                |                |                | location: 2,   |
|                |                |                | 11)            |
+----------------+----------------+----------------+----------------+
|                | different-t    | 7.7.24         | NOT REQ        |
|                | ransform-preco |                |                |
|                | ding-in-user-g |                |                |
|                | roup-supported |                |                |
+----------------+----------------+----------------+----------------+
|                | differen       | 7.7.24         | NOT REQ        |
|                | t-cdm-without- |                |                |
|                | data-in-user-g |                |                |
|                | roup-supported |                |                |
+----------------+----------------+----------------+----------------+
| Measurements   | SINR reporting | 7.2.11, 7.4.11 | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | MEAS-UE-TAE    | 9.2.1          | O-RU REQ       |
|                | (UE timing     |                |                |
|                | advance error) |                |                |
+----------------+----------------+----------------+----------------+
|                | MEAS-          | 9.2.1          | O-RU REQ       |
|                | UE-LAYER-POWER |                |                |
+----------------+----------------+----------------+----------------+
|                | MEAS-          | 9.2.1          | O-RU REQ       |
|                | UE-FREQ-OFFSET |                |                |
+----------------+----------------+----------------+----------------+
|                | MEAS-IPN-ALLOC | 9.2.1          | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | ME             | 9.2.1          | O-RU REQ       |
|                | AS-IPN-UNALLOC |                |                |
+----------------+----------------+----------------+----------------+
|                | MEA            | 9.2.1          | NOT REQ        |
|                | S-ANT-DMRS-SNR |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | REQ            |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | NOT REQ        |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | N/A            |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2,\       | REQ: LLS-C1 or |
|                | configuration  | 11.2.3 (for    | LLS-C3         |
|                |                | PLFS)          |                |
+----------------+----------------+----------------+----------------+

Table A.3.1.12-2 lists "to be reported" and "to be validated"
capabilities in radio layer 3 C-plane establishment and initial radio
U-plane data transfer test. Table A.3.1.12-3 lists "to be reported" and
"to be validated" capabilities in U-plane DL data transfer test. Table
A.3.1.12-4 lists "to be reported" and "to be validated" capabilities in
U-plane UL data transfer test.

Table A.3.1.12-2: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 9 in radio layer 3 C-Plane establishment and initial
radio U-Plane data transfer test

  PTCs   
  ------ --------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: WDBF for DL, DMRS-BF-EQ for PUSCH, modulation compression, Per-window symbol reordering using on-air symbol number
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, SE4, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer
  PTC2   Capabilities to be validated: WDBF for DL, DMRS-BF-EQ for PUSCH, modulation compression, Per-window symbole reordering using tx-window symbold number
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, SE4, SE5, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer
  PTC3   Capabilities to be validated: WDBF for DL, DMRS-BF-EQ for PUSCH, Per-window symbol reordering using tx-window symbol number
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, eAxC-ID format (3238 or 2338), M-Plane static window control for SRS transfer
  PTC4   Capabilities to be validated: WDBF for DL, DMRS-BF-EQ for PUSCH, modulation compression, Per-section tx-window reassignment using on-air symbol number
         Capabilities to be reported: PDBF for DL, BFW Fixed point 12 bits, SE4, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer
  PTC5   Capabilities to be validated: WDBF for DL, DMRS-BF-EQ for PUSCH, modulation compression, Per-section tx-window reassignment using on-air symbol number
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, SE4, eAxC-ID format (3238 or 2338), M-Plane static window control for SRS transfer

Table A.3.1.12-3: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 7 in U-Plane DL data transfer test

  PTCs   
  ------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, DMRS-BF-EQ for PUSCH, Non-delay managed U-plane for SRS transfer, BFW BFP 8 bits, SE4, eAxC-ID format (3238 or 2338), Per-window symbol reordering using on-air symbol number
  PTC2   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, DMRS-BF-EQ for PUSCH, Non-delay managed U-plane for SRS transfer, BFW BFP 8 bits, SE4, SE5, eAxC-ID format (3238 or 2338), Per-window symbol reordering using tx-window symbold number
  PTC3   Capabilities to be validated: WDBF for DL
         Capabilities to be reported: PDBF for DL, DMRS-BF-EQ for PUSCH, M-Plane static window control for SRS transfer, BFW BFP 8 bits, eAxC-ID format (3238 or 2338), Per-window symbol reordering using tx-window symbol number
  PTC4   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, DMRS-BF-EQ for PUSCH, Non-delay managed U-plane for SRS transfer, BFW Fixed point 12 bits, SE4, eAxC-ID format (3238 or 2338), Per-section tx-window reassignment using on-air symbol number
  PTC5   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, DMRS-BF-EQ for PUSCH, M-Plane static window control for SRS transfer, BFW BFP 8 bits, SE4, eAxC-ID format (3238 or 2338), Per-section tx-window reassignment using on-air symbol number

Table A.3.1.12-4: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 7 in U-Plane data UL transfer test

  PTCs   
  ------ -----------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: DMRS-BF-EQ for PUSCH, modulation compression, Per-window symbol reordering using on-air symbol number
         Capabilities to be reported: WDBF or PDBF for DL, BFW BFP 8 bits, SE4, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer
  PTC2   Capabilities to be validated: DMRS-BF-EQ for PUSCH, modulation compression, Per-window symbol reordering using tx-window symbold number
         Capabilities to be reported: WDBF or PDBF for DL, BFW BFP 8 bits, SE4, SE5, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer
  PTC3   Capabilities to be validated: DMRS-BF-EQ for PUSCH, Per-window symbol reordering using tx-window symbol number
         Capabilities to be reported: WDBF or PDBF for DL, BFW BFP 8 bits, eAxC-ID format (3238 or 2338), M-Plane static window control for SRS transfer
  PTC4   Capabilities to be validated: DMRS-BF-EQ for PUSCH, modulation compression, Per-section tx-window reassignment using on-air symbol number
         Capabilities to be reported: WDBF or PDBF for DL, BFW Fixed point 12 bits, SE4, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer
  PTC5   Capabilities to be validated: DMRS-BF-EQ for PUSCH, modulation compression, Per-section tx-window reassignment using on-air symbol number
         Capabilities to be reported: WDBF or PDBF for DL, BFW BFP 8 bits, SE4, eAxC-ID format (3238 or 2338), M-Plane static window control for SRS transfer

#### A.3.1.13 NR TDD IOT M-MIMO Profile 10 - NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-NEQ-Reordering

Table A.3.1.13-1 describes the base profile. It is expected that
reordering feature is used when using reordering PTCs for IOT testing.
The following PTCs are defined.

1\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-NEQ-Reordering_PTC1\_\[8bitBFP.BFW-nondelay.SRS-PerWindows.reord-txwindow.upsymbolId-SE4.ModComp\]

2\)
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-NEQ-Reordering_PTC2\_\[12bitFP.BFW-MplaneTxWindow.SRS-PerWindows.reord-txwindow.upsymbolId-noModComp\]

Table A.3.1.13-1: NR TDD IOT M-MIMO Profile 10:
NR-TDD-FR1-CAT-B-mMIMO-WDBF-DMRS-BF-NEQ-Reordering

+----------------+----------------+----------------+----------------+
| Category       | Item           | Related O-RAN  |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)     |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR TDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | DDDSUUDDDD     |
|                | configuration  |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    |                | 4096           |
|                | size           |                |                |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | 100MHz x 1 CC  |
|                | bandwidth      |                |                |
+----------------+----------------+----------------+----------------+
|                | Number of user | \-             | DL: 2 -- 16    |
|                | layers         |                |                |
|                |                |                | UL: 2 -- 8     |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 25Gbps x 1     |
|                | Ethernet link  |                | lane           |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | O-RU REQ: F0   |
|                | format         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-RU category  | 4.2.1          | Category B     |
+----------------+----------------+----------------+----------------+
|                | LAA            | 7.2.5          | N/A            |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4          | Defined        |
| management,    | determination  |                | Transport      |
| general        |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 4.4.4.3        | NOT REQ        |
|                | adaptation of  |                |                |
|                | delay profile  |                |                |
|                | information    |                |                |
|                | (based on      |                |                |
|                | lls-CU delay   |                |                |
|                | profile and    |                |                |
|                | transport      |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | REQ: Fixed     |
|                | advance type   | Annex B        | timing Advance |
+----------------+----------------+----------------+----------------+
|                | SRS transfer   | 4.4.7, 4.6.4   | PTC2: M-Plane  |
|                |                |                | static window  |
|                |                |                | control        |
|                |                |                | (STATIC-       |
|                |                |                | TRANSMISSION-W |
|                |                |                | INDOW-CONTROL) |
|                |                |                | REQ            |
|                |                |                |                |
|                |                |                | PTC1:          |
|                |                |                | Non-delay      |
|                |                |                | managed        |
|                |                |                | U-Plane REQ    |
+----------------+----------------+----------------+----------------+
| Delay          | Delay Sets for |                | REQ: Table     |
| management,    | timing         |                | A.4.1-1        |
| default        | parameters     |                |                |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
| Delay          | non-default    | 12.6.3         | REQ:           |
| management,    | beamforming    |                | DMRS-BF-NEQ    |
| non default    | methods \#1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Delay Sets for |                | REQ: Table     |
|                | timing         |                | A.4.3-1        |
|                | parameters     |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | REQ: eCPRI     |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5.1.3.2        | NOT REQ        |
|                | concatenation  |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 3    |
|                | DU_Port_ID     |                | and 2          |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 2    |
|                | BandSector_ID  |                | and 3          |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | O-RU REQ: 3    |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 8    |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
|                |                |                | REQ            |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | Priority REQ   |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | NOT REQ        |
|                | prioritization |                |                |
|                | within U-Plane |                |                |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID REQ    |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | NOT REQ        |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0 dB           |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
|                | (not           |                |                |
|                | applicable to  |                |                |
|                | DMRS-BF-EQ)    |                |                |
+----------------+----------------+----------------+----------------+
|                | equalizatio    | 12.6.3.5       | N/A            |
|                | n-data-scaling |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | O-RU           | 4.2.1          | REQ: Digital   |
|                | beamforming    |                | beamforming    |
|                | type           |                |                |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.2.1, 12.6,   | DL: REQ: WDBF  |
|                | control method | Annex J        | and PDBF       |
|                |                |                |                |
|                |                |                | UL: REQ:       |
|                |                |                | DMRS-BF for    |
|                |                |                | PUSCH, WDBF or |
|                |                |                | PDBF for       |
|                |                |                | non-PUSCH      |
+----------------+----------------+----------------+----------------+
|                | BFW IQ         | 7.7.1, Annex J | REQ            |
|                |                |                |                |
|                |                |                | PTC2: Fixed    |
|                |                |                | point, 12 bits |
|                |                |                |                |
|                |                |                | PTC1: BFP, 8   |
|                |                |                | bits           |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | DL: O-RU REQ   |
|                | compression    |                |                |
|                | method         |                | PTC1: Mod      |
|                |                |                | Comp, no sel   |
|                |                |                | RE             |
|                |                |                |                |
|                |                |                | PTC2: BFP      |
|                |                |                |                |
|                |                |                | UL: REQ BFP    |
+----------------+----------------+----------------+----------------+
|                | U-Plane        | 8, Annex D     | DL: O-RU REQ   |
|                | (DL/UL) data   |                |                |
|                | IQ bitwidth    |                | PTC1: 4 bits   |
|                |                |                | (Mod Comp)     |
|                |                |                |                |
|                |                |                | PTC2: 9 bits,  |
|                |                |                | BFP            |
|                |                |                |                |
|                |                |                | UL: REQ: 9     |
|                |                |                | bits           |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | REQ            |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | REQ (for PRACH |
|                |                |                | )              |
+----------------+----------------+----------------+----------------+
|                | Section Type 4 | 7.4.6          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | REQ (for       |
|                |                |                | DMRS-BF)       |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | N/A            |
+----------------+----------------+----------------+----------------+
|                | Section Type 8 | 7.4.10         | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 9 | 7.4.11         | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type   | 7.4.12         | NOT REQ        |
|                | 10             |                |                |
+----------------+----------------+----------------+----------------+
|                | Section Type   | 7.4.13         | NOT REQ        |
|                | 11             |                |                |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | NOT REQ        |
|                | flag           |                |                |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | REQ: Single    |
|                | PRACH formats  |                | C-Plane        |
|                | with preamble  |                | message        |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | REQ            |
|                | extension 1    |                |                |
|                | (beamforming   |                |                |
|                | weights)       |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | NOT REQ        |
|                | extension 2    |                |                |
|                | (beamforming   |                |                |
|                | attributes)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | NOT REQ        |
|                | extension 3    |                |                |
|                | (DL Precoding  |                |                |
|                | configuration  |                |                |
|                | parameters and |                |                |
|                | indications)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | PTC2: NOT REQ  |
|                | extension 4    |                |                |
|                | (modulation    |                | PTC1: O-RU REQ |
|                | compr. params) |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | NOT REQ        |
|                | extension 5    |                |                |
|                | (modulation    |                |                |
|                | compression    |                |                |
|                | additional     |                |                |
|                | scaling        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.6          | NOT REQ        |
|                | extension 6    |                |                |
|                | (              |                |                |
|                | Non-contiguous |                |                |
|                | PRB            |                |                |
|                | allocation)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.7          | NOT REQ        |
|                | extension 7    |                |                |
|                | (Multiple-eAxC |                |                |
|                | designation)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.8          | NOT REQ        |
|                | extension 8    |                |                |
|                | (              |                |                |
|                | regularization |                |                |
|                | factor)        |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.9          | NOT REQ        |
|                | extension 9    |                |                |
|                | (Dynamic       |                |                |
|                | Spectrum       |                |                |
|                | Sharing        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.10         | REQ (for       |
|                | extension 10   |                | DMRS-BF)       |
|                | (Multiple      |                |                |
|                | ports          |                |                |
|                | grouping)      |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.11         | O-RU REQ       |
|                | extension 11   |                |                |
|                | (Flexible BF   |                |                |
|                | weights)       |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.12         | NOT REQ        |
|                | extension 12   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.13         | NOT REQ        |
|                | extension 13   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.14         | NOT REQ        |
|                | extension 14   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.15         | NOT REQ        |
|                | extension 15   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.16         | NOT REQ        |
|                | extension 16   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.17         | NOT REQ        |
|                | extension 17   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.18         | NOT REQ        |
|                | extension 18   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.19         | NOT REQ        |
|                | extension 19   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.20         | NOT REQ        |
|                | extension 20   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.21         | NOT REQ        |
|                | extension 21   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.22         | NOT REQ        |
|                | extension 22   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.23         | NOT REQ        |
|                | extension 23   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.24         | REQ            |
|                | extension 24   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.25         | REQ            |
|                | extension 25   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.26         | O-RU REQ       |
|                | extension 26   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.27         | NOT REQ        |
|                | extension 27   |                |                |
+----------------+----------------+----------------+----------------+
| DMRS-BF        | Port reduced   | 12.6.3.1       | REQ            |
|                | DMRS data      |                |                |
|                | sending        |                |                |
+----------------+----------------+----------------+----------------+
|                | User group     | 7.7.24         | NOT REQ        |
|                | self assembly  |                |                |
+----------------+----------------+----------------+----------------+
|                | Per-window     | 7.7.25,        | REQ            |
|                | symbol         | 12.6.1.5       |                |
|                | reordering     |                |                |
+----------------+----------------+----------------+----------------+
|                | Per section    | 7.7.25,        | NOT REQ        |
|                | tx-window      | 12.6.1.5       |                |
|                | reassignment   |                |                |
+----------------+----------------+----------------+----------------+
|                | symbolid       | 7.7.25         | REQ:           |
|                | meaining when  |                | Transmission   |
|                | reordering     |                | window number  |
|                | (up-symbolId-t |                |                |
|                | ype-supported) |                |                |
+----------------+----------------+----------------+----------------+
|                | Transform      | 7.7.24         | O-RU REQ       |
|                | precoding      |                |                |
|                | supported      |                |                |
+----------------+----------------+----------------+----------------+
|                | PUSCH and DMRS | 7.7.24         | O-RU REQ       |
|                | mux supported  |                |                |
+----------------+----------------+----------------+----------------+
|                | DMRS           | 7.7.24,        | REQ: Type 1    |
|                | configuration  | 7.7.24.14      | (dType=0)      |
|                | Type (dType)   |                |                |
+----------------+----------------+----------------+----------------+
|                | dmrsSymbolMask | 7.7.24         | REQ: 1+1       |
|                |                |                | (symbol        |
|                |                |                | location: 2,   |
|                |                |                | 11)            |
+----------------+----------------+----------------+----------------+
|                | different-t    | 7.7.24         | NOT REQ        |
|                | ransform-preco |                |                |
|                | ding-in-user-g |                |                |
|                | roup-supported |                |                |
+----------------+----------------+----------------+----------------+
|                | differen       | 7.7.24         | NOT REQ        |
|                | t-cdm-without- |                |                |
|                | data-in-user-g |                |                |
|                | roup-supported |                |                |
+----------------+----------------+----------------+----------------+
| Measurements   | SINR reporting | 7.2.11, 7.4.11 | N/A            |
+----------------+----------------+----------------+----------------+
|                | MEAS-UE-TAE    | 9.2.1          | NOT REQ.       |
|                | (UE timing     |                |                |
|                | advance error) |                | O-RU declares  |
|                |                |                | feature        |
|                |                |                | DMRS-BF-NEQ-   |
|                |                |                | UNALTERED-TAE. |
+----------------+----------------+----------------+----------------+
|                | MEAS-          | 9.2.1          | NOT REQ        |
|                | UE-LAYER-POWER |                |                |
+----------------+----------------+----------------+----------------+
|                | MEAS-          | 9.2.1          | NOT REQ.       |
|                | UE-FREQ-OFFSET |                |                |
|                |                |                | O-RU declares  |
|                |                |                | feature        |
|                |                |                | DMRS-B         |
|                |                |                | F-NEQ-UNALTERE |
|                |                |                | D-FREQ-OFFSET. |
+----------------+----------------+----------------+----------------+
|                | MEAS-IPN-ALLOC | 9.2.1          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | ME             | 9.2.1          | NOT REQ        |
|                | AS-IPN-UNALLOC |                |                |
+----------------+----------------+----------------+----------------+
|                | MEA            | 9.2.1          | NOT REQ        |
|                | S-ANT-DMRS-SNR |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | REQ            |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | NOT REQ        |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | N/A            |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2,\       | REQ: LLS-C1 or |
|                | configuration  | 11.2.3 (for    | LLS-C3         |
|                |                | PLFS)          |                |
+----------------+----------------+----------------+----------------+

Table A.3.1.13-2 lists "to be reported" and "to be validated"
capabilities in radio layer 3 C-plane establishment and initial radio
U-plane data transfer test. Table A.3.1.13-3 lists "to be reported" and
"to be validated" capabilities in U-plane DL data transfer test. Table
A.3.1.13-4 lists "to be reported" and "to be validated" capabilities in
U-plane UL data transfer test.

Table A.3.1.13-2: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 10 in radio layer 3 C-Plane establishment and initial
radio U-Plane data transfer test

  PTCs   
  ------ ----------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: WDBF for DL, DMRS-BF-NEQ for PUSCH, modulation compression, Per-window symbol reording using tx-window symbol number
         Capabilities to be reported: PDBF for DL, BFW BFP 8 bits, SE4, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer
  PTC2   Capabilities to be validated: WDBF for DL, DMRS-BF-NEQ for PUSCH, Per-window symbol reording using tx-window symbol number
         Capabilities to be reported: PDBF for DL, BFW Fixed point 12 bits, eAxC-ID format (3238 or 2338), M-Plane static window control for SRS transfer

Table A.3.1.14-3: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 11 in U-Plane DL data transfer test

  PTCs   
  ------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: WDBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, DMRS-BF-NEQ for PUSCH, Non-delay managed U-plane for SRS transfer, BFW BFP 8 bits, SE4, eAxC-ID format (3238 or 2338), Per-window symbol reording using tx-window symbol number
  PTC2   Capabilities to be validated: WDBF for DL
         Capabilities to be reported: PDBF for DL, DMRS-BF-NEQ for PUSCH, M-Plane static window control for SRS transfer, BFW Fixed point 12 bits, eAxC-ID format (3238 or 2338), Per-window symbol reording using tx-window symbol number

Table A.3.1.14-4: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 11 in U-Plane data UL transfer test

  PTCs   
  ------ ----------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: DMRS-BF-NEQ for PUSCH, modulation compression, Per-window symbol reording using tx-window symbol number
         Capabilities to be reported: WDBF or PDBF for DL, BFW BFP 8 bits, SE4, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer
  PTC2   Capabilities to be validated: DMRS-BF-NEQ for PUSCH, Per-window symbol reording using tx-window symbol number
         Capabilities to be reported: WDBF or PDBF for DL, BFW Fixed point 12 bits, eAxC-ID format (3238 or 2338), M-Plane static window control for SRS transfer

#### A.3.1.14 NR TDD IOT M-MIMO Profile 11 - NR-TDD-FR1-CAT-B-mMIMO-CIBF-DMRS-BF-EQ

Table A.3.1.14-1 shows the base profile. The following PTCs are defined.

1\)
NR-TDD-FR1-CAT-B-mMIMO-CIBF-DMRS-BF-EQ_PTC1\_\[SE4.ModComp-noSE25-noReorder\]

2\)
NR-TDD-FR1-CAT-B-mMIMO-CIBF-DMRS-BF-EQ_PTC2\_\[SE4.ModComp-SE25-PerWindow.reord-txwindow.upsymbolId\]

3\)
NR-TDD-FR1-CAT-B-mMIMO-CIBF-DMRS-BF-EQ_PTC3\_\[SE4.ModComp-SE25-PerSection.reord-onair.upsymbolId\]

Table A.3.1.14-1: NR TDD IOT M-MIMO Profile 11:
NR-TDD-FR1-CAT-B-mMIMO-CIBF-DMRS-BF-EQ

+----------------+----------------+----------------+----------------+
| Category       | Item           | Related O-RAN  |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)     |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR TDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | DDDSUUDDDD     |
|                | configuration  |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    |                | 4096           |
|                | size           |                |                |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | 100MHz x 1 CC  |
|                | bandwidth      |                |                |
+----------------+----------------+----------------+----------------+
|                | Number of user | \-             | DL: 2 -- 16    |
|                | layers         |                |                |
|                |                |                | UL: 2 -- 8     |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 25Gbps x 1     |
|                | Ethernet link  |                | lane           |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | O-RU REQ: F0   |
|                | format         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-RU category  | 4.2.1          | Category B     |
+----------------+----------------+----------------+----------------+
|                | LAA            | 7.2.5          | N/A            |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4          | Defined        |
| management,    | determination  |                | Transport      |
| general        |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 4.4.4.3        | NOT REQ        |
|                | adaptation of  |                |                |
|                | delay profile  |                |                |
|                | information    |                |                |
|                | (based on      |                |                |
|                | lls-CU delay   |                |                |
|                | profile and    |                |                |
|                | transport      |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | REQ: Fixed     |
|                | advance type   | Annex B        | timing Advance |
+----------------+----------------+----------------+----------------+
|                | SRS transfer   | 4.4.7          | REQ: Non-delay |
|                |                |                | managed        |
|                |                |                | U-Plane        |
+----------------+----------------+----------------+----------------+
| Delay          | Delay Sets for |                | REQ: Table     |
| management,    | timing         |                | A.4.2-1        |
| default        | parameters     |                |                |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
| Delay          | non-default    | 12.6.3         | REQ:           |
| management,    | beamforming    |                | DMRS-BF-EQ     |
| non default    | methods \#1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Delay Sets for |                | REQ: Table     |
|                | timing         |                | A.4.3-1        |
|                | parameters     |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | REQ: eCPRI     |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5.1.3.2        | NOT REQ        |
|                | concatenation  |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 3    |
|                | DU_Port_ID     |                | and 2          |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 2    |
|                | BandSector_ID  |                | and 3          |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | O-RU REQ: 3    |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 8    |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
|                |                |                | REQ            |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | Priority REQ   |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | NOT REQ        |
|                | prioritization |                |                |
|                | within U-Plane |                |                |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID REQ    |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | NOT REQ        |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0 dB           |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
|                | (not           |                |                |
|                | applicable to  |                |                |
|                | DMRS-BF-EQ)    |                |                |
+----------------+----------------+----------------+----------------+
|                | equalizatio    | 12.6.3.5       | REQ:           |
|                | n-data-scaling |                | Sca            |
|                |                |                | ling-function1 |
|                |                |                | or             |
|                |                |                | Sca            |
|                |                |                | ling-function2 |
+----------------+----------------+----------------+----------------+
| Beamforming    | O-RU           | 4.2.1          | REQ: Digital   |
|                | beamforming    |                | beamforming    |
|                | type           |                |                |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.2.1, 12.6,   | DL: REQ: CIBF  |
|                | control method | Annex J        | and PDBF       |
|                |                |                |                |
|                |                |                | UL: REQ:       |
|                |                |                | DMRS-BF for    |
|                |                |                | PUSCH, PDBF    |
|                |                |                | for non-PUSCH  |
+----------------+----------------+----------------+----------------+
|                | BFW IQ         | 7.7.1, Annex J | N/A            |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | DL: REQ:       |
|                | compression    |                | Modulation     |
|                | method         |                | compression,   |
|                |                |                | no selective   |
|                |                |                | RE             |
|                |                |                |                |
|                |                |                | UL: REQ: BFP   |
+----------------+----------------+----------------+----------------+
|                | U-Plane        | 8, Annex D     | REQ            |
|                | (DL/UL) data   |                |                |
|                | IQ bitwidth    |                | for Mod Comp   |
|                |                |                | in DL: 4 bits  |
|                |                |                |                |
|                |                |                | for BFP in UL: |
|                |                |                | 8 and 9 bits   |
|                |                |                | for DMRS-BF    |
|                |                |                | and 9 bits for |
|                |                |                | other BF       |
|                |                |                | methods        |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | REQ            |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | REQ (for PRACH |
|                |                |                | )              |
+----------------+----------------+----------------+----------------+
|                | Section Type 4 | 7.4.6          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | N/A            |
+----------------+----------------+----------------+----------------+
|                | Section Type 8 | 7.4.10         | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 9 | 7.4.11         | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section Type   | 7.4.12         | REQ            |
|                | 10             |                |                |
+----------------+----------------+----------------+----------------+
|                | Section Type   | 7.4.13         | O-RU REQ       |
|                | 11             |                |                |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | NOT REQ        |
|                | flag           |                |                |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | REQ: Single    |
|                | PRACH formats  |                | C-Plane        |
|                | with preamble  |                | message        |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | NOT REQ        |
|                | extension 1    |                |                |
|                | (beamforming   |                |                |
|                | weights)       |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | NOT REQ        |
|                | extension 2    |                |                |
|                | (beamforming   |                |                |
|                | attributes)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | NOT REQ        |
|                | extension 3    |                |                |
|                | (DL Precoding  |                |                |
|                | configuration  |                |                |
|                | parameters and |                |                |
|                | indications)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | REQ            |
|                | extension 4    |                |                |
|                | (modulation    |                |                |
|                | compr. params) |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | NOT REQ        |
|                | extension 5    |                |                |
|                | (modulation    |                |                |
|                | compression    |                |                |
|                | additional     |                |                |
|                | scaling        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.6          | NOT REQ        |
|                | extension 6    |                |                |
|                | (              |                |                |
|                | Non-contiguous |                |                |
|                | PRB            |                |                |
|                | allocation)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.7          | NOT REQ        |
|                | extension 7    |                |                |
|                | (Multiple-eAxC |                |                |
|                | designation)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.8          | NOT REQ        |
|                | extension 8    |                |                |
|                | (              |                |                |
|                | regularization |                |                |
|                | factor)        |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.9          | NOT REQ        |
|                | extension 9    |                |                |
|                | (Dynamic       |                |                |
|                | Spectrum       |                |                |
|                | Sharing        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.10         | REQ            |
|                | extension 10   |                |                |
|                | (Multiple      |                |                |
|                | ports          |                |                |
|                | grouping)      |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.11         | NOT REQ        |
|                | extension 11   |                |                |
|                | (Flexible BF   |                |                |
|                | weights)       |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.12         | NOT REQ        |
|                | extension 12   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.13         | NOT REQ        |
|                | extension 13   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.14         | NOT REQ        |
|                | extension 14   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.15         | NOT REQ        |
|                | extension 15   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.16         | NOT REQ        |
|                | extension 16   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.17         | NOT REQ        |
|                | extension 17   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.18         | NOT REQ        |
|                | extension 18   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.19         | NOT REQ        |
|                | extension 19   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.20         | NOT REQ        |
|                | extension 20   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.21         | NOT REQ        |
|                | extension 21   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.22         | NOT REQ        |
|                | extension 22   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.23         | NOT REQ        |
|                | extension 23   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.24         | REQ            |
|                | extension 24   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.25         | PTC1: NOT REQ  |
|                | extension 25   |                |                |
|                |                |                | PTC2, PTC3:    |
|                |                |                | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.26         | O-RU REQ       |
|                | extension 26   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.27         | NOT REQ        |
|                | extension 27   |                |                |
+----------------+----------------+----------------+----------------+
| DMRS-BF        | Port reduced   | 12.6.3.1       | O-RU REQ       |
|                | DMRS data      |                |                |
|                | sending        |                |                |
+----------------+----------------+----------------+----------------+
|                | User group     | 7.7.24         | NOT REQ        |
|                | self assembly  |                |                |
+----------------+----------------+----------------+----------------+
|                | Per-window     | 7.7.25,        | PTC1, PTC3:    |
|                | symbol         | 12.6.1.5       | NOT REQ        |
|                | reordering     |                |                |
|                |                |                | PTC2: REQ      |
|                |                |                |                |
|                |                |                | If             |
|                |                |                | \"per-window   |
|                |                |                | symbol         |
|                |                |                | reordering\"   |
|                |                |                | is used, then  |
|                |                |                | \"per-section  |
|                |                |                | tx-window      |
|                |                |                | reassignment\" |
|                |                |                | is not used.   |
+----------------+----------------+----------------+----------------+
|                | Per section    | 7.7.25,        | PTC1, PTC2:    |
|                | tx-window      | 12.6.1.5       | NOT REQ        |
|                | reassignment   |                |                |
|                |                |                | PTC3: REQ      |
|                |                |                |                |
|                |                |                | If             |
|                |                |                | \"per-section  |
|                |                |                | tx-window      |
|                |                |                | reassignment\" |
|                |                |                | is used, then  |
|                |                |                | \"per-window   |
|                |                |                | symbol         |
|                |                |                | reordering\"   |
|                |                |                | is not used.   |
+----------------+----------------+----------------+----------------+
|                | symbolid       | 7.7.25         | PTC1: N/A      |
|                | meaining when  |                |                |
|                | reordering     |                | PTC2:          |
|                | (up-symbolId-t |                | Transmission   |
|                | ype-supported) |                | window number  |
|                |                |                | REQ            |
|                |                |                |                |
|                |                |                | PTC3: on-air   |
|                |                |                | symbol number  |
|                |                |                | REQ            |
+----------------+----------------+----------------+----------------+
|                | Transform      | 7.7.24         | O-RU REQ       |
|                | precoding      |                |                |
|                | supported      |                |                |
+----------------+----------------+----------------+----------------+
|                | PUSCH and DMRS | 7.7.24         | O-RU REQ       |
|                | mux supported  |                |                |
+----------------+----------------+----------------+----------------+
|                | DMRS           | 7.7.24,        | REQ: Type 1    |
|                | configuration  | 7.7.24.14      | (dType=0)      |
|                | Type (dType)   |                |                |
+----------------+----------------+----------------+----------------+
|                | dmrsSymbolMask | 7.7.24         | REQ: 1+1       |
|                |                |                | (symbol        |
|                |                |                | location: 2,   |
|                |                |                | 11)            |
+----------------+----------------+----------------+----------------+
|                | different-t    | 7.7.24         | NOT REQ        |
|                | ransform-preco |                |                |
|                | ding-in-user-g |                |                |
|                | roup-supported |                |                |
+----------------+----------------+----------------+----------------+
|                | differen       | 7.7.24         | NOT REQ        |
|                | t-cdm-without- |                |                |
|                | data-in-user-g |                |                |
|                | roup-supported |                |                |
+----------------+----------------+----------------+----------------+
| Measurements   | SINR reporting | 7.2.11, 7.4.11 | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | MEAS-UE-TAE    | 9.2.1          | O-RU REQ       |
|                | (UE timing     |                |                |
|                | advance error) |                |                |
+----------------+----------------+----------------+----------------+
|                | MEAS-          | 9.2.1          | O-RU REQ       |
|                | UE-LAYER-POWER |                |                |
+----------------+----------------+----------------+----------------+
|                | MEAS-          | 9.2.1          | O-RU REQ       |
|                | UE-FREQ-OFFSET |                |                |
+----------------+----------------+----------------+----------------+
|                | MEAS-IPN-ALLOC | 9.2.1          | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | ME             | 9.2.1          | O-RU REQ       |
|                | AS-IPN-UNALLOC |                |                |
+----------------+----------------+----------------+----------------+
|                | MEA            | 9.2.1          | NOT REQ        |
|                | S-ANT-DMRS-SNR |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | REQ            |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | NOT REQ        |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | N/A            |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2,\       | REQ: LLS-C1 or |
|                | configuration  | 11.2.3 (for    | LLS-C3         |
|                |                | PLFS)          |                |
+----------------+----------------+----------------+----------------+

Table A.3.1.14-2 lists "to be reported" and "to be validated"
capabilities in radio layer 3 C-plane establishment and initial radio
U-plane data transfer test. Table A.3.1.14-3 lists "to be reported" and
"to be validated" capabilities in U-plane DL data transfer test. Table
A.3.1.14-4 lists "to be reported" and "to be validated" capabilities in
U-plane UL data transfer test.

Table A.3.1.14-2: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 11 in radio layer 3 C-Plane establishment and initial
radio U-Plane data transfer test

  PTCs   
  ------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: CIBF for DL, DMRS-BF-EQ for PUSCH, modulation compression
         Capabilities to be reported: PDBF for DL, SE4, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Non-delay managed U-plane for SRS transfer
  PTC2   Capabilities to be validated: CIBF for DL, DMRS-BF-EQ for PUSCH, modulation compression, Per-window symbol reording using tx-window symbol number
         Capabilities to be reported: PDBF for DL, SE4, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Non-delay managed U-plane for SRS transfer
  PTC3   Capabilities to be validated: CIBF for DL, DMRS-BF-EQ for PUSCH, modulation compression, Per-section tx-window reassignment using on-air symbol number
         Capabilities to be reported: PDBF for DL, SE4, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Non-delay managed U-plane for SRS transfer

Table A.3.1.14-3: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 11 in U-Plane DL data transfer test

  PTCs   
  ------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: CIBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, SE4, DMRS-BF-EQ for PUSCH, Non-delay managed U-plane for SRS transfer, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits)
  PTC2   Capabilities to be validated: CIBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, SE4, DMRS-BF-EQ for PUSCH, Non-delay managed U-plane for SRS transfer, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Per-window symbol reording using tx-window symbol number
  PTC3   Capabilities to be validated: CIBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, SE4, DMRS-BF-EQ for PUSCH, Non-delay managed U-plane for SRS transfer, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Per-section tx-window reassignment using on-air symbol number

Table A.3.1.14-4: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 11 in U-Plane data UL transfer test

  PTCs   
  ------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: DMRS-BF-EQ for PUSCH, modulation compression
         Capabilities to be reported: CIBF or PDBF for DL, SE4, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Non-delay managed U-plane for SRS transfer
  PTC2   Capabilities to be validated: DMRS-BF-EQ for PUSCH, modulation compression, Per-window symbol reording using tx-window symbol number
         Capabilities to be reported: CIBF or PDBF for DL, SE4, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Non-delay managed U-plane for SRS transfer
  PTC3   Capabilities to be validated: DMRS-BF-EQ for PUSCH, modulation compression, Per-section tx-window reassignment using on-air symbol number
         Capabilities to be reported: CIBF or PDBF for DL, SE4, eAxC-ID format (3238 or 2338), PUSCH data IQ bitwidth (8 bits or 9 bits), Non-delay managed U-plane for SRS transfer

#### A.3.1.15 NR TDD IOT M-MIMO Profile 12 - NR-TDD-FR1-CAT-B-mMIMO-CIBF-DMRS-BF-NEQ

Table A.3.1.15-1 describes the base profile. The following PTC is
defined.

1\)
NR-TDD-FR1-CAT-B-mMIMO-CIBF-DMRS-BF-NEQ_PTC1\_\[SE4.ModComp-noReorder\]

Table A.3.1.15-1: NR TDD IOT M-MIMO Profile 12:
NR-TDD-FR1-CAT-B-mMIMO-CIBF-DMRS-BF-NEQ

+----------------+----------------+----------------+----------------+
| Category       | Item           | Related O-RAN  |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)     |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR TDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | DDDSUUDDDD     |
|                | configuration  |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | 30kHz          |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    |                | 4096           |
|                | size           |                |                |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | 100MHz x 1 CC  |
|                | bandwidth      |                |                |
+----------------+----------------+----------------+----------------+
|                | Number of user | \-             | DL: 2 -- 16    |
|                | layers         |                |                |
|                |                |                | UL: 2 -- 8     |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 25Gbps x 1     |
|                | Ethernet link  |                | lane           |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | O-RU REQ: F0   |
|                | format         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-RU category  | 4.2.1          | Category B     |
+----------------+----------------+----------------+----------------+
|                | LAA            | 7.2.5          | N/A            |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4          | Defined        |
| management,    | determination  |                | Transport      |
| general        |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | O-RU           | 4.4.4.3        | NOT REQ        |
|                | adaptation of  |                |                |
|                | delay profile  |                |                |
|                | information    |                |                |
|                | (based on      |                |                |
|                | lls-CU delay   |                |                |
|                | profile and    |                |                |
|                | transport      |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | REQ: Fixed     |
|                | advance type   | Annex B        | timing Advance |
+----------------+----------------+----------------+----------------+
|                | SRS transfer   | 4.4.7          | REQ: Non-delay |
|                |                |                | managed        |
|                |                |                | U-Plane        |
+----------------+----------------+----------------+----------------+
| Delay          | Delay Sets for |                | REQ: Table     |
| management,    | timing         |                | A.4.2-1        |
| default        | parameters     |                |                |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160us          |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0us            |
+----------------+----------------+----------------+----------------+
| Delay          | non-default    | 12.6.3         | REQ:           |
| management,    | beamforming    |                | DMRS-BF-NEQ    |
| non default    | methods \#1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Delay Sets for |                | REQ: Table     |
|                | timing         |                | A.4.3-1        |
|                | parameters     |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plan       | Transport      | 5.1.1-5.1.2    | Ethernet       |
|                | encapsulation  |                |                |
| e transport    |                |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | REQ: eCPRI     |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5.1.3.2        | NOT REQ        |
|                | concatenation  |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 3    |
|                | DU_Port_ID     |                | and 2          |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 2    |
|                | BandSector_ID  |                | and 3          |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | O-RU REQ: 3    |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | O-RU REQ: 8    |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
|                |                |                | REQ            |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | Priority REQ   |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | NOT REQ        |
|                | prioritization |                |                |
|                | within U-Plane |                |                |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID REQ    |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | NOT REQ        |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0 dB           |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
|                | (not           |                |                |
|                | applicable to  |                |                |
|                | DMRS-BF-EQ)    |                |                |
+----------------+----------------+----------------+----------------+
|                | equalizatio    | 12.6.3.5       | N/A            |
|                | n-data-scaling |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | O-RU           | 4.2.1          | REQ: Digital   |
|                | beamforming    |                | beamforming    |
|                | type           |                |                |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.2.1, 12.6,   | DL: REQ: CIBF  |
|                | control method | Annex J        | and PDBF       |
|                |                |                |                |
|                |                |                | UL: REQ:       |
|                |                |                | DMRS-BF for    |
|                |                |                | PUSCH, PDBF    |
|                |                |                | for non-PUSCH  |
+----------------+----------------+----------------+----------------+
|                | BFW IQ         | 7.7.1, Annex J | N/A            |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | DL: REQ:       |
|                | compression    |                | Modulation     |
|                | method         |                | compression,   |
|                |                |                | no selective   |
|                |                |                | RE             |
|                |                |                |                |
|                |                |                | UL: REQ: BFP   |
+----------------+----------------+----------------+----------------+
|                | U-Plane        | 8, Annex D     | DL: REQ: 4     |
|                | (DL/UL) data   |                | bits           |
|                | IQ bitwidth    |                |                |
|                |                |                | UL: REQ: 9     |
|                |                |                | bits           |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | REQ            |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | O-RU REQ       |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | REQ (for PRACH |
|                |                |                | )              |
+----------------+----------------+----------------+----------------+
|                | Section Type 4 | 7.4.6          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | REQ            |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | N/A            |
+----------------+----------------+----------------+----------------+
|                | Section Type 8 | 7.4.10         | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type 9 | 7.4.11         | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | Section Type   | 7.4.12         | NOT REQ        |
|                | 10             |                |                |
+----------------+----------------+----------------+----------------+
|                | Section Type   | 7.4.13         | NOT REQ        |
|                | 11             |                |                |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | NOT REQ        |
|                | flag           |                |                |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | REQ: Single    |
|                | PRACH formats  |                | C-Plane        |
|                | with preamble  |                | message        |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | NOT REQ        |
|                | extension 1    |                |                |
|                | (beamforming   |                |                |
|                | weights)       |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | NOT REQ        |
|                | extension 2    |                |                |
|                | (beamforming   |                |                |
|                | attributes)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | NOT REQ        |
|                | extension 3    |                |                |
|                | (DL Precoding  |                |                |
|                | configuration  |                |                |
|                | parameters and |                |                |
|                | indications)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | REQ            |
|                | extension 4    |                |                |
|                | (modulation    |                |                |
|                | compr. params) |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | NOT REQ        |
|                | extension 5    |                |                |
|                | (modulation    |                |                |
|                | compression    |                |                |
|                | additional     |                |                |
|                | scaling        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.6          | NOT REQ        |
|                | extension 6    |                |                |
|                | (              |                |                |
|                | Non-contiguous |                |                |
|                | PRB            |                |                |
|                | allocation)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.7          | NOT REQ        |
|                | extension 7    |                |                |
|                | (Multiple-eAxC |                |                |
|                | designation)   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.8          | NOT REQ        |
|                | extension 8    |                |                |
|                | (              |                |                |
|                | regularization |                |                |
|                | factor)        |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.9          | NOT REQ        |
|                | extension 9    |                |                |
|                | (Dynamic       |                |                |
|                | Spectrum       |                |                |
|                | Sharing        |                |                |
|                | parameters)    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.10         | REQ            |
|                | extension 10   |                |                |
|                | (Multiple      |                |                |
|                | ports          |                |                |
|                | grouping)      |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.11         | NOT REQ        |
|                | extension 11   |                |                |
|                | (Flexible BF   |                |                |
|                | weights)       |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.12         | NOT REQ        |
|                | extension 12   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.13         | NOT REQ        |
|                | extension 13   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.14         | NOT REQ        |
|                | extension 14   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.15         | NOT REQ        |
|                | extension 15   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.16         | NOT REQ        |
|                | extension 16   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.17         | NOT REQ        |
|                | extension 17   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.18         | NOT REQ        |
|                | extension 18   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.19         | NOT REQ        |
|                | extension 19   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.20         | NOT REQ        |
|                | extension 20   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.21         | NOT REQ        |
|                | extension 21   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.22         | NOT REQ        |
|                | extension 22   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.23         | NOT REQ        |
|                | extension 23   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.24         | REQ            |
|                | extension 24   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.25         | NOT REQ        |
|                | extension 25   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.26         | O-RU REQ       |
|                | extension 26   |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.27         | NOT REQ        |
|                | extension 27   |                |                |
+----------------+----------------+----------------+----------------+
| DMRS-BF        | Port reduced   | 12.6.3.1       | REQ            |
|                | DMRS data      |                |                |
|                | sending        |                |                |
+----------------+----------------+----------------+----------------+
|                | User group     | 7.7.24         | NOT REQ        |
|                | self assembly  |                |                |
+----------------+----------------+----------------+----------------+
|                | Per-window     | 7.7.25,        | NOT REQ        |
|                | symbol         | 12.6.1.5       |                |
|                | reordering     |                |                |
|                | with DMRS      |                |                |
|                | sending        |                |                |
+----------------+----------------+----------------+----------------+
|                | Per section    | 7.7.25,        | NOT REQ        |
|                | tx-window      | 12.6.1.5       |                |
|                | reassignment   |                |                |
+----------------+----------------+----------------+----------------+
|                | symbolid       | 7.7.25         | N/A            |
|                | meaining when  |                |                |
|                | reordering     |                |                |
|                | (up-symbolId-t |                |                |
|                | ype-supported) |                |                |
+----------------+----------------+----------------+----------------+
|                | Transform      | 7.7.24         | O-RU REQ       |
|                | precoding      |                |                |
|                | supported      |                |                |
+----------------+----------------+----------------+----------------+
|                | PUSCH and DMRS | 7.7.24         | O-RU REQ       |
|                | mux supported  |                |                |
+----------------+----------------+----------------+----------------+
|                | DMRS           | 7.7.24,        | REQ: Type 1    |
|                | configuration  | 7.7.24.14      | (dType=0)      |
|                | Type (dType)   |                |                |
+----------------+----------------+----------------+----------------+
|                | dmrsSymbolMask | 7.7.24         | REQ: 1+1       |
|                |                |                | (symbol        |
|                |                |                | location: 2,   |
|                |                |                | 11)            |
+----------------+----------------+----------------+----------------+
|                | different-t    | 7.7.24         | NOT REQ        |
|                | ransform-preco |                |                |
|                | ding-in-user-g |                |                |
|                | roup-supported |                |                |
+----------------+----------------+----------------+----------------+
|                | differen       | 7.7.24         | NOT REQ        |
|                | t-cdm-without- |                |                |
|                | data-in-user-g |                |                |
|                | roup-supported |                |                |
+----------------+----------------+----------------+----------------+
| Measurements   | SINR reporting | 7.2.11, 7.4.11 | N/A            |
+----------------+----------------+----------------+----------------+
|                | MEAS-UE-TAE    | 9.2.1          | NOT REQ.       |
|                | (UE timing     |                |                |
|                | advance error) |                | O-RU declares  |
|                |                |                | feature        |
|                |                |                | DMRS-BF-NEQ-   |
|                |                |                | UNALTERED-TAE. |
+----------------+----------------+----------------+----------------+
|                | MEAS-          | 9.2.1          | NOT REQ        |
|                | UE-LAYER-POWER |                |                |
+----------------+----------------+----------------+----------------+
|                | MEAS-          | 9.2.1          | NOT REQ.       |
|                | UE-FREQ-OFFSET |                |                |
|                |                |                | O-RU declares  |
|                |                |                | feature        |
|                |                |                | DMRS-B         |
|                |                |                | F-NEQ-UNALTERE |
|                |                |                | D-FREQ-OFFSET. |
+----------------+----------------+----------------+----------------+
|                | MEAS-IPN-ALLOC | 9.2.1          | NOT REQ        |
+----------------+----------------+----------------+----------------+
|                | ME             | 9.2.1          | NOT REQ        |
|                | AS-IPN-UNALLOC |                |                |
+----------------+----------------+----------------+----------------+
|                | MEA            | 9.2.1          | NOT REQ        |
|                | S-ANT-DMRS-SNR |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | REQ            |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | NOT REQ        |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | N/A            |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2,\       | REQ: LLS-C1 or |
|                | configuration  | 11.2.3 (for    | LLS-C3         |
|                |                | PLFS)          |                |
+----------------+----------------+----------------+----------------+

Table A.3.1.15-2 lists "to be reported" and "to be validated"
capabilities in radio layer 3 C-plane establishment and initial radio
U-plane data transfer test. Table A.3.1.15-3 lists "to be reported" and
"to be validated" capabilities in U-plane DL data transfer test. Table
A.3.1.15-4 lists "to be reported" and "to be validated" capabilities in
U-plane UL data transfer test.

Table A.3.1.15-2: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 12 in radio layer 3 C-Plane establishment and initial
radio U-Plane data transfer test

  PTCs   
  ------ --------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: CIBF for DL, DMRS-BF-NEQ for PUSCH, modulation compression
         Capabilities to be reported: PDBF for DL, SE4, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer

Table A.3.1.15-3: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 12 in U-Plane DL data transfer test

  PTCs   
  ------ -------------------------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: CIBF for DL, modulation compression
         Capabilities to be reported: PDBF for DL, SE4, DMRS-BF-NEQ for PUSCH, Non-delay managed U-plane for SRS transfer, eAxC-ID format (3238 or 2338)

Table A.3.1.15-4: Capability to be reported or validated for NR TDD IOT
M-MIMO profile 12 in U-Plane data UL transfer test

  PTCs   
  ------ ----------------------------------------------------------------------------------------------------------------------------------
  PTC1   Capabilities to be validated: DMRS-BF-NEQ for PUSCH, modulation compression
         Capabilities to be reported: CIBF or PDBF for DL, SE4, eAxC-ID format (3238 or 2338), Non-delay managed U-plane for SRS transfer

### A.3.2 NR FDD 

#### A.3.2.1 NR FDD IOT Profile 1 - NR-FDD-FR1(15kHzSCS)-CAT-B-DBF 

Profile Test Configurations:

-   NR-FDD-FR1(15kHzSCS)-CAT-B-DBF\_\[20MHz-8SS-PRACH0-9bitIQ-llsC2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-B-DBF\_\[30MHz-8SS-PRACH0-9bitIQ-llsC2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-B-DBF\_\[20MHz-16SS-PRACH0-9bitIQ-llsC2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-B-DBF\_\[30MHz-16SS-PRACH0-9bitIQ-llsC2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-B-DBF\_\[20MHz-8SS-PRACHC2-9bitIQ-llsC2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-B-DBF\_\[30MHz-8SS-PRACHC2-9bitIQ-llsC2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-B-DBF\_\[20MHz-16SS-PRACHC2-9bitIQ-llsC2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-B-DBF\_\[30MHz-16SS-PRACHC2-9bitIQ-llsC2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-B-DBF\_\[20MHz-8SS-PRACH0-12bitIQ-llsC3\]

-   NR-FDD-FR1(15kHzSCS)-CAT-B-DBF\_\[30MHz-8SS-PRACH0-12bitIQ-llsC3\]

-   NR-FDD-FR1(15kHzSCS)-CAT-B-DBF\_\[20MHz-16SS-PRACH0-12bitIQ-llsC3\]

-   NR-FDD-FR1(15kHzSCS)-CAT-B-DBF\_\[30MHz-16SS-PRACH0-12bitIQ-llsC3\]

-   NR-FDD-FR1(15kHzSCS)-CAT-B-DBF\_\[20MHz-8SS-PRACHC2-12bitIQ-llsC3\]

-   NR-FDD-FR1(15kHzSCS)-CAT-B-DBF\_\[30MHz-8SS-PRACHC2-12bitIQ-llsC3\]

-   NR-FDD-FR1(15kHzSCS)-CAT-B-DBF\_\[20MHz-16SS-PRACHC2-12bitIQ-llsC3\]

-   NR-FDD-FR1(15kHzSCS)-CAT-B-DBF\_\[30MHz-16SS-PRACHC2-12bitIQ-llsC3\]

**Table A.3.2.1-1: NR FDD IOT Profile 1 -
NR-FDD-FR1(15kHzSCS)-CAT-B-DBF**

+----------------+----------------+----------------+----------------+
| **Category**   | **Item**       | **Related      |                |
|                |                | O-RAN          |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)**   |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR FDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | NA             |
|                | configuration  |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 15 kHz         |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | 15 kHz         |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    | \-             | 2048           |
|                | size           |                |                |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | Entry1: 20MHz\ |
|                | bandwidth      |                | Entry2:        |
|                |                |                | 20MHz+10MHz    |
+----------------+----------------+----------------+----------------+
|                | Number of      | \-             | Entry1: 8\     |
|                | s              |                | Entry2: 16     |
|                | patial/antenna |                |                |
|                | streams        |                |                |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 25Gbps x 1lane |
|                | Ethernet link  |                | for 8 spatial  |
|                |                |                | streams,\      |
|                |                |                | 25Gbps x 2lane |
|                |                |                | for 16 spatial |
|                |                |                | streams        |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | Entry1: 0\     |
|                | format         |                | Entry2: C2     |
+----------------+----------------+----------------+----------------+
|                | RU category    | 4.2.1          | Category B     |
+----------------+----------------+----------------+----------------+
|                | LAA            | \-             | FALSE          |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4.2        | Defined        |
| management     | determination  |                | Transport      |
|                |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | RU adaptation  | 4.4.4.3        | FALSE          |
|                | of delay       |                |                |
|                | profile        |                |                |
|                | information\   |                |                |
|                | (based on O-DU |                |                |
|                | delay profile  |                |                |
|                | and transport  |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | Fixed Timing   |
|                | advance type   | Annex B        | Advance        |
+----------------+----------------+----------------+----------------+
|                | T1a_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 437us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 366us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 437us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 206us |
+----------------+----------------+----------------+----------------+
|                | Tcp_adv_dl     | 4.3.2, Annex B | 125 us         |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 232us |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 70us  |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 392us |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 70us  |
+----------------+----------------+----------------+----------------+
|                | T1a_max_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 356us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 285us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 356us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 125us |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | Non-delay      | 4.4.7          | FALSE          |
|                | managed        |                |                |
|                | U-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | eCPRI          |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5              | FALSE          |
|                | concatenation  | .1.3.1-5.1.3.2 |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 2              |
|                | DU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 3              |
|                | BandSector_ID  |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | 3              |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 8              |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | priority       |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | False (Default |
|                | prioritization |                | U-Plane        |
|                | within U-Plane |                | priority       |
|                |                |                | applies)       |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID        |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | FALSE          |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0dB            |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | RU beamforming | 4.2.1 (10.1)   | Digital        |
|                | type           |                | beamforming    |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.3, Annex J   | Beamforming ID |
|                | control method |                | based          |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | Block floating |
|                | compression    |                | point          |
|                | method         |                |                |
+----------------+----------------+----------------+----------------+
|                | U-Plane data   | 8, Annex D     | Entry1: 9\     |
|                | IQ bitwidth    |                | Entry2: 12     |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | TRUE           |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | FALSE (always  |
|                | flag           |                | set to \'0\')  |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | Single C-Plane |
|                | PRACH formats  |                | message        |
|                | with preamble  |                |                |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | FALSE          |
|                | extension 1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | FALSE          |
|                | extension 2    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | FALSE          |
|                | extension 3    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | FALSE          |
|                | extension 4    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | FALSE          |
|                | extension 5    |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | TRUE           |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | FALSE          |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | FALSE          |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2         | Entry1:        |
|                | configuration  |                | lls-C2\        |
|                |                | 10, 11.2.3     | Entry2: lls-C3 |
|                |                | (for PLFS)     |                |
+----------------+----------------+----------------+----------------+

#### A.3.2.2 NR FDD IOT Profile 2 - NR-FDD-FR1-CAT-B-DBF 

Profile Test Configurations:

-   NR-FDD-FR1-CAT-B-DBF\_\[20MHz-8SS-9bitIQ-llsC2\]

-   NR-FDD-FR1-CAT-B-DBF\_\[30MHz-8SS-9bitIQ-llsC2\]

-   NR-FDD-FR1-CAT-B-DBF\_\[20MHz-16SS-9bitIQ-llsC2\]

-   NR-FDD-FR1-CAT-B-DBF\_\[30MHz-16SS-9bitIQ-llsC2\]

-   NR-FDD-FR1-CAT-B-DBF\_\[20MHz-8SS-12bitIQ-llsC3\]

-   NR-FDD-FR1-CAT-B-DBF\_\[30MHz-8SS-12bitIQ-llsC3\]

-   NR-FDD-FR1-CAT-B-DBF\_\[20MHz-16SS-12bitIQ-llsC3\]

-   NR-FDD-FR1-CAT-B-DBF\_\[30MHz-16SS-12bitIQ-llsC3\]

**Table A.3.2.2-1: NR FDD IOT Profile 2 - NR-FDD-FR1-CAT-B-DBF**

+----------------+----------------+----------------+----------------+
| **Category**   | **Item**       | **Related      |                |
|                |                | O-RAN          |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)**   |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR FDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | NA             |
|                | configuration  |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 30 kHz         |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | 30 kHz         |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    | \-             | 1024           |
|                | size           |                |                |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | Entry1: 20MHz\ |
|                | bandwidth      |                | Entry2:        |
|                |                |                | 20MHz+10MHz    |
+----------------+----------------+----------------+----------------+
|                | Number of      | \-             | Entry1: 8\     |
|                | s              |                | Entry2: 16     |
|                | patial/antenna |                |                |
|                | streams        |                |                |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 25Gbps x 1lane |
|                | Ethernet link  |                | for 8 spatial  |
|                |                |                | streams,\      |
|                |                |                | 25Gbps x 2lane |
|                |                |                | for 16 spatial |
|                |                |                | streams        |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | 0              |
|                | format         |                |                |
+----------------+----------------+----------------+----------------+
|                | RU category    | 4.2.1          | Category B     |
+----------------+----------------+----------------+----------------+
|                | LAA            | \-             | FALSE          |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4.2        | Defined        |
| management     | determination  |                | Transport      |
|                |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | RU adaptation  | 4.4.4.3        | FALSE          |
|                | of delay       |                |                |
|                | profile        |                |                |
|                | information\   |                |                |
|                | (based on O-DU |                |                |
|                | delay profile  |                |                |
|                | and transport  |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | Fixed Timing   |
|                | advance type   | Annex B        | Advance        |
+----------------+----------------+----------------+----------------+
|                | T1a_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 345us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 294us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 345us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 134us |
+----------------+----------------+----------------+----------------+
|                | Tcp_adv_dl     | 4.3.2, Annex B | 125 us         |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 171us |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 50us  |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 331us |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 50us  |
+----------------+----------------+----------------+----------------+
|                | T1a_max_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 336us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 285us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 336us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 125us |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | Non-delay      | 4.4.7          | FALSE          |
|                | managed        |                |                |
|                | U-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | eCPRI          |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5              | FALSE          |
|                | concatenation  | .1.3.1-5.1.3.2 |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 2              |
|                | DU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 3              |
|                | BandSector_ID  |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | 3              |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 8              |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | priority       |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | False (Default |
|                | prioritization |                | U-Plane        |
|                | within U-Plane |                | priority       |
|                |                |                | applies)       |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID        |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | FALSE          |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0dB            |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | RU beamforming | 4.2.1..(10.1)  | Digital        |
|                | type           |                | beamforming    |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.3, Annex J   | Beamforming ID |
|                | control method |                | based          |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | Block floating |
|                | compression    |                | point          |
|                | method         |                |                |
+----------------+----------------+----------------+----------------+
|                | U-Plane data   | 8, Annex D     | Entry1: 9\     |
|                | IQ bitwidth    |                | Entry2: 12     |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | TRUE           |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | FALSE (always  |
|                | flag           |                | set to \'0\')  |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | Single C-Plane |
|                | PRACH formats  |                | message        |
|                | with preamble  |                |                |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | FALSE          |
|                | extension 1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | FALSE          |
|                | extension 2    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | FALSE          |
|                | extension 3    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | FALSE          |
|                | extension 4    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | FALSE          |
|                | extension 5    |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | TRUE           |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | FALSE          |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | FALSE          |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2         | Entry1:        |
|                | configuration  |                | lls-C2\        |
|                |                | 10, 11.2.3     | Entry2: lls-C3 |
|                |                | (for PLFS)     |                |
+----------------+----------------+----------------+----------------+

#### A.3.2.3 NR FDD IOT Profile 3 - NR-FDD-FR1-CAT-A-NoBF 

Profile Test Configurations:

-   NR-FDD-FR1-CAT-A-NoBF\_\[20MHz-9bitIQ-llsC2\]

-   NR-FDD-FR1-CAT-A-NoBF\_\[30MHz-9bitIQ-llsC2\]

-   NR-FDD-FR1-CAT-A-NoBF\_\[20MHz-12bitIQ-llsC3\]

-   NR-FDD-FR1-CAT-A-NoBF\_\[30MHz-12bitIQ-llsC3\]

**Table A.3.2.3-1: NR FDD IOT Profile 3 - NR-FDD-FR1-CAT-A-NoBF**

+----------------+----------------+----------------+----------------+
| **Category**   | **Item**       | **Related      |                |
|                |                | O-RAN          |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)**   |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR FDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | NA             |
|                | configuration  |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 30 kHz         |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | 30 kHz         |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    | \-             | 1024           |
|                | size           |                |                |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | Entry1: 20MHz\ |
|                | bandwidth      |                | Entry2:        |
|                |                |                | 20MHz+10MHz    |
+----------------+----------------+----------------+----------------+
|                | Number of      | \-             | 4              |
|                | s              |                |                |
|                | patial/antenna |                |                |
|                | streams        |                |                |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 10Gbps x 1     |
|                | Ethernet link  |                | lane           |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | 0              |
|                | format         |                |                |
+----------------+----------------+----------------+----------------+
|                | RU category    | 4.2.1          | Category A     |
+----------------+----------------+----------------+----------------+
|                | LAA            | \-             | FALSE          |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4.2        | Defined        |
| management     | determination  |                | Transport      |
|                |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | RU adaptation  | 4.4.4.3        | FALSE          |
|                | of delay       |                |                |
|                | profile        |                |                |
|                | information\   |                |                |
|                | (based on O-DU |                |                |
|                | delay profile  |                |                |
|                | and transport  |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | Fixed Timing   |
|                | advance type   | Annex B        | Advance        |
+----------------+----------------+----------------+----------------+
|                | T1a_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 345us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 294us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 345us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 134us |
+----------------+----------------+----------------+----------------+
|                | Tcp_adv_dl     | 4.3.2, Annex B | 125 us         |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 171us |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 50us  |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 331us |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 50us  |
+----------------+----------------+----------------+----------------+
|                | T1a_max_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 336us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 285us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 336us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 125us |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | Non-delay      | 4.4.7          | FALSE          |
|                | managed        |                |                |
|                | U-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | eCPRI          |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5              | FALSE          |
|                | concatenation  | .1.3.1-5.1.3.2 |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 2              |
|                | DU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 3              |
|                | BandSector_ID  |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | 3              |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 8              |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | priority       |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | False (Default |
|                | prioritization |                | U-Plane        |
|                | within U-Plane |                | priority       |
|                |                |                | applies)       |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID        |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | FALSE          |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0dB            |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | RU beamforming | 4.2.1..(10.1)  | No beamforming |
|                | type           |                |                |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.3, Annex J   | Beamforming ID |
|                | control method |                | based (always  |
|                |                |                | \"0\")         |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | Block floating |
|                | compression    |                | point          |
|                | method         |                |                |
+----------------+----------------+----------------+----------------+
|                | U-Plane data   | 8, Annex D     | Entry1: 9\     |
|                | IQ bitwidth    |                | Entry2: 12     |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | TRUE           |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | FALSE (always  |
|                | flag           |                | set to \'0\')  |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | Single C-Plane |
|                | PRACH formats  |                | message        |
|                | with preamble  |                |                |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | FALSE          |
|                | extension 1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | FALSE          |
|                | extension 2    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | FALSE          |
|                | extension 3    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | FALSE          |
|                | extension 4    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | FALSE          |
|                | extension 5    |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | TRUE           |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | FALSE          |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | FALSE          |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2         | Entry1:        |
|                | configuration  |                | lls-C2\        |
|                |                | 10, 11.2.3     | Entry2: lls-C3 |
|                |                | (for PLFS)     |                |
+----------------+----------------+----------------+----------------+

#### A.3.2.4 NR FDD IOT Profile 4 - NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF

Profile Test Configurations:

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[10MHz-4SS-PRACHF0-9bitIQ-llsC2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[20MHz-4SS-PRACHF0-9bitIQ-llsC2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[10MHz-4SS-PRACHF0-12bitIQ-llsC2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[20MHz-4SS-PRACHF0-12bitIQ-llsC2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[10MHz-4SS-PRACHF0-9bitIQ-llsC3\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[20MHz-4SS-PRACHF0-9bitIQ-llsC3\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[10MHz-4SS-PRACHF0-12bitIQ-llsC3\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[20MHz-4SS-PRACHF0-12bitIQ-llsC3\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[10MHz-2SS-PRACHF0-9bitIQ-llsC2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[20MHz-2SS-PRACHF0-9bitIQ-llsC2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[10MHz-2SS-PRACHF0-12bitIQ-llsC2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[20MHz-2SS-PRACHF0-12bitIQ-llsC2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[10MHz-2SS-PRACHF0-9bitIQ-llsC3\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[20MHz-2SS-PRACHF0-9bitIQ-llsC3\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[10MHz-2SS-PRACHF0-12bitIQ-llsC3\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[20MHz-2SS-PRACHF0-12bitIQ-llsC3\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[10MHz-2SS-PRACHF0-14bitIQ-llsC1C2\]

-   NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF\_\[10MHz-2SS-PRACHF1-14bitIQ-llsC1C2\]

**Table A.3.2.4-1: NR FDD IOT Profile 4 -
NR-FDD-FR1(15kHzSCS)-CAT-A-NoBF**

+----------------+----------------+----------------+----------------+
| **Category**   | **Item**       | **Related      |                |
|                |                | O-RAN          |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)**   |                |
+================+================+================+================+
| General        | Radio access   | \-             | NR FDD         |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | NA             |
|                | configuration  |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 15 kHz         |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | 15 kHz         |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    | \-             | 1024 for 10MHz |
|                | size           |                | BW, 2048 for   |
|                |                |                | 20MHz BW       |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | Entry1: 10MHz\ |
|                | bandwidth      |                | Entry2: 20MHz  |
+----------------+----------------+----------------+----------------+
|                | Number of      | \-             | Entry1: 4\     |
|                | s              |                | Entry2: 2      |
|                | patial/antenna |                |                |
|                | streams        |                |                |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 10Gbps x 1     |
|                | Ethernet link  |                | lane           |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | Entry1: Long   |
|                | format         |                | preamble F0    |
|                |                |                |                |
|                |                |                | Entry2: Long   |
|                |                |                | preamble F1    |
+----------------+----------------+----------------+----------------+
|                | RU category    | 4.2.1          | Category A     |
+----------------+----------------+----------------+----------------+
|                | LAA            | \-             | FALSE          |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4.2        | Defined        |
| management     | determination  |                | Transport      |
|                |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | RU adaptation  | 4.4.4.3        | FALSE          |
|                | of delay       |                |                |
|                | profile        |                |                |
|                | information\   |                |                |
|                | (based on O-DU |                |                |
|                | delay profile  |                |                |
|                | and transport  |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | Fixed Timing   |
|                | advance type   | Annex B        | Advance        |
+----------------+----------------+----------------+----------------+
|                | T1a_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 437us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 366us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 437us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 206us |
+----------------+----------------+----------------+----------------+
|                | Tcp_adv_dl     | 4.3.2, Annex B | 125 us         |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 232us |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 70us  |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 392us |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 70us  |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                | (scs=1.25kHz)  |                | equal to       |
|                |                |                | 1650us         |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                | (scs=1.25kHz)  |                | equal to 827us |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4.3-4.4.4,   | More than or   |
|                | (scs=1.25kHz)  | Annex B        | equal to       |
|                |                |                | 1810us         |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4.3-4.4.4,   | Less than or   |
|                | (scs=1.25kHz)  | Annex B        | equal to 827us |
+----------------+----------------+----------------+----------------+
|                | T1a_max_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 356us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 285us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 356us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 125us |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | Non-delay      | 4.4.7          | FALSE          |
|                | managed        |                |                |
|                | U-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | eCPRI          |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5              | FALSE          |
|                | concatenation  | .1.3.1-5.1.3.2 |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 2              |
|                | DU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 6              |
|                | BandSector_ID  |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | 4              |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 4              |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | priority       |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | False (Default |
|                | prioritization |                | U-Plane        |
|                | within U-Plane |                | priority       |
|                |                |                | applies)       |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID        |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | FALSE          |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0dB            |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | RU beamforming | 4.2.1..(10.1)  | No beamforming |
|                | type           |                |                |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.3, Annex J   | Beamforming ID |
|                | control method |                | based (always  |
|                |                |                | \"0\")         |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | Block floating |
|                | compression    |                | point          |
|                | method         |                |                |
+----------------+----------------+----------------+----------------+
|                | U-Plane data   | 8, Annex D     | Entry1: 9\     |
|                | IQ bitwidth    |                | Entry2: 12     |
|                |                |                |                |
|                |                |                | Entry3: 14     |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | TRUE           |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | FALSE (always  |
|                | flag           |                | set to \'0\')  |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | Single C-Plane |
|                | PRACH formats  |                | message        |
|                | with preamble  |                |                |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | FALSE          |
|                | extension 1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | FALSE          |
|                | extension 2    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | FALSE          |
|                | extension 3    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | FALSE          |
|                | extension 4    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | FALSE          |
|                | extension 5    |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | TRUE           |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | FALSE          |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | FALSE          |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2         | Entry1: lls-C2 |
|                | configuration  |                | (can also      |
|                |                | 10, 11.2.3     | apply lls-C1)\ |
|                |                | (for PLFS)     | Entry2: lls-C3 |
+----------------+----------------+----------------+----------------+

### A.3.3 LTE FDD 

#### A.3.3.1 LTE FDD IOT Profile 1 - LTE-FDD-FR1-CAT-B-DBF 

Profile Test Configurations:

-   LTE-FDD-FR1-CAT-B-DBF\_\[20MHz-8SS-9bitIQ-llsC2\]

-   LTE-FDD-FR1-CAT-B-DBF\_\[30MHz-8SS-9bitIQ-llsC2\]

-   LTE-FDD-FR1-CAT-B-DBF\_\[20MHz-16SS-9bitIQ-llsC2\]

-   LTE-FDD-FR1-CAT-B-DBF\_\[30MHz-16SS-9bitIQ-llsC2\]

-   LTE-FDD-FR1-CAT-B-DBF\_\[20MHz-8SS-12bitIQ-llsC3\]

-   LTE-FDD-FR1-CAT-B-DBF\_\[30MHz-8SS-12bitIQ-llsC3\]

-   LTE-FDD-FR1-CAT-B-DBF\_\[20MHz-16SS-12bitIQ-llsC3\]

-   LTE-FDD-FR1-CAT-B-DBF\_\[30MHz-16SS-12bitIQ-llsC3\]

**Table A.3.3.1-1: LTE FDD IOT Profile 1 - LTE-FDD-FR1-CAT-B-DBF**

+----------------+----------------+----------------+----------------+
| **Category**   | **Item**       | **Related      |                |
|                |                | O-RAN          |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)**   |                |
+================+================+================+================+
| General        | Radio access   | \-             | LTE FDD        |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | NA             |
|                | configuration  |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 15 kHz         |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | NA             |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    | \-             | 2048           |
|                | size           |                |                |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | Entry1: 20MHz\ |
|                | bandwidth      |                | Entry2:        |
|                |                |                | 20MHz+10MHz    |
+----------------+----------------+----------------+----------------+
|                | Number of      | \-             | Entry1: 8\     |
|                | s              |                | Entry2: 16     |
|                | patial/antenna |                |                |
|                | streams        |                |                |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 25Gbps x 1lane |
|                | Ethernet link  |                | for 8 spatial  |
|                |                |                | streams,\      |
|                |                |                | 25Gbps x 2lane |
|                |                |                | for 16 spatial |
|                |                |                | streams        |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | 0              |
|                | format         |                |                |
+----------------+----------------+----------------+----------------+
|                | RU category    | 4.2.1          | Category B     |
+----------------+----------------+----------------+----------------+
|                | LAA            | \-             | FALSE          |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4.2        | Defined        |
| management     | determination  |                | Transport      |
|                |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | RU adaptation  | 4.4.4.3        | FALSE          |
|                | of delay       |                |                |
|                | profile        |                |                |
|                | information\   |                |                |
|                | (based on O-DU |                |                |
|                | delay profile  |                |                |
|                | and transport  |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | Fixed Timing   |
|                | advance type   | Annex B        | Advance        |
+----------------+----------------+----------------+----------------+
|                | T1a_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 437us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 366us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 437us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 206us |
+----------------+----------------+----------------+----------------+
|                | Tcp_adv_dl     | 4.3.2, Annex B | 125 us         |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 232us |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 70us  |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 392us |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 70us  |
+----------------+----------------+----------------+----------------+
|                | T1a_max_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 356us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 285us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 356us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 125us |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | Non-delay      | 4.4.7          | FALSE          |
|                | managed        |                |                |
|                | U-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | eCPRI          |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5              | FALSE          |
|                | concatenation  | .1.3.1-5.1.3.2 |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 2              |
|                | DU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 3              |
|                | BandSector_ID  |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | 3              |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 8              |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | priority       |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | False (Default |
|                | prioritization |                | U-Plane        |
|                | within U-Plane |                | priority       |
|                |                |                | applies)       |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID        |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | FALSE          |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0dB            |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | RU beamforming | 4.2.1..(10.1)  | Digital        |
|                | type           |                | beamforming    |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.3, Annex J   | Beamforming ID |
|                | control method |                | based          |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | Block floating |
|                | compression    |                | point          |
|                | method         |                |                |
+----------------+----------------+----------------+----------------+
|                | U-Plane data   | 8, Annex D     | Entry1: 9\     |
|                | IQ bitwidth    |                | Entry2: 12     |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | TRUE           |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | FALSE (always  |
|                | flag           |                | set to \'0\')  |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | Single C-Plane |
|                | PRACH formats  |                | message        |
|                | with preamble  |                |                |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | FALSE          |
|                | extension 1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | FALSE          |
|                | extension 2    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | TRUE           |
|                | extension 3    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | FALSE          |
|                | extension 4    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | FALSE          |
|                | extension 5    |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | TRUE           |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | FALSE          |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | FALSE          |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2         | Entry1:        |
|                | configuration  |                | lls-C2\        |
|                |                | 10, 11.2.3     | Entry2: lls-C3 |
|                |                | (for PLFS)     |                |
+----------------+----------------+----------------+----------------+

#### A.3.3.2 LTE FDD IOT Profile 2 - LTE-FDD-FR1-CAT-A-NoBF 

Profile Test Configurations:

-   LTE-FDD-FR1-CAT-A-NoBF\_\[10MHz-2SS-9bitIQ-llsC1C2\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[20MHz-2SS-9bitIQ-llsC1C2\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[10MHz-2SS-12bitIQ-llsC1C2\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[20MHz-2SS-12bitIQ-llsC1C2\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[10MHz-4SS-9bitIQ-llsC3\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[20MHz-4SS-9bitIQ-llsC3\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[10MHz-4SS-12bitIQ-llsC3\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[20MHz-4SS-12bitIQ-llsC3\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[10MHz-2SS-9bitIQ-llsC3\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[15MHz-2SS-9bitIQ-llsC3\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[15MHz-4SS-9bitIQ-llsC3\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[20MHz-2SS-9bitIQ-llsC3\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[40MHz-2SS-12bitIQ-llsC1C2\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[20MHz-4SS-12bitIQ-llsC1C2\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[20MHz-4SS-12bitIQ-llsC1C2-Jumbo\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[20MHz-2SS-12bitIQ-llsC3-Jumbo\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[20MHz-4SS-12bitIQ-llsC3-Jumbo\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[40MHz-4SS-12bitIQ-llsC3-Jumbo\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[5MHz-2SS-16bitIQ-llsC1C2\]

-   LTE-FDD-FR1-CAT-A-NoBF\_\[60MHz-4SS-16bitIQ-llsC1C2-Jumbo\]

**Table A.3.3.2-1: LTE FDD IOT Profile 2 - LTE-FDD-FR1-CAT-A-NoBF**

+----------------+----------------+----------------+----------------+
| **Category**   | **Item**       | **Related      |                |
|                |                | O-RAN          |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)**   |                |
+================+================+================+================+
| General        | Radio access   | \-             | LTE FDD        |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | NA             |
|                | configuration  |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 15 kHz         |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | NA             |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    | \-             | 1024 for 10MHz |
|                | size           |                | BW, 1536 for   |
|                |                |                | 15MHz BW, 2048 |
|                |                |                | for 20MHz BW   |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | Entry1: 5MHz\  |
|                | bandwidth      |                | Entry2: 10MHz\ |
|                |                |                | Entry3: 15MHz\ |
|                |                |                | Entry4: 20MHz\ |
|                |                |                | Entry5:        |
|                |                |                | 20MHz+20MHz\   |
|                |                |                | Entry6:        |
|                |                |                | 20M            |
|                |                |                | Hz+20MHz+20MHz |
+----------------+----------------+----------------+----------------+
|                | Number of      | \-             | Entry1: 2\     |
|                | s              |                | Entry2: 4      |
|                | patial/antenna |                |                |
|                | streams        |                |                |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 10Gbps x 1lane |
|                | Ethernet link  |                |                |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | 0              |
|                | format         |                |                |
+----------------+----------------+----------------+----------------+
|                | RU category    | 4.2.1          | Category A     |
+----------------+----------------+----------------+----------------+
|                | LAA            | \-             | FALSE          |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4.2        | Defined        |
| management     | determination  |                | Transport      |
|                |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | RU adaptation  | 4.4.4.3        | FALSE          |
|                | of delay       |                |                |
|                | profile        |                |                |
|                | information\   |                |                |
|                | (based on O-DU |                |                |
|                | delay profile  |                |                |
|                | and transport  |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | Fixed Timing   |
|                | advance type   | Annex B        | Advance        |
+----------------+----------------+----------------+----------------+
|                | T1a_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 437us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 366us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 437us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 206us |
+----------------+----------------+----------------+----------------+
|                | Tcp_adv_dl     | 4.3.2, Annex B | 125 us         |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 232us |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 70us  |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 392us |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 70us  |
+----------------+----------------+----------------+----------------+
|                | T1a_max_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 356us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 285us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 356us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 125us |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | Non-delay      | 4.4.7          | FALSE          |
|                | managed        |                |                |
|                | U-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | Entry1: FALSE\ |
|                |                |                | Entry2: TRUE   |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | eCPRI          |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5              | FALSE          |
|                | concatenation  | .1.3.1-5.1.3.2 |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 2              |
|                | DU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 6              |
|                | BandSector_ID  |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | 4              |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 4              |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | priority       |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | False (Default |
|                | prioritization |                | U-Plane        |
|                | within U-Plane |                | priority       |
|                |                |                | applies)       |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID        |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | FALSE          |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0dB            |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | RU beamforming | 4.2.1..(10.1)  | No beamforming |
|                | type           |                |                |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.3, Annex J   | Beamforming ID |
|                | control method |                | based (always  |
|                |                |                | \"0\")         |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | Entry1: Block  |
|                | compression    |                | floating       |
|                | method         |                | point\         |
|                |                |                | Entry2: No     |
|                |                |                | compression    |
+----------------+----------------+----------------+----------------+
|                | U-Plane data   | 8, Annex D     | For Block      |
|                | IQ bitwidth    |                | floating       |
|                |                |                | point:\        |
|                |                |                | Entry1: 9\     |
|                |                |                | Entry2: 12\    |
|                |                |                | For No         |
|                |                |                | compression:   |
|                |                |                | 16             |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | TRUE           |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | FALSE (always  |
|                | flag           |                | set to \'0\')  |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | Single C-Plane |
|                | PRACH formats  |                | message        |
|                | with preamble  |                |                |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | FALSE          |
|                | extension 1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | FALSE          |
|                | extension 2    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | FALSE          |
|                | extension 3    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | FALSE          |
|                | extension 4    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | FALSE          |
|                | extension 5    |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | TRUE           |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | FALSE          |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | FALSE          |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2         | Entry1: lls-C1 |
|                | configuration  |                | (can also      |
|                |                | 10, 11.2.3     | apply lls-C2)\ |
|                |                | (for PLFS)     | Entry2: lls-C3 |
+----------------+----------------+----------------+----------------+

### A.3.4 LTE TDD 

#### A.3.4.1 LTE TDD IOT Profile 1 - LTE-TDD-FR1-CAT-A-DBF 

Profile Test Configurations:

-   LTE-TDD-FR1-CAT-A-DBF\_\[20MHz-9bitIQ-llsC2\]

-   LTE-TDD-FR1-CAT-A-DBF\_\[30MHz-9bitIQ-llsC2\]

-   LTE-TDD-FR1-CAT-A-DBF\_\[40MHz-9bitIQ-llsC2\]

-   LTE-TDD-FR1-CAT-A-DBF\_\[20MHz-16bitIQ-llsC2\]

-   LTE-TDD-FR1-CAT-A-DBF\_\[30MHz-16bitIQ-llsC2\]

-   LTE-TDD-FR1-CAT-A-DBF\_\[40MHz-16bitIQ-llsC2\]

-   LTE-TDD-FR1-CAT-A-DBF\_\[20MHz-9bitIQ-llsC3\]

-   LTE-TDD-FR1-CAT-A-DBF\_\[30MHz-9bitIQ-llsC3\]

-   LTE-TDD-FR1-CAT-A-DBF\_\[40MHz-9bitIQ-llsC3\]

-   LTE-TDD-FR1-CAT-A-DBF\_\[20MHz-16bitIQ-llsC3\]

-   LTE-TDD-FR1-CAT-A-DBF\_\[30MHz-16bitIQ-llsC3\]

-   LTE-TDD-FR1-CAT-A-DBF\_\[40MHz-16bitIQ-llsC3\]

**Table A.3.4.1-1: LTE TDD IOT Profile 1 - LTE-TDD-FR1-CAT-A-DBF**

+----------------+----------------+----------------+----------------+
| **Category**   | **Item**       | **Related      |                |
|                |                | O-RAN          |                |
|                |                | CUS-Plane      |                |
|                |                | specification  |                |
|                |                | section(s)**   |                |
+================+================+================+================+
| General        | Radio access   | \-             | LTE TDD        |
|                | technology     |                |                |
+----------------+----------------+----------------+----------------+
|                | TDD            | \-             | subf           |
|                | configuration  |                | rameAssignment |
|                |                |                | sa2            |
+----------------+----------------+----------------+----------------+
|                | Nominal        | \-             | 15 kHz         |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | SSB            | \-             | NA             |
|                | sub-carrier    |                |                |
|                | spacing        |                |                |
+----------------+----------------+----------------+----------------+
|                | Nominal FFT    | \-             | 1024 for 10MHz |
|                | size           |                | BW, 2048 for   |
|                |                |                | 20MHz BW       |
+----------------+----------------+----------------+----------------+
|                | Total channel  | \-             | Entry1: 20MHz  |
|                | bandwidth      |                |                |
|                |                |                | Entry2:        |
|                |                |                | 20MHz+10MHz    |
|                |                |                |                |
|                |                |                | Entry3:        |
|                |                |                | 20MHz+20MHz    |
+----------------+----------------+----------------+----------------+
|                | Number of      | \-             | 8              |
|                | s              |                |                |
|                | patial/antenna |                |                |
|                | streams        |                |                |
+----------------+----------------+----------------+----------------+
|                | Fronthaul      | \-             | 10Gbps x 1     |
|                | Ethernet link  |                | lane for 20MHz |
|                |                |                |                |
|                |                |                | 10Gbps x 2     |
|                |                |                | lane for       |
|                |                |                | 20MHz+10MHz,   |
|                |                |                | 20MHz+20MHz    |
+----------------+----------------+----------------+----------------+
|                | PRACH preamble | \-             | 0              |
|                | format         |                |                |
+----------------+----------------+----------------+----------------+
|                | RU category    | 4.2.1          | Category A     |
+----------------+----------------+----------------+----------------+
|                | LAA            | \-             | FALSE          |
+----------------+----------------+----------------+----------------+
| Delay          | Network delay  | 4.4.4.2        | Defined        |
| management     | determination  |                | Transport      |
|                |                |                | Method         |
+----------------+----------------+----------------+----------------+
|                | RU adaptation  | 4.4.4.3        | FALSE          |
|                | of delay       |                |                |
|                | profile        |                |                |
|                | information\   |                |                |
|                | (based on O-DU |                |                |
|                | delay profile  |                |                |
|                | and transport  |                |                |
|                | delay)         |                |                |
+----------------+----------------+----------------+----------------+
|                | O-DU timing    | 4.4.5-4.4.6,   | Fixed Timing   |
|                | advance type   | Annex B        | Advance        |
+----------------+----------------+----------------+----------------+
|                | T1a_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 437us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 366us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 437us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 206us |
+----------------+----------------+----------------+----------------+
|                | Tcp_adv_dl     | 4.3.2, Annex B | 125 us         |
+----------------+----------------+----------------+----------------+
|                | Ta3_max_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 232us |
+----------------+----------------+----------------+----------------+
|                | Ta3_min_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 70us  |
+----------------+----------------+----------------+----------------+
|                | Ta4_max_up     | 4.4, Annex B   | More than or   |
|                |                |                | equal to 392us |
+----------------+----------------+----------------+----------------+
|                | Ta4_min_up     | 4.4, Annex B   | Less than or   |
|                |                |                | equal to 70us  |
+----------------+----------------+----------------+----------------+
|                | T1a_max_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 356us |
+----------------+----------------+----------------+----------------+
|                | T1a_min_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 285us |
+----------------+----------------+----------------+----------------+
|                | T2a_max_cp_ul  | 4.4.3-4.4.4,   | More than or   |
|                |                | Annex B        | equal to 356us |
+----------------+----------------+----------------+----------------+
|                | T2a_min_cp_ul  | 4.4.3-4.4.4,   | Less than or   |
|                |                | Annex B        | equal to 125us |
+----------------+----------------+----------------+----------------+
|                | T12_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T12_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | T34_max        | 4.4, Annex B   | 160 us         |
+----------------+----------------+----------------+----------------+
|                | T34_min        | 4.4, Annex B   | 0 us           |
+----------------+----------------+----------------+----------------+
|                | Non-delay      | 4.4.7          | FALSE          |
|                | managed        |                |                |
|                | U-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| C/U-Plane      | Transport      | 5.1.1-5.1.2    | Ethernet       |
| transport      | encapsulation  |                |                |
+----------------+----------------+----------------+----------------+
|                | Jumbo frames   | 5.1.2          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.1.3          | eCPRI          |
|                | header         |                |                |
+----------------+----------------+----------------+----------------+
|                | eCPRI          | 5              | FALSE          |
|                | concatenation  | .1.3.1-5.1.3.2 |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 4              |
|                | DU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 3              |
|                | BandSector_ID  |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID CC_ID  | 5.1.3.2.7      | 3              |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | eAxC ID        | 5.1.3.2.7      | 6              |
|                | RU_Port_ID     |                |                |
|                | bitwidth       |                |                |
+----------------+----------------+----------------+----------------+
|                | Fragmentation  | 5.5            | Application    |
|                |                |                | layer          |
|                |                |                | fragmentation  |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | Default L2 CoS |
|                | prioritization |                | priority       |
|                | across         |                |                |
|                | C/U/S/M-Plane  |                |                |
+----------------+----------------+----------------+----------------+
|                | Transport      | 5.3            | False (Default |
|                | prioritization |                | U-Plane        |
|                | within U-Plane |                | priority       |
|                |                |                | applies)-Plane |
+----------------+----------------+----------------+----------------+
|                | Separation of  | 5.4            | VLAN ID        |
|                | C/U-Plane and  |                |                |
|                | M-Plane        |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
|                | T              | 5.4            | FALSE          |
|                | ransport-based |                |                |
|                | separation     |                |                |
|                | within         |                |                |
|                | C/U-Plane      |                |                |
|                | traffic        |                |                |
+----------------+----------------+----------------+----------------+
| Digital Power  | UL             | 8.1.3.2        | 0dB            |
| Scaling        | g              |                |                |
|                | ain_correction |                |                |
+----------------+----------------+----------------+----------------+
| Beamforming    | RU beamforming | 4.2.1..(10.1)  | Digital        |
|                | type           |                | beamforming    |
+----------------+----------------+----------------+----------------+
|                | Beamforming    | 7.3, Annex J   | Beamforming    |
|                | control method |                | weight based   |
+----------------+----------------+----------------+----------------+
| IQ compression | U-Plane data   | 8, Annex A     | Entry1: Block  |
|                | compression    |                | floating point |
|                | method         |                |                |
|                |                |                | Entry2: No     |
|                |                |                | compression    |
+----------------+----------------+----------------+----------------+
|                | U-Plane data   | 8, Annex D     | 9 for Block    |
|                | IQ bitwidth    |                | floating       |
|                |                |                | point, 16 for  |
|                |                |                | No compression |
+----------------+----------------+----------------+----------------+
|                | IQ data frame  | 8.3.3.13       | TRUE           |
|                | format not     |                |                |
|                | including      |                |                |
|                | udCompHdr      |                |                |
|                | field          |                |                |
+----------------+----------------+----------------+----------------+
| C-Plane        | Section Type 0 | 7.4.2          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 1 | 7.4.3          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 3 | 7.4.5          | TRUE           |
+----------------+----------------+----------------+----------------+
|                | Section Type 5 | 7.4.7          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 6 | 7.4.8          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | Section Type 7 | 7.4.9          | FALSE          |
+----------------+----------------+----------------+----------------+
|                | \"symInc\"     | 7.5.3.3        | FALSE (always  |
|                | flag           |                | set to \'0\')  |
+----------------+----------------+----------------+----------------+
|                | C-Plane for    | 7.2.3.4        | Single C-Plane |
|                | PRACH formats  |                | message        |
|                | with preamble  |                |                |
|                | repetition     |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.1          | FALSE          |
|                | extension 1    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.2          | FALSE          |
|                | extension 2    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.3          | TRUE           |
|                | extension 3    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.4          | FALSE          |
|                | extension 4    |                |                |
+----------------+----------------+----------------+----------------+
|                | Section        | 7.7.5          | FALSE          |
|                | extension 5    |                |                |
+----------------+----------------+----------------+----------------+
| S-Plane        | PTP Full       | 5.2.3, 10.1,   | TRUE           |
|                | Timing Support | 11             |                |
|                | (G.8275.1)     |                |                |
+----------------+----------------+----------------+----------------+
|                | PTP Partial    | 5.2.3, 10.1,   | FALSE          |
|                | Timing Support | 11             |                |
|                | (G.8275.2)     |                |                |
+----------------+----------------+----------------+----------------+
|                | Local PRTC     | 5.2.3, 10.1,   | FALSE          |
|                |                | 11             |                |
+----------------+----------------+----------------+----------------+
|                | Topology       | 11.2.2         | Entry1: lls-C2 |
|                | configuration  |                |                |
|                |                | 10, 11.2.3     | Entry2: lls-C3 |
|                |                | (for PLFS)     |                |
+----------------+----------------+----------------+----------------+

## A.4 Delay Sets

### A.4.1 NR TDD FR1 Cat-B mMIMO WDBF Delay Sets for DMRS-BF profiles

Table A.4.1-1 defines the Delay Sets for NR TDD FR1 Cat-B mMIMO WDBF
when used in DMRS-BF profiles. For IOT entry, both O-DU and O-RU shall
share at least one common Delay Set.

Table A.4.1-1: NR TDD FR1 CAT-B mMIMO WDBF Delay Sets for DMRS-BF
profile

  **C/U-Plane timing parameters**   **Range**               **DS-W1 (WDBF DS1)**   **DS-W2 (WDBF DS2)**
  --------------------------------- ----------------------- ---------------------- ----------------------
  T1a_max_up                        Less than or equal to   345 us                 475 us
  T1a_min_up                        More than or equal to   294 us                 400 us
  T1a_max_cp_dl                     Less than or equal to   669 us                 971 us
  T1a_min_cp_dl                     More than or equal to   419 us                 550 us
  T2a_max_up                        More than or equal to   345 us                 475 us
  T2a_min_up                        Less than or equal to   134 us                 240 us
  T2a_max_cp_dl                     More than or equal to   669 us                 971 us
  T2a_min_cp_dl                     Less than or equal to   259 us                 390 us
  Tcp_adv_dl                                                125 us                 150 us
  Ta3_max_up                        Less than or equal to   171 us                 280 us
  Ta3_min_up                        More than or equal to   50 us                  50 us
  Ta4_max_up                        More than or equal to   331 us                 440 us
  Ta4_min_up                        Less than or equal to   50 us                  50 us
  Ta3_max_up (scs=1.25kHz)          Less than or equal to   1650 us                1650 us
  Ta3_min_up (scs=1.25kHz)          More than or equal to   827 us                 827 us
  Ta4_max_up (scs=1.25kHz)          More than or equal to   1810 us                1810 us
  Ta4_min_up (scs=1.25kHz)          Less than or equal to   827 us                 827 us
  T1a_max_cp_ul                     Less than or equal to   840 us                 840 us
  T1a_min_cp_ul                     More than or equal to   660 us                 660 us
  T2a_max_cp_ul                     More than or equal to   840 us                 840 us
  T2a_min_cp_ul                     Less than or equal to   500 us                 500 us

### A.4.2 NR TDD FR1 Cat-B mMIMO CIBF Delay Sets

Delay Set for NR TDD FR1 Cat-B mMIMO CIBF is defined in Table A.4.2-1.

Table A.4.2-1: NR TDD FR1 CAT-B mMIMO CIBF Delay Sets

  **C/U-Plane timing parameters**   **Range**               **DS-C1 (CIBF DS1)**
  --------------------------------- ----------------------- ----------------------
  T1a_max_up                        Less than or equal to   345 us
  T1a_min_up                        More than or equal to   294 us
  T1a_max_cp_dl                     Less than or equal to   820 us
  T1a_min_cp_dl                     More than or equal to   769 us
  T2a_max_up                        More than or equal to   345 us
  T2a_min_up                        Less than or equal to   134 us
  T2a_max_cp_dl                     More than or equal to   820 us
  T2a_min_cp_dl                     Less than or equal to   609 us
  Tcp_adv_dl                                                475 us
  Ta3_max_up                        Less than or equal to   171 us
  Ta3_min_up                        More than or equal to   50 us
  Ta4_max_up                        More than or equal to   331 us
  Ta4_min_up                        Less than or equal to   50 us
  Ta3_max_up (scs=1.25kHz)          Less than or equal to   1650 us
  Ta3_min_up (scs=1.25kHz)          More than or equal to   827 us
  Ta4_max_up (scs=1.25kHz)          More than or equal to   1810 us
  Ta4_min_up (scs=1.25kHz)          Less than or equal to   827 us
  T1a_max_cp_ul                     Less than or equal to   336 us
  T1a_min_cp_ul                     More than or equal to   285 us
  T2a_max_cp_ul                     More than or equal to   336 us
  T2a_min_cp_ul                     Less than or equal to   125 us

### A.4.3 NR TDD FR1 Cat-B mMIMO DMRS-BF Delay Sets

The Delay Sets specified in Table A.4.3-1 apply to both DMRS-BF-EQ and
DMRS-BF-NEQ. For entry to IOT testing, both O-DU and O-RU shall share at
least one common Delay Set. DS-D1 (DMRS-BF DS 1) is recommended for
interoperability testing. DS-D2 (DMRS-BF DS 2) may alternatively be used
for interoperability testing. For profiles in which measurements are not
required, support for 2g timing parameters is optional.

Table A.4.3-1: NR TDD FR1 CAT-B mMIMO DMRS-BF Delay Sets

  **C/U-Plane timing parameters**                                                                                                 **Range**               **DS-D1 (DMRS-BF DS 1)**   **DS-D2 (DMRS-BF DS 2)**
  ------------------------------------------------------------------------------------------------------------------------------- ----------------------- -------------------------- --------------------------
  Ta3_max_2g                                                                                                                      Less than or equal to   1280 us                    1280 us
  Ta3_min_2g                                                                                                                      More than or equal to   571 us                     571 us
  Ta4_max_2g                                                                                                                      More than or equal to   1440 us                    1440 us
  Ta4_min_2g                                                                                                                      Less than or equal to   571 us                     571 us
  Ta3_max_up                                                                                                                      Less than or equal to   1080 us                    1180 us
  Ta3_min_up                                                                                                                      More than or equal to   823 us                     886 us
  Ta4_max_up                                                                                                                      More than or equal to   1240 us                    1340 us
  Ta4_min_up                                                                                                                      Less than or equal to   823 us                     886 us
  T1a_max_cp_ul (NOTE)                                                                                                            Less than or equal to   840 us                     840 us
  T1a_min_cp_ul (NOTE)                                                                                                            More than or equal to   660 us                     660 us
  T2a_max_cp_ul (NOTE)                                                                                                            More than or equal to   840 us                     840 us
  T2a_min_cp_ul (NOTE)                                                                                                            Less than or equal to   500 us                     500 us
  NOTE: This is applicable to all C-plane messages constrained by T2a_max_cp_ul and T2a_min_cp_ul sent to the DMRS-BF endpoint.                                                      

# Annex (informative): Change history/Change request (history)

+----------------------+----------------------+----------------------+
| #                    | # **Revisi           | # **Description*     |
| **Date** {#date .TT} | on** {#revision .TT} | * {#description .TT} |
+======================+======================+======================+
| # 2019.09            | # 01                 | # Firs               |
| .05 {#section-1 .TT} | .00 {#section-2 .TT} | t published version  |
|                      |                      | for Fronthaul Intero |
|                      |                      | perability Test Spec |
|                      |                      | ification (IOT) {#fi |
|                      |                      | rst-published-versio |
|                      |                      | n-for-fronthaul-inte |
|                      |                      | roperability-test-sp |
|                      |                      | ecification-iot .TT} |
+----------------------+----------------------+----------------------+
| # 2020.03            | # 02                 | # Second             |
| .13 {#section-3 .TT} | .00 {#section-4 .TT} |  published version f |
|                      |                      | or Fronthaul Interop |
|                      |                      | erability Test Speci |
|                      |                      | fication (IOT) {#sec |
|                      |                      | ond-published-versio |
|                      |                      | n-for-fronthaul-inte |
|                      |                      | roperability-test-sp |
|                      |                      | ecification-iot .TT} |
+----------------------+----------------------+----------------------+
| # 2020.1             | # 03                 | # Implement chan     |
| 1.5 {#section-5 .TT} | .00 {#section-6 .TT} | ge requests, minor e |
|                      |                      | ditorials, slave rep |
|                      |                      | laced by subordinate |
|                      |                      |  {#implement-change- |
|                      |                      | requests-minor-edito |
|                      |                      | rials-slave-replaced |
|                      |                      | -by-subordinate .TT} |
|                      |                      |                      |
|                      |                      | # CIS_2020 10 13-o   |
|                      |                      | RAN-WG4 IoT CR CIS-1 |
|                      |                      | 6 SSHv2 ciphers (3)  |
|                      |                      | {#cis_2020-10-13-ora |
|                      |                      | n-wg4-iot-cr-cis-16- |
|                      |                      | sshv2-ciphers-3 .TT} |
|                      |                      |                      |
|                      |                      | # O-                 |
|                      |                      | RAN.WG4.IOT.v2.00_FM |
|                      |                      | _RVG3 {#o-ran.wg4.io |
|                      |                      | t.v2.00_fm_rvg3 .TT} |
|                      |                      |                      |
|                      |                      | # Incl               |
|                      |                      | udes text mandating  |
|                      |                      | both the IOT Profile |
|                      |                      |  and the Spec versio |
|                      |                      | n are nominated to e |
|                      |                      | nsure the appropriat |
|                      |                      | e parameter values a |
|                      |                      | re referenced. {#inc |
|                      |                      | ludes-text-mandating |
|                      |                      | -both-the-iot-profil |
|                      |                      | e-and-the-spec-versi |
|                      |                      | on-are-nominated-to- |
|                      |                      | ensure-the-appropria |
|                      |                      | te-parameter-values- |
|                      |                      | are-referenced. .TT} |
+----------------------+----------------------+----------------------+
| # 2021.03            | # 04                 | # Rename Profiles as |
| .18 {#section-7 .TT} | .00 {#section-8 .TT} |  Profile Test Config |
|                      |                      | urations NOK-0052 {# |
|                      |                      | rename-profiles-as-p |
|                      |                      | rofile-test-configur |
|                      |                      | ations-nok-0052 .TT} |
|                      |                      |                      |
|                      |                      | # M-Plane corr       |
|                      |                      | ection NEC-0009 rev1 |
|                      |                      |  {#m-plane-correctio |
|                      |                      | n-nec-0009-rev1 .TT} |
|                      |                      |                      |
|                      |                      | # M-Plane sy         |
|                      |                      | stem recovery action |
|                      |                      |  for S-Plane degrade |
|                      |                      | d conditions NEC-001 |
|                      |                      | 0 {#m-plane-system-r |
|                      |                      | ecovery-action-for-s |
|                      |                      | -plane-degraded-cond |
|                      |                      | itions-nec-0010 .TT} |
|                      |                      |                      |
|                      |                      | # Update eaxc_       |
|                      |                      | id to align with M-P |
|                      |                      | lane and CUS-Plane d |
|                      |                      | escription {#update- |
|                      |                      | eaxc_id-to-align-wit |
|                      |                      | h-m-plane-and-cus-pl |
|                      |                      | ane-description .TT} |
|                      |                      |                      |
|                      |                      | # Update eax         |
|                      |                      | c_id to eaxc-id to a |
|                      |                      | lign with M-Plane Sp |
|                      |                      | ecification {#update |
|                      |                      | -eaxc_id-to-eaxc-id- |
|                      |                      | to-align-with-m-plan |
|                      |                      | e-specification .TT} |
|                      |                      |                      |
|                      |                      | # Include mMIM       |
|                      |                      | O IOT profile and as |
|                      |                      | sociated test equipm |
|                      |                      | ent update {#include |
|                      |                      | -mmimo-iot-profile-a |
|                      |                      | nd-associated-test-e |
|                      |                      | quipment-update .TT} |
|                      |                      |                      |
|                      |                      | # mMIMO Prof         |
|                      |                      | ile Test Configurati |
|                      |                      | ons and FFS {#mmimo- |
|                      |                      | profile-test-configu |
|                      |                      | rations-and-ffs .TT} |
|                      |                      |                      |
|                      |                      | # Inclu              |
|                      |                      | des values of Ta3_ma |
|                      |                      | x-up, Ta3_min_up, Ta |
|                      |                      | 4_max_up, Ta4_min_up |
|                      |                      |  in the mMIMO profil |
|                      |                      | es which were accide |
|                      |                      | ntally omitted. {#in |
|                      |                      | cludes-values-of-ta3 |
|                      |                      | _max-up-ta3_min_up-t |
|                      |                      | a4_max_up-ta4_min_up |
|                      |                      | -in-the-mmimo-profil |
|                      |                      | es-which-were-accide |
|                      |                      | ntally-omitted. .TT} |
+----------------------+----------------------+----------------------+
| # 2021.07            | # 05.                | # CRs                |
| .06 {#section-9 .TT} | 00 {#section-10 .TT} | and text proposals w |
|                      |                      | ere implemented alon |
|                      |                      | g with editorial upd |
|                      |                      | ates {#crs-and-text- |
|                      |                      | proposals-were-imple |
|                      |                      | mented-along-with-ed |
|                      |                      | itorial-updates .TT} |
|                      |                      |                      |
|                      |                      | # Correct de         |
|                      |                      | scription of delay p |
|                      |                      | rofile tests MAV-001 |
|                      |                      | 7 {#correct-descript |
|                      |                      | ion-of-delay-profile |
|                      |                      | -tests-mav-0017 .TT} |
|                      |                      |                      |
|                      |                      | # Add mMIMO IO       |
|                      |                      | T profile test confi |
|                      |                      | gurations VIA-CR0005 |
|                      |                      |  {#add-mmimo-iot-pro |
|                      |                      | file-test-configurat |
|                      |                      | ions-via-cr0005 .TT} |
|                      |                      |                      |
|                      |                      | # Update mMIMO       |
|                      |                      |  IOT profile re sect |
|                      |                      | ion extension 1,11 a |
|                      |                      | nd 4,5 MAV-0022 & 00 |
|                      |                      | 26 {#update-mmimo-io |
|                      |                      | t-profile-re-section |
|                      |                      | -extension-111-and-4 |
|                      |                      | 5-mav-0022-0026 .TT} |
|                      |                      |                      |
|                      |                      | # Add mMIMO PRAC     |
|                      |                      | H delay parameters V |
|                      |                      | IA-CR0006 {#add-mmim |
|                      |                      | o-prach-delay-parame |
|                      |                      | ters-via-cr0006 .TT} |
|                      |                      |                      |
|                      |                      | # Upda               |
|                      |                      | ting IOT profile for |
|                      |                      |  S-plane and alignin |
|                      |                      | g them with CUS tabl |
|                      |                      | e 8-2 NOK-0075 {#upd |
|                      |                      | ating-iot-profile-fo |
|                      |                      | r-s-plane-and-aligni |
|                      |                      | ng-them-with-cus-tab |
|                      |                      | le-8-2-nok-0075 .TT} |
|                      |                      |                      |
|                      |                      | # Annex A text to c  |
|                      |                      | larify the intent an |
|                      |                      | d completeness of an |
|                      |                      |  IOT profile test  { |
|                      |                      | #annex-a-text-to-cla |
|                      |                      | rify-the-intent-and- |
|                      |                      | completeness-of-an-i |
|                      |                      | ot-profile-test .TT} |
+----------------------+----------------------+----------------------+
| # 2021.11.           | # 06.                | # CR and             |
| 14 {#section-11 .TT} | 00 {#section-12 .TT} | text proposals and e |
|                      |                      | ditorial updates and |
|                      |                      |  updates to referenc |
|                      |                      | es  {#cr-and-text-pr |
|                      |                      | oposals-and-editoria |
|                      |                      | l-updates-and-update |
|                      |                      | s-to-references .TT} |
|                      |                      |                      |
|                      |                      | # IQ compression     |
|                      |                      |  field correction fo |
|                      |                      | r mMIMO IOR profiles |
|                      |                      |  MAV-0027 {#iq-compr |
|                      |                      | ession-field-correct |
|                      |                      | ion-for-mmimo-ior-pr |
|                      |                      | ofiles-mav-0027 .TT} |
|                      |                      |                      |
|                      |                      | # New                |
|                      |                      | mMIMO IOT profile ti |
|                      |                      | ming parameters ERI- |
|                      |                      | 0030 {#new-mmimo-iot |
|                      |                      | -profile-timing-para |
|                      |                      | meters-eri-0030 .TT} |
|                      |                      |                      |
|                      |                      | # Update             |
|                      |                      |  of NR TDD IOT profi |
|                      |                      | le 1 CHM-0003 {#upda |
|                      |                      | te-of-nr-tdd-iot-pro |
|                      |                      | file-1-chm-0003 .TT} |
|                      |                      |                      |
|                      |                      | # Update of NR TDD p |
|                      |                      | rofile 2 DCM-0015 {# |
|                      |                      | update-of-nr-tdd-pro |
|                      |                      | file-2-dcm-0015 .TT} |
|                      |                      |                      |
|                      |                      | # Update of NR FDD   |
|                      |                      |  profile4 DCM-0016 { |
|                      |                      | #update-of-nr-fdd-pr |
|                      |                      | ofile4-dcm-0016 .TT} |
|                      |                      |                      |
|                      |                      | # M-Plane IOT pr     |
|                      |                      | ofile for IPv6 and T |
|                      |                      | LS RMI-0003 + IOT Pr |
|                      |                      | ofile Configurations |
|                      |                      |  {#m-plane-iot-profi |
|                      |                      | le-for-ipv6-and-tls- |
|                      |                      | rmi-0003-iot-profile |
|                      |                      | -configurations .TT} |
+----------------------+----------------------+----------------------+
| # 2022.03.           | # 07.                | # CR and text pro    |
| 08 {#section-13 .TT} | 00 {#section-14 .TT} | posals and editorial |
|                      |                      |  updates  {#cr-and-t |
|                      |                      | ext-proposals-and-ed |
|                      |                      | itorial-updates .TT} |
|                      |                      |                      |
|                      |                      | #                    |
|                      |                      |  Correct M-Plane tes |
|                      |                      | ts to use Ipv6/TLS V |
|                      |                      | IA-0007 {#correct-m- |
|                      |                      | plane-tests-to-use-i |
|                      |                      | pv6tls-via-0007 .TT} |
|                      |                      |                      |
|                      |                      | Add M-Plane hybrid   |
|                      |                      | mode profile         |
|                      |                      | Ipv6/TLS VIA-0008    |
+----------------------+----------------------+----------------------+
| # 2022.08.           | # 08.                | # CR                 |
| 03 {#section-15 .TT} | 00 {#section-16 .TT} | text proposals, upda |
|                      |                      | te reference to CUS/ |
|                      |                      | M specs, editorial u |
|                      |                      | pdates {#cr-text-pro |
|                      |                      | posals-update-refere |
|                      |                      | nce-to-cusm-specs-ed |
|                      |                      | itorial-updates .TT} |
|                      |                      |                      |
|                      |                      | # O-RAN FH IOT pro   |
|                      |                      | file modifications f |
|                      |                      | or NR TDD DCM-0020 { |
|                      |                      | #o-ran-fh-iot-profil |
|                      |                      | e-modifications-for- |
|                      |                      | nr-tdd-dcm-0020 .TT} |
|                      |                      |                      |
|                      |                      | #                    |
|                      |                      | IOT Profile modifica |
|                      |                      | tions for TDD config |
|                      |                      | uration of UL heavy  |
|                      |                      | pattern DCM-0021 {#i |
|                      |                      | ot-profile-modificat |
|                      |                      | ions-for-tdd-configu |
|                      |                      | ration-of-ul-heavy-p |
|                      |                      | attern-dcm-0021 .TT} |
|                      |                      |                      |
|                      |                      | Removal of Annex ZZZ |
|                      |                      | and related          |
|                      |                      | references           |
+----------------------+----------------------+----------------------+
| # 2022.11.           | # 09.                | #                    |
| 08 {#section-17 .TT} | 00 {#section-18 .TT} |  CR text proposals,  |
|                      |                      | editorial updates {# |
|                      |                      | cr-text-proposals-ed |
|                      |                      | itorial-updates .TT} |
|                      |                      |                      |
|                      |                      | # Alignment to t     |
|                      |                      | emplate VIA CR-0009  |
|                      |                      | {#alignment-to-templ |
|                      |                      | ate-via-cr-0009 .TT} |
|                      |                      |                      |
|                      |                      | IOT                  |
|                      |                      | -profile-terminology |
|                      |                      | update QCM CR-0056   |
+----------------------+----------------------+----------------------+
| # 2023.03.           | # 10.                | # C                  |
| 17 {#section-19 .TT} | 00 {#section-20 .TT} | R text proposals, ed |
|                      |                      | itorial updates {#cr |
|                      |                      | -text-proposals-edit |
|                      |                      | orial-updates-1 .TT} |
|                      |                      |                      |
|                      |                      | # Align              |
|                      |                      | to TSC drafting rule |
|                      |                      | s NEC CR-0020 {#alig |
|                      |                      | n-to-tsc-drafting-ru |
|                      |                      | les-nec-cr-0020 .TT} |
|                      |                      |                      |
|                      |                      | Modification to      |
|                      |                      | delay management     |
|                      |                      | tests VIA CR-0009    |
|                      |                      |                      |
|                      |                      | Proposed set of      |
|                      |                      | parameters to assign |
|                      |                      | as modifiable or     |
|                      |                      | forbidden for        |
|                      |                      | Customized IOT       |
|                      |                      | Profiles concept     |
|                      |                      | introduced into      |
|                      |                      | version 9.0 VIA      |
|                      |                      | CR-0008              |
+----------------------+----------------------+----------------------+
| # 2024.03.           | # 11.                | # C                  |
| 18 {#section-21 .TT} | 00 {#section-22 .TT} | R text proposals, ed |
|                      |                      | itorial updates {#cr |
|                      |                      | -text-proposals-edit |
|                      |                      | orial-updates-2 .TT} |
|                      |                      |                      |
|                      |                      | Clarification that   |
|                      |                      | it is mandatory to   |
|                      |                      | test at least 1      |
|                      |                      | synchronization      |
|                      |                      | topology and         |
|                      |                      | provided clear test  |
|                      |                      | classifications for  |
|                      |                      | each test DTAG -0001 |
+----------------------+----------------------+----------------------+
| # 2024.07.           | # 12.                | # C                  |
| 03 {#section-23 .TT} | 00 {#section-24 .TT} | R text proposals, ed |
|                      |                      | itorial updates {#cr |
|                      |                      | -text-proposals-edit |
|                      |                      | orial-updates-3 .TT} |
|                      |                      |                      |
|                      |                      | Update that it is    |
|                      |                      | conditional          |
|                      |                      | mandatory to test    |
|                      |                      | M-Plane hybrid mode, |
|                      |                      | conditional upon the |
|                      |                      | O-DU supporting it.  |
|                      |                      | DCM-022              |
+----------------------+----------------------+----------------------+
| # 2024.12.           | # 12.00.             | # C                  |
| 03 {#section-25 .TT} | 01 {#section-26 .TT} | R text proposals, ed |
|                      |                      | itorial updates {#cr |
|                      |                      | -text-proposals-edit |
|                      |                      | orial-updates-4 .TT} |
|                      |                      |                      |
|                      |                      | Correction of        |
|                      |                      | references: ERI-0127 |
|                      |                      |                      |
|                      |                      | Update clause        |
|                      |                      | numbering ERI-0133   |
+----------------------+----------------------+----------------------+
| # 2025.03.           | # 12.00.             | # Correctio          |
| 04 {#section-27 .TT} | 02 {#section-28 .TT} | n of clause numberin |
|                      |                      | g CR implementation  |
|                      |                      | after comments from  |
|                      |                      | Ericsson and Qualcom |
|                      |                      | m  {#correction-of-c |
|                      |                      | lause-numbering-cr-i |
|                      |                      | mplementation-after- |
|                      |                      | comments-from-ericss |
|                      |                      | on-and-qualcomm .TT} |
+----------------------+----------------------+----------------------+
| # 2025.03.           | # 12.00.             | # Baseline version w |
| 11 {#section-29 .TT} | 03 {#section-30 .TT} | ith changes from ERI |
|                      |                      | -0127 and ERI-0133 a |
|                      |                      | ccepted {#baseline-v |
|                      |                      | ersion-with-changes- |
|                      |                      | from-eri-0127-and-er |
|                      |                      | i-0133-accepted .TT} |
+----------------------+----------------------+----------------------+
| # 2025.03.           | # 12.00.             | # C                  |
| 12 {#section-31 .TT} | 04 {#section-32 .TT} | R text proposals, ed |
|                      |                      | itorial updates {#cr |
|                      |                      | -text-proposals-edit |
|                      |                      | orial-updates-5 .TT} |
|                      |                      |                      |
|                      |                      | # VIA-0010 DMRS-     |
|                      |                      | BF uplink throughput |
|                      |                      |  test v13 {#via-0010 |
|                      |                      | -dmrs-bf-uplink-thro |
|                      |                      | ughput-test-v13 .TT} |
|                      |                      |                      |
|                      |                      | ERI-0134 IOT         |
|                      |                      | addition of ULPI     |
|                      |                      | profiles v10         |
+----------------------+----------------------+----------------------+
| # 2025.03.           | # 12.00.             | # Correction o       |
| 16 {#section-33 .TT} | 05 {#section-34 .TT} | f implementation aft |
|                      |                      | er comments from NEC |
|                      |                      |  {#correction-of-imp |
|                      |                      | lementation-after-co |
|                      |                      | mments-from-nec .TT} |
+----------------------+----------------------+----------------------+
| # 2025.03.           | # 12.00.             | # Corre              |
| 18 {#section-35 .TT} | 06 {#section-36 .TT} | ction of implementat |
|                      |                      | ion after comments f |
|                      |                      | rom ERI, QCM, NOK, a |
|                      |                      | nd call to resolve i |
|                      |                      | ssues {#correction-o |
|                      |                      | f-implementation-aft |
|                      |                      | er-comments-from-eri |
|                      |                      | -qcm-nok-and-call-to |
|                      |                      | -resolve-issues .TT} |
+----------------------+----------------------+----------------------+
| # 2025.03.           | # 12.00.             | # Reinstate de       |
| 19 {#section-37 .TT} | 07 {#section-38 .TT} | lay sets (accidental |
|                      |                      | ly removed) {#reinst |
|                      |                      | ate-delay-sets-accid |
|                      |                      | entally-removed .TT} |
+----------------------+----------------------+----------------------+
| # 2025.03.           | # 12.00.             | # Min                |
| 21 {#section-39 .TT} | 08 {#section-40 .TT} | or updates from disc |
|                      |                      | ussion in ad-hoc cal |
|                      |                      | l, apply O-RAN forma |
|                      |                      | tting to tables {#mi |
|                      |                      | nor-updates-from-dis |
|                      |                      | cussion-in-ad-hoc-ca |
|                      |                      | ll-apply-o-ran-forma |
|                      |                      | tting-to-tables .TT} |
+----------------------+----------------------+----------------------+
| # 2025.03.           | # 13.00.             | # Accept all         |
| 23 {#section-41 .TT} | 00 {#section-42 .TT} |  changes and change  |
|                      |                      | title and file name  |
|                      |                      | to 13.00.00 {#accept |
|                      |                      | -all-changes-and-cha |
|                      |                      | nge-title-and-file-n |
|                      |                      | ame-to-13.00.00 .TT} |
+----------------------+----------------------+----------------------+
| # 2025.03.           | # 13.                | # Up                 |
| 25 {#section-43 .TT} | 00 {#section-44 .TT} | date file name to 13 |
|                      |                      | .00 and minor editor |
|                      |                      | ial corrections {#up |
|                      |                      | date-file-name-to-13 |
|                      |                      | .00-and-minor-editor |
|                      |                      | ial-corrections .TT} |
+----------------------+----------------------+----------------------+
