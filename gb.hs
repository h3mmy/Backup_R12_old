#!/usr/bin/env runhaskell

{-# OPTIONS_GHC -O2 -llvm #-}


import Data.Array.Unboxed


primesSA = 2 : prs
  where 
    prs = 3 : sieve prs 3 []
    sieve (p:ps) x fs = [i*2 + x | (i,e) <- assocs a, e] 
                        ++ sieve ps (p*p) fs'
     where
      q     = (p*p-x)`div`2                  
      fs'   = (p,0) : [(s, rem (y-q) s) | (s,y) <- fs]
      a     :: UArray Int Bool                                   -- Using Unboxed Array module
      a     = accumArray (\ b c -> False) True (1,q-1)
                         [(i,()) | (s,y) <- fs, i <- [y+s, y+s+s..q]]

d = takeWhile (<5000) $ tail primesSA

r = [(show x, show y) | x <- d, y <- d, x<y]

f n = x/y where
	 x = read (fst n) :: Float
	 y = read (snd n) :: Float

rt = map f r

main = do
	print $ sum rt / (read (show $ length rt) :: Float)