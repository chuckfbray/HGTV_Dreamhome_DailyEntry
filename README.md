# HGTV_Dreamhome_DailyEntry
/// Purpose ///
A program that quickly passes your personal details to HGTV's (and sister site Food Network's) sweepstakes entry pages and submits them.

/// Language(s) [packages] ///
Python [Selenium, time]

/// Methods ///
Open a headless Chrome browser with Selenium webdriver, then enter the user's email into the landing page form, taking the browser to the form submission page where further personal details are entered before submitting the user's entry for the day.

/// Notes ///
Program will NOT work multiple times a day with the same personal identifying information, as an individual's entries are limited to once a day.
