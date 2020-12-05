# Name: SecurePass
Despite its widely-discussed shortcomings, text password authentication is widely used to authenticate users to online services. Many attempts have been made to replace simple password authentication, e.g. using biometrics, tokens, and multifactor authentication. However, single-factor password-based authentication remains very widely used. Moreover, in recent years the number of widely-used password-protected services has grown in turn increasing the number of passwords users are expected to remember. There is a range of issues associated with the use of text pass-words. These issues can be categorized as either user-related or online.

# The reason behind the selection of this topic:
Help people to create a strong password.

# Objectives:
1. Create a strong password(<b>maximum 94 character</b>)
2. Make existing password Secure

# Methodology:
# A password generator has the following components:
1. A set of input values is used to determine the password for a particular site. Some values must be site-specific so that the generated password is site-specific. The values could be stored based on characteristics of the authenticating site, or user-entered when re-quired. Systems can, and often do combine these types of input.

2. A password generation function combines the input values to generate an appropriate password. This function could operate in a range of ways depending on the requirements of the web site performing the authentication. For example, one web site might forbid the inclusion of non-alphanumeric characters in a password, whereas another might insist that a password contains at least one such character. To be broadly applicable, a password generation function must, therefore.

3. A password output method enables the generated password to be transferred to the authenticating site. This could, for example, involve dis-playing the generated password to the user, who must then type it into the appropriate place. All this functionality needs to be implemented on the user platform. There are various possibilities for such an implementation, including as a stand-alone application or as a browser plug-in.

# Software Configuration:
1. Operating System: Windows.
2. Language: Python.
2. IDE: PyCharm.

# Features:
1. Create a secure password
2. Combination of lowercase + uppercase + digits + punctuation
3. Random password
4. User can choose a password size
5. Two methods assure randomness
6. take the previous password and return a secure password
# New Features!
1. After an action is performed, it ask you, if you want to run again or exit

# References:
    https://projects.raspberrypi.org/en/projects/password-generator
    
# Check SecurePassword online:
    https://repl.it/@montasimmamun/LightpinkLimegreenLists#main.py

# Author
    Author: Mohammad Montasim -Al- Mamun Shuvo
    Github: https://github.com/montasimmamun

# License
    Apache-2.0 License
    
# Project status
    Active
