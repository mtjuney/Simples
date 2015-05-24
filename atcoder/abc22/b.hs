import Control.Monad
import Control.Applicative hiding (empty)
import Data.Set hiding (foldl)

main = do
  n <- (read :: String -> Int) <$> getLine
  as <- replicateM n readLn

  print $ (\(_, x) -> x) $ foldl func (empty, 0) (as::[Int])


func :: (Set Int, Int) -> Int -> (Set Int, Int)
func (xs, count) x = if member x xs then (xs, count + 1) else (insert x xs, count)
