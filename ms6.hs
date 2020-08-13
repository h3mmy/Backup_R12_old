a = map (+24) $ map (6*) [1..]
b = map (+20) $ map (10*) [1..]
c = map (14*) [1..]

c_a = map (20-) $ map (4*) [1..]
b_a = map (4-) $ map (4*) [1..]

main = do
	print $ take 40 a
	print $ take 40 b
	print $ take 40 c
	print $ take 40 c_a
	print $ take 40 b_a