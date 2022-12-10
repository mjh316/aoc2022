puts (($<.read.strip.split"\n\n").map {|l| (l.split"\n").inject{ |s,n| s.to_i + n.to_i}}).map(&:to_i).sort.slice(-3,3).sum
