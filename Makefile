install:
	chmod +x ln_plus.py prepare_build.py
	./ln_plus.py --from /usr/local/bin --to ln_plus.py
	./ln_plus.py --from /usr/local/bin --to prepare_build.py
