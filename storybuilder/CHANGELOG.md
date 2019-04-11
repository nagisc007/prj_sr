# ChangeLog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2019-04-10
### Added
- new Base Action
- new Base Subject
- Subject class for basic all subject
### Changed
- StoryDB to Master
- All tests with new Action and Subject
### Deleted
- Behavior
- BehavType
- old Person class (have many attr)

## [0.0.9] - 2019-04-08
### Added
- Characters count
- Insert break line
- Break symbol
- Combine description
- Dialogue mode in description
- Replaced calling tag in description
### Changed
- Omit description using a priority
### Fixed
- (Kakko, Hatena) and Maru bug
- Combine bug (vanish or each inserted break line)

## [0.0.8] - 2019-04-05
### Added
- Utility functions(assertion, print test title)
- Omit description
- Story title(episode title) inserted break line before
- Description shorter typing
### Changed
- Class and function arg type check using custom assertion
- Multi calling attribute
### Fixed
- No use comma when after symbol
- Coverage check
- Behavior REPLY lacking

## [0.0.7] - 2019-04-02
### Added
- StoryDB
- Info, Nothing
- AuxVerb
- Converted objects
- Multi object at an action
### Changed
- Refined Action
- Assertion for object types

## [0.0.6] - 2019-03-25
### Added
- New action group (scene, combi)
- negative mode
- action flags and deflags
### Changed
- output an action format
### Fixed
- error message without an action info
- error message without an object name

## [0.0.5] - 2019-03-19
### Added
- Word class
- Action's object param
- Behavior type
- Many new attribute words to Person class
- Passive mode to Action
- Language type
### Changed
- Outline test using Action
### Fixed
- Top space with a description
- Exchanged commandline action flags

## [0.0.4] - 2019-03-19
### Added
- ActionGroup class
- Master class (inherited Subject class)
### Changed
- Action class < Act class
- Story management as ActionGroup
### Deleted
- Story class
- Episode class
- Scene class

## [0.0.3] - 2019-03-18
### Added
- Github issue template
- Github pull request template
- BaseAction class
- Story class
- Episode class
- Scene class
- story building method
- option parser
- output as action infos
### Changed
- Act's verb without a particle
### Fixed
- Failed to equal sentences in testtools

## [0.0.2] - 2019-03-11
### Added
- Act class to add a new attr "behavior"
- Behavior enum types (from major english verbs)
- Subject class for using act's subject base
### Changed
- Person, Stage, Item and DayTime class based Subject
- Story check test completely 5w1h.
### Deleted
- Example story and test.
- ActType(MUST, DONE)
- Must and Done act (instead to an act behavior).

## [0.0.1] - 2019-03-08
### Added
- This CHANGELOG file to hopefully serve as an evolving example of a standardized open source project CHANGELOG.
- README one line implemented.
- Basic classes to build a story.
- Test suites for basic features.
- Example story as usage.
- Output story as markdown.

[Unreleased]: https://github.com/nagisc007/storybuilder/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/nagisc007/storybuilder/releases/v0.1.0
[0.0.9]: https://github.com/nagisc007/storybuilder/releases/v0.0.9
[0.0.8]: https://github.com/nagisc007/storybuilder/releases/v0.0.8
[0.0.7]: https://github.com/nagisc007/storybuilder/releases/v0.0.7
[0.0.6]: https://github.com/nagisc007/storybuilder/releases/v0.0.6
[0.0.5]: https://github.com/nagisc007/storybuilder/releases/v0.0.5
[0.0.4]: https://github.com/nagisc007/storybuilder/releases/v0.0.4
[0.0.3]: https://github.com/nagisc007/storybuilder/releases/v0.0.3
[0.0.2]: https://github.com/nagisc007/storybuilder/releases/v0.0.2
[0.0.1]: https://github.com/nagisc007/storybuilder/releases/v0.0.1
