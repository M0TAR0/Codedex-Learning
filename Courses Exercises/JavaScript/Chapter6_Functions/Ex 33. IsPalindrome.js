function isPalindrome(word){
    let reversed_word;
    reversed_word = word.split("").reverse().join("");

    if (word.toLowerCase() === reversed_word){
        return true;
    } else {
        return false;
    }

}

console.log(isPalindrome("radar"));
console.log(isPalindrome("noon"));
console.log(isPalindrome("Palabra"));