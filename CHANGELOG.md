# Changelog


## (unreleased)

### Other

* Ci: Add git change log. [Christopher Burgess]


## 0.2.3 (2019-11-19)

### Other

* Chore: pyproject typo. [Christopher Burgess]

* Ci: Add poetry pyproject.toml. [Christopher Burgess]


## 0.2.2 (2019-11-19)

### Fix

* Call API in parallel. [Christopher Burgess]

### Other

* Perf: Call the API in parallel. [Christopher Burgess]

* Perf: Call API in parallel (#44) [Kit Burgess]

  perf: Call API in parallel

* Style: Implement recommendations from @cvonsteg. [Christopher Burgess]

* Test: Remove speed test. [Christopher Burgess]

* Style: Enable pre commit hook. [Christopher Burgess]

* Perf: Limit threads to 5. [Christopher Burgess]

* Perf: Call API using multithreading. [Christopher Burgess]

* Perf: Convert cargo movements to dataframe in parallel. [Christopher Burgess]


## 0.2.1 (2019-11-18)

### Fix

* Search pages correctly. [Christopher Burgess]

* Return all vessels from search, not just arbitrary 100 (#41) [Kit Burgess]

  fix: Return all vessels from search, not just arbitrary 100

* Serialize vessels to list in parallel. [Christopher Burgess]

### Other

* Ci: Reformat setup.cfg. [Christopher Burgess]

* Ci: Put flake config in setup.cfg so that pep8speaks can read it @cvonsteg. [Christopher Burgess]

* Style: Remove status token from README (#32) [Kit Burgess]

  style: Remove status token from README

* Style: Remove status token from README. [Christopher Burgess]

* Products endpoint test (#11) [Kit Burgess]

  Products endpoint test

* Merge branch 'master' into products_endpoint_test. [Kit Burgess]

* Update vortexasdk/endpoints/products.py. [Kit Burgess]

* Test: add test_products_real test for products endpoint. [dstarkey23]

* Test: Use original vessers.json. [Christopher Burgess]

* Merge branch 'master' into products_endpoint_test. [Kit Burgess]

* Test: generate product stubs. [dstarkey23]

* Update documentation and tests to product endpoint. [dstarkey23]

* Add product_parent to product search params. Bug fix import statement. [dstarkey23]

* Why no Search feature in products.py? tests/products no longer works. [dstarkey23]

* Fix merge conflicts endpoints products. [dstarkey23]

* Fix merge conflicts endpoints products. [dstarkey23]

* Add test_products test case to tests/endpoints. [dstarkey23]

* Add products endpoint. [dstarkey23]

* Merge branch 'master' into products_endpoint_test. [dstarkey23]

* Write test_products script in tests/endpoints (in progress) [dstarkey23]

* Add products.py to endpoints. [dstarkey23]


## 0.2.0 (2019-11-18)

### Feat

* Bump version to 0.2.0. [Christopher Burgess]

* Convert IDs to names. [Christopher Burgess]

* Allow filtering cargo movements using entity name. [Christopher Burgess]

* Allow user to search cargo movements with single filter, fi… (#21) [Kit Burgess]

  feat: Allow user to search cargo movements with single filter, fixes #16

* Allow user to search cargo movements with single filter, fixes #16. [Christopher Burgess]

### Other

* Filter on name (#27) [Kit Burgess]

  Filter on name

* Update tests/test_id.py. [syed]

* Merge remote-tracking branch 'origin/master' into filter-on-name. [Christopher Burgess]

* Merge pull request #28 from V0RT3X4/global-client. [Kit Burgess]

  test: Fix global client state

* Test: Fix global client state. [Christopher Burgess]

* Refactor: Move private methods to appropriate module. [Christopher Burgess]

* Merge pull request #26 from V0RT3X4/live-ci-tests. [Kit Burgess]

  Run tests against live API in circle ci

* Ci: Verbose nose2 logging. [Christopher Burgess]

* Ci: Run all tests, including live API. [Christopher Burgess]

* Merge branch 'master' into live-ci-tests. [Kit Burgess]

* Revert "ci: Run live tests in circleci" (#24) [Kit Burgess]

  Revert "ci: Run live tests in circleci"

* Revert "ci: Run live tests in circleci" [Kit Burgess]

* Merge pull request #22 from V0RT3X4/live-ci-tests. [Kit Burgess]

  ci: Run live tests in circleci

* Chore: Log the client when it's set. [Christopher Burgess]

* Merge branch 'master' into live-ci-tests. [Kit Burgess]

* Test: Correctly set client in tests (#23) [Kit Burgess]

  test: Correctly set client in tests

* Test: Correctly set client in tests. [Christopher Burgess]

* Update .circleci/config.yml. [Kit Burgess]

* Merge branch 'master' into live-ci-tests. [Kit Burgess]

* Chore: Missing comma. [Christopher Burgess]

* Docs: Add setting api key to contributing guide. [Christopher Burgess]

* Ci: Add tabulate to setup.py. [Christopher Burgess]

* Ci: Run live tests in circleci. [Christopher Burgess]

* Ci: Integrate git release tag with pip version. [Christopher Burgess]


## 0.1.0 (2019-11-13)

### Feat

* Add Node reference return objects. [Christopher Burgess]

* Filter cargo movement columns. [Christopher Burgess]

* Filter cargo movement columns. [Christopher Burgess]

* Serialize CargoMovementEntity. [Christopher Burgess]

* Read vessels as dataframe. [Christopher Burgess]

* Autogenerate python docs examples. [Christopher Burgess]

* Add paging. [Christopher Burgess]

* Call cargo movements api. [Christopher Burgess]

* We can now search on geographies. [Christopher Burgess]

* Complete the get reference. [Christopher Burgess]

* Add corporate entity. [Christopher Burgess]

* Add ProductLayer enum. [Christopher Burgess]

* Add maiden and final voyages. [Christopher Burgess]

* Compare US to asia average journey times. [Christopher Burgess]

* Sample notebook now finds number of clean -> dirty swaps by day. [Christopher Burgess]

* Add initial sample notebook. [Christopher Burgess]

### Other

* Merge pull request #15 from V0RT3X4/add-manifest. [Kit Burgess]

  ci: Add export packages

* Ci: Add export packages. [Christopher Burgess]

* Docs: Add tips to contributing docs (#13) [Kit Burgess]

  docs: Add tips to contributing docs

* Merge branch 'master' into tips. [Kit Burgess]

* Refactor: Rename root dir from vortexa to vortexasdk (#12) [Kit Burgess]

  refactor: Rename root dir from vortexa to vortexasdk

* Chore: Use correct email address. [Christopher Burgess]

* Refactor: Rename root dir from vortexa to vortexasdk. [Christopher Burgess]

* Docs: Add tips to contributing docs. [Christopher Burgess]

* Refactor: Allow clients to import classes without knowledge of int… (#8) [Kit Burgess]

  refactor: Allow clients to import classes without knowledge of internals

* Merge branch 'master' into blind-imports. [Kit Burgess]

* Docs: Improve the contributing guide (#9) [Kit Burgess]

  docs: Improve the contributing guide

* Ci: Install the new way. [Christopher Burgess]

* Docs: Correctly install dependencies. [Christopher Burgess]

* Chore: Add git clone to docs. [Christopher Burgess]

* Chore: Reorder the documentation page. [Christopher Burgess]

* Docs: Improve the contributing guide. [Christopher Burgess]

* Style: Implement feedback from @cvonsteg. [Christopher Burgess]

* Refactor: Allow clients to import classes without knowledge of internals. [Christopher Burgess]

* Merge pull request #3 from V0RT3X4/vessels-cleanup. [Kit Burgess]

  test: Vessel dataframe test actually does something

* Merge branch 'master' into vessels-cleanup. [Kit Burgess]

* Merge pull request #5 from V0RT3X4/quickstart. [Kit Burgess]

  docs: Add quickstart to docs

* Docs: Add quickstart to docs. [Christopher Burgess]

* Chore: Merge master. [Christopher Burgess]

* Merge pull request #4 from V0RT3X4/pipping. [Kit Burgess]

  ci: Create the setup.py file

* Test: Move installs to setup.extras_require. [Christopher Burgess]

* Chore: Rename test package to tests. [Christopher Burgess]

* Chore: Fix install versions. [Christopher Burgess]

* Chore: Tinker with setup.py. [Christopher Burgess]

* Ci: Create the setup.py file. [Christopher Burgess]

* Refactor: Move test to correct place. [Christopher Burgess]

* Merge remote-tracking branch 'origin/master' into vessels-cleanup. [Christopher Burgess]

* Style: Enable pydocstyle precommit hook. [Christopher Burgess]

* Merge remote-tracking branch 'origin/master' into vessels-cleanup. [Christopher Burgess]

* Ci: Circleci uses write deploy key. [Christopher Burgess]

* Test: Add setup method to vessels test. [Christopher Burgess]

* Docs: Cleanup docs. [Christopher Burgess]

* Test: Vessel dataframe test actually does something. [Christopher Burgess]

* Consistent types (#2) [Kit Burgess]

  Consistent types

* Docs: Only build docs in non-master branch. [Christopher Burgess]

* Docs: Rename Charterer to Corporate. [Christopher Burgess]

* Chore: Install pydoc-markdown. [Christopher Burgess]

* Ci: Generate docs on any branch, only deploy on master. [Christopher Burgess]

* Test: Correctly annotate live cargo movement tests. [Christopher Burgess]

* Docs: Include docs for all entities. [Christopher Burgess]

* Ci: Don't run tests against real endpoint. [Christopher Burgess]

* Test: Mock API client. [Christopher Burgess]

* Test: Add autogenerated test examples. [Christopher Burgess]

* Refactor: Introduce some type consistency. [Christopher Burgess]

* Refactor: Replace python_sdk with vortexa. [Christopher Burgess]

* Docs: Don't ignore docs. [Christopher Burgess]

* Ci: CircleCi deploys to github pages. [Christopher Burgess]

* Chore: Remove unecessary files. [Christopher Burgess]

* Docs: Add contributing guide. [Christopher Burgess]

* Docs: Add code of conduct. [Christopher Burgess]

* Docs: Add china example. [Christopher Burgess]

* Refactor: Reduce duplication when creating params. [Christopher Burgess]

* Chore: Start to explore extracting dict items. [Christopher Burgess]

* Docs: Show endpoints in docsite. [Christopher Burgess]

* Refactor: Remove unused pyproject.toml. [Christopher Burgess]

* Refactor: Move endpoint callers into endpoints package. [Christopher Burgess]

* Docs: Document vessel endpoint. [Christopher Burgess]

* Create LICENSE. [Kit Burgess]

* Docs: Document Entities. [Christopher Burgess]

* Test: Add CargoEventEntity tests. [Christopher Burgess]

* Docs: Add vessels documentation with pandas example. [Christopher Burgess]

* Chore: Add a second demo example. [Christopher Burgess]

* Refactor: Move tests to test package. [Christopher Burgess]

* Docs: Use keras inspired docs. [Christopher Burgess]

* Docs: Add documentation for Search and Reference classes. [Christopher Burgess]

* Style: Experiment using portray and pydocmd. [Christopher Burgess]

* Chore: Re-enable flake. [Christopher Burgess]

* Ci: Add circle ci status badge token. [Christopher Burgess]

* Ci: Add circleci status badge. [Christopher Burgess]

* Ci: Import jsons. [Christopher Burgess]

* Ci: Add circle ci config. [Christopher Burgess]

* Refactor: Remove redundant file. [Christopher Burgess]

* Test: Write ProductEntity serialization test. [Christopher Burgess]

* Style: Add favicon. [Christopher Burgess]

* Docs: Start to use portray to generate docs. [Christopher Burgess]

* Docs: Add mkdocs template. [Christopher Burgess]

* Chore: Add versions to requirements.txt. [Christopher Burgess]

* Initial commit. [Kit Burgess]


