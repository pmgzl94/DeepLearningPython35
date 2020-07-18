##
## EPITECH PROJECT, 2020
## cpp
## File description:
## Makefile cpp with Unit tests
##

NAME	=	trade

TU_NAME	=	unit_tests

all:	$(NAME)

$(NAME):

# 	@echo "python3 src/main.py \$${1:*}" > trade ; chmod 700 trade
	# cp -r src/* .
	# mv main.py $(NAME)

tests_run:
	@rm -rf unit_tests; touch unit_tests; echo "#!/bin/env python3" > unit_tests ; cat tests/unitTest.py >> unit_tests; chmod 700 unit_tests

clean:
	rm -rf *.py

fclean:	clean
	rm -rf $(NAME)

re:	fclean all

	# @mv main.py $(TU_NAME)
	# @rsync -av --progress src/* . --exclude src/main.py
	# @rsync -av --progress tests/unitTest.py .
	# @echo "python3 tests/unitTest.py \$${1:*}" > test ; chmod 700 test