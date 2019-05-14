- Add more functions?
	* Use functions to determine which function to run?
	* Individual functions for each race and class?
		- Create list of abilities, traits, spells, etc.
			* Final function pulls all of these lists together

- Select available books
	* Options
		- PHB (Includes DMG villainous options) -- Always on
		- Volo
		- Xanathar
		- Sword Coast
		- Mordenkainen
	* Display shorthand of what each book gives
		- Classes
		- Races
		- Backgrounds
		- Feats
		- etc.

- Give option of what section to do next, based on available sections
	* Allow players to redo choices
		- Use print() formatting to separate
		- Write code in sections
			* Functions
			* Loops
	* Race and Class both must be done first
		- Prompt confirmation if user changes one of these
			* Prompt for all, but make sure user knows these impact other things
		- Reset Equipment if Class is changed
		- Reset Character Description if Race is changed
	* Allow users to view a completed option's details
	* Allow users to see a summary of what a choice entails
		- e.g. "Race represents the physical form your character has. It impacts base ability score improvements, and adds a few racial traits. Certain feats may be dependant on race."
- Race Choice
	* Display all races
		- Name, subrace options(!), short description, bonuses, abilities
		- Include common variants (Human)
	* When a race is chosen, give detailed information
		- Allow for confirm choice or go back

- Class choice
	* Display all classes
		- Name, short description, abilities, abbreviated proficiencies
	* When a class is chosen, give detailed information
		- Allow for confirm choice or go back

- Ability Score Method
	* Allow option for random rolling
		- Look into robust rolling inputs (input custom method)
	* Allow option for standard array
	* Allow option for specifying custom scores
	* Look into point buy
		- Specify number of points
		- Use standard algorithm
	* Ability Score assignment

- Character Description
	* Prompt for descriptors
	* Make optional

- Equipment
	* Quick loadout
	* Starting gold

- use xlsxWriter to format sheet in excel
	* Like current sheet?
	* https://xlsxwriter.readthedocs.io/
	* https://xlsxwriter.readthedocs.io/example_images.html
	* https://xlsxwriter.readthedocs.io/example_merge1.html

- Eventually add additional excel page with raw data for input
	* Allows for level up function
		- Data Tab in Excel output --> Stores all current values in easy-to-parse format
		- ???
