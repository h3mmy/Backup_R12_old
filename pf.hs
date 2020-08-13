#!/usr/bin/env runhaskell
--{-# OPTIONS_GHC -O2 -llvm #-}

-- Importing modules

--import Data.Array
import Data.Array.Unboxed

-- Common sequence generators

    -- Prime number generator (For producing the first few million primes)
primesSA = 2 : prs
  where 
    prs = 3 : sieve prs 3 []
    sieve (p:ps) x fs = [i*2 + x | (i,e) <- assocs a, e] 
                        ++ sieve ps (p*p) fs'
     where
      q     = (p*p-x)`div`2                  
      fs'   = (p,0) : [(s, rem (y-q) s) | (s,y) <- fs]
      a     :: UArray Int Bool
      a     = accumArray (\ b c -> False) True (1,q-1)
                         [(i,()) | (s,y) <- fs, i <- [y+s, y+s+s..q]]

	 -- A sequence of triangular numbers
tris = scanl (+) 1 [2..]

	 -- The Fibonacci series
fibs = 1 : 1 : zipWith (+) fibs (tail fibs)

-- Square root implementation of GNU's multiprecision library

(^!) :: Num a => a -> Int -> a
(^!) x n = x^n
 
squareRoot :: Integer -> Integer
squareRoot 0 = 0
squareRoot 1 = 1
squareRoot n =
   let twopows = iterate (^!2) 2
       (lowerRoot, lowerN) =
          last $ takeWhile ((n>=) . snd) $ zip (1:twopows) twopows
       newtonStep x = div (x + div n x) 2
       iters = iterate newtonStep (squareRoot (div n lowerN) * lowerRoot)
       isRoot r  =  r^!2 <= n && n < (r+1)^!2
   in  head $ dropWhile (not . isRoot) iters
   
-- Factorial 

factorial :: (Num a, Eq a) => a -> a
factorial 0 = 1
factorial n = n * factorial (n-1)


-- Prime factorization attempt

factor 1 = []
factor n = let divisors = dropWhile ((/= 0) . mod n) [2 .. ceiling $ sqrt $ fromIntegral n]
           in let prime = if null divisors then n else head divisors
              in (prime :) $ factor $ div n prime
