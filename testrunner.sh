#!/bin/bash

cd tests/todo/api

echo "Running All Tests in tests/api"

pytest -q get_new_year_eve_options.py
pytest -q post_selected_new_year_eve_option.py
pytest -q get_funny_content_for_selected_new_year_eve_option.py
