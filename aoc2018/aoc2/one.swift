import Foundation

let path = "input.txt"

do {
  let content = try String(contentsOfFile: path, encoding: String.Encoding.utf8)
  var numOfTwos = 0
  var numOfThrees = 0


  content.enumerateLines { line, _ in
    var freqs = [Character: Int]()

    for char in line {
      if let count = freqs[char] {
        freqs[char] = count + 1
      } else {
        freqs[char] = 1
      }
    }

    if freqs.values.contains(where: { $0 == 2 }) {
      numOfTwos += 1
    }

    if freqs.values.contains(where: { $0 == 3 }) {
      numOfThrees += 1
    }

  }

  print("Twos: \(numOfTwos)")
  print("Threes: \(numOfThrees)")
  print("Checksum: \(numOfTwos * numOfThrees)")

} catch let error {
  print("Error \(error)")
}
