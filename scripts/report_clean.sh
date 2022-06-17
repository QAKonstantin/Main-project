#!/usr/bin/env bash
find ../allure-results \
\( ! -path "../allure-results/categories.json" ! \
     -path "../allure-results/environment.properties" \) \
-delete