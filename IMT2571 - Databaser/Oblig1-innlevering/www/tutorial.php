<?php 

/**
    
    forelesning tirsdag U35 30.08.16

    VIKTIG at all kommunikasjon mot database skjer ved try-catch exception handling.
*/


function add($a, $b){

    print($a + $b);
}

add(2, 3.1);
print("\n");
add(2, 3);
print("\n");
add(2, '3M');
print("\n");
add(2, 'M');



function validateAge($age){

    // is_int checks whether var is int or not, pretty self-explanatory
    if(!is_int($age)){

        // IllegalArgumentException ???
        // http://php.net/manual/en/class.invalidargumentexception.php

        throw new InvalidArgumentException("$age"
            ."validateAge: age must be an int,"
            .   " was: '$age'");
        }
    }

$age = '10';

try{
    validateAge($age);
    // Exception superclass håndterer alle exceptions
} catch (InvalidArgumentException $e){
    //$message = $e.getMessage();
    echo "\$Age: $age har feil verdi, må være int";
}

?>
<style> 

    #woho {
        text-align: center;
        font-size: 20px;
    }

    #navnholder {
        text-align: center;
        color: red;
        font-size: 30px;
    }
</style>

<?php


class Person {

    var $pNr = -1;
    var $fornavn = null;
    var $etternavn = null;

    function __construct($pNr, $fornavn, $etternavn){

        $this->pNr = $pNr;
        $this->fornavn = $fornavn; 
        $this->etternavn = $etternavn;
    }
}

$per = new Person('1', 'Per', 'Testerson');

echo '</br><p id="navnholder">navn:' . $per->fornavn . ' ' . $per->etternavn . '</p></br>';


for ($i = 3; $i <= 50; $i++){
    for ($j = 2; $j < $i/2; $j++){
        if($i % $j == 0){
            echo '<p id="woho"> '.$i.' / '.$j.' = ' . $i / $j . '</br>';
        }
    }
}

?>