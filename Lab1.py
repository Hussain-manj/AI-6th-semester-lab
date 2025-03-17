# We use hash for comments in Python

# This is how we show an output string
print ( "Hello Guys, I'm New Here" )

# This is how we show any number as an output
print ( 100 )

# Variable Declaration
a = 10
b = 3.35
c = 2e-2
d = 10E3
e = 1 + 2j
f = 5 + 3J
g = "okay."
h = "It's said "
i = '"Dream Big and Dare to Fail!"'
j = True


print ( a, b, c, d, e, f, g, "\t", h+i, j )

# Datatype Checking Function
print ( type ( a ) )
print ( type ( b ) )
print ( type ( c ) )
print ( type ( d ) )
print ( type ( e ) )
print ( type ( f ) )
print ( type ( g ) )
print ( type ( h ) )
print ( type ( i ) )
print ( type ( j ), "\n" )

# TypeCasting
w = complex ( 8, 5 ) 
x = str ( 100 )
y = int ( 100 )
z = float ( 100 )

print ( w )
print ( x )
print ( y )
print ( z )

print ( type ( w ) ) 
print ( type ( x ) )
print ( type ( y ) )
print ( type ( z ) )

# Two Statements in same line
print ( w ) ; print ( x )

# String indices and accessing
string1 = "FAHAD GULZAR"

print ( string1 )

# String indices
print ( string1[0] )
print ( string1[-12] )

# String slicing
print ( string1[ 1 : 5 ] )
print ( string1[ 6 : ] )
print ( string1[ : 6 ] )

# List
list1 = [ "List", 12, True ]

print ( list1 )

# List indices
print ( list1[0] )

print ( type ( list1[0] ) )
print ( type ( list1[1] ) )
print ( type ( list1[-1] ) )

# List slicing
print ( list1[ 0: 1 ] )
print ( list1[ 0 : 2 ] )
