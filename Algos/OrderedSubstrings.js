function subsets(str, results = []) {
    if (str.length === 0) {
      results.push(str);
      return results;
    }
    var arr = str.split("");
    arr.length--;
    var str2 = arr.join("");
    subsets(str2, results);
    var endIndex = results.length;
    for (let i = 0; i < endIndex; i++) {
      results.push(results[i] + str.charAt(str.length - 1));
    }
    return results;
  }

  a="abcdef";
  console.log(subsets(a));