import Foundation

let path = "input.txt"

do {
  let content = try String(contentsOfFile: path, encoding: String.Encoding.utf8)
  var counter = 0
  content.enumerateLines { line, _ in
    let value = Int(line)!
    counter += value
  }
  print(counter)
} catch let error {
  print("Error \(error)")
}
