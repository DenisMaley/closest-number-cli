NUM=3
SAMPLES=1000000

install:
	docker build -t closest-number .

strategy:
	docker run --rm -it closest-number optimal-strategy -n $(NUM)

proof:
	docker run --rm -it closest-number proof -n $(NUM) -s $(SAMPLES)