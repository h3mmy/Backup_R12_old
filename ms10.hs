#!/usr/bin/env runhaskell

import Data.List (nub)

d = [1..9999]

f x = if (length $ nub $ show x) <= 2 then True else False

main = do
	print $ length $ filter f d 
