== OSSEC Web User Interface (wui) ==

=== Download ===

You can download OSSEC wui v0.3 from:

*http://www.ossec.net/files/ui/ossec-wui-0.3.tar.gz

The checksum and gpg signature are also available:

*http://www.ossec.net/files/ui/ossec-wui-0.3-checksum.txt
*http://www.ossec.net/files/ui/ossec-wui-0.3.tar.gz.sig


=== Installation ===

*[[OSSECWUI:Install|Installation Tutorial]]



=== TODO list ===

<br />
'''For PHP Developers interested in helping with the UI''' ([http://www.ossec.net/en/contact.html contact] us for more details) (<font color="red">new!</font>)


List of features/bugs that we plan to add on the next version. 

* [http://www.ossec.net/bugs/show_bug.cgi?id=125 Bug 118] Is it possible to add one link in the main page (next to the agents list) that would search for alll the messages from the selected agent? by <i>Nuno Gomes</i>

* [http://www.ossec.net/bugs/show_bug.cgi?id=125 Bug 119] Support for Firewall logs (reading from logs/firewall/firewall.log). We already started something, but it is incomplete (look at searchfw.php).

* [http://www.ossec.net/bugs/show_bug.cgi?id=125 Bug 120] Add some links for popular options in the stats page, such as last 24 hours, top attacking IP, events by agent, etc.

* [http://www.ossec.net/bugs/show_bug.cgi?id=121 Bug 121] Fix issue where some logs exceeds the width of the table, so visually it runs off the screen.

* [http://www.ossec.net/bugs/show_bug.cgi?id=122 Bug 122] Incorporate some kind of graphing library and maybe PDF exporter for eye candy and management chow (for search results and stats page).

* [http://www.ossec.net/bugs/show_bug.cgi?id=123 Bug 123] Create new "report" page with pre-formatted search options (including today events, this week, yesterday, etc). Such as Today's authentication failures, Today's integrity checking events, etc.

* [http://www.ossec.net/bugs/show_bug.cgi?id=124 Bug 124] Create new page with only the agents information. This could give a better health status of the install.

* [http://www.ossec.net/bugs/show_bug.cgi?id=125 Bug 125] Add a way to mark the events as dealt with would be useful.  There could be something like a 'mark event as.. (closed|follow up|etc)'  If there is a small notes field, the analyst could put in notes such as 'filed abuse report with ISP'. - <i>suggestion by Michael Starks</i>.

* [http://www.ossec.net/bugs/show_bug.cgi?id=126 Bug 126] I'd like to see the source IP linked with useful sites like dshield or a quick way to do a whois on the netblock.  For that matter, maybe filing an abuse report could be made super-simple.  Just click on the IP, select 'file report' and it copies the event to a new mail message addressed to the abuse contact address of the netblock. - <i>suggestion by Michael Starks</i>.

* [http://www.ossec.net/bugs/show_bug.cgi?id=127 Bug 127] On the search screen, having 'level' link to something explaining the levels would be useful.

* [http://www.ossec.net/bugs/show_bug.cgi?id=125 Bug 128] On the search screen, add 'dstip' to compliment 'srcip'.

* [http://www.ossec.net/bugs/show_bug.cgi?id=129 Bug 129] Add option to validate a file change on the integrity checking page. It would also need a search option for all events or only non-validated changes.

* [http://www.ossec.net/bugs/show_bug.cgi?id=130 Bug 130] In the stats tab, show alert breakdowns per agent. <i>suggestion by John Lewis</i>

* [http://www.ossec.net/bugs/show_bug.cgi?id=131 Bug 131] In the stats tab, make results clickable to display the list of alerts referenced in the stat. <i>suggestion by John Lewis</i> 

* [http://www.ossec.net/bugs/show_bug.cgi?id=132 Bug 132] In the stats tab, add a column in the aggregate values by rule table that shows the rule description/summary, so we know what the rules are.  Identifying them by number is less useful. <i>suggestion by John Lewis</i>

* [http://www.ossec.net/bugs/show_bug.cgi?id=133 Bug 133] Would be great to see the alert results in all the pages in a table format with the following columns: date; location; ruleid; rule level; rule description; alert results. Would be cool to allow the columns to be sortable.  I believe this would make it easier to read the alerts.<i>suggestion by John Lewis</i>


