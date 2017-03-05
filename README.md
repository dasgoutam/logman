# logman
<p>A keylogger written in python to serve Linux distros.</p>
<p>This logger is built using the pyxhook library created by Jeff Hoogland(https://github.com/JeffHoogland/pyxhook), which itself is an implementation of the popular pyhook library for windows.</p>

<h3>Why logman was created</h3>
<p>logman was created to collect data from users about their typing patterns for a particular password. When a user types a password, logman logs the keystrokes along with the up-up, up-down and hold key timings and saves it.</p>
<p>The data collected by logman from different users was used to analyze different users and try to differentiate them based on their typing patterns.<p>

<h3>How to use logman</h3>
<p>Well that's pretty straightforward-</p>
<ul>
<li>Clone the logman repository</li>
<li>Fire up your favourite terminal. You can start logman by running the main.py file</li>
<li>After the promt, enter the password you want to store</li>
<li>Continue typing the password to store it in the file. Don't worry if you type it incorrectly. Logman will detect this and prompt you to type it again.</li>
<li>Finally, all your data will be stored in the output.txt and output.csv files in the same directory</li>
</ul>

<h3>Note</h3>
<p>This logger was created for the specific purpose to be used as a part of a larger project. Thus to cater to own customized logging needs, it may be better to use the pyxhook library directly. Logman can provide you with an example of how to use this library.</p>
