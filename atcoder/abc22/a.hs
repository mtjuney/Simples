import Data.List
import Control.Monad
import Control.Applicative

main = do
  [n, s, t] <- fmap (read :: String -> Int) . words <$> getLine
  w <- (read :: String -> Int) <$> getLine
  as <- fmap (read :: String -> Int) <$> replicateM (n - 1) getLine
  putStrLn $ show $ (\(_, x) -> x) $ foldl (func (s, t)) (w, if s <= w && w <= t then 1 else 0 ) as


func :: (Int, Int) -> (Int, Int) -> Int -> (Int, Int)
func (s, t) (now_weight, count) updown =
  let new_weight = if now_weight + updown <= 0 then 1 else now_weight + updown
  in
  if s <= new_weight && new_weight <= t
    then (new_weight, count + 1)
    else (new_weight, count)
