#!/usr/bin/env runhaskell

import Data.Char

f n = tail $ show n
g q = read (f q) :: Integer
h t = if 29*(g t) == t then Just t else Nothing

a = [x|x<-[10..], h x /= Nothing] 

main = do
	print $ head a
