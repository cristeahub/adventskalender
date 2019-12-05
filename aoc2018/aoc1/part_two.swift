import Foundation

let path = "input.txt"

do {
  let content = try String(contentsOfFile: path, encoding: String.Encoding.utf8)
  var foundFrequencies = [Int: Int]()
  var counter = 0
  var frequencyRepeatFound = false

  repeat {
    content.enumerateLines { line, stop in
      let value = Int(line)!
      counter += value
      if let _ = foundFrequencies[counter] {
        print("First frequency \(counter)")
        frequencyRepeatFound = true
        stop = true
      }
      foundFrequencies[counter] = 1
    }
  } while(!frequencyRepeatFound)
} catch let error {
  print("Error \(error)")
}
