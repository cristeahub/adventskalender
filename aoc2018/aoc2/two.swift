import Foundation

let path = "input.txt"

func compareLines(_ a: String, _ b: String) -> String? {
  if a.count != b.count {
    return nil
  }

  var oneErrorFound = false

  for (c1, c2) in zip(a, b) {
    if c1 != c2 {
      if oneErrorFound {
        return nil
      }
      oneErrorFound = true
    }
  }

  return String(zip(a, b).filter{ $0 == $1 }.map{ $0.0 })
}


do {
  let content = try String(contentsOfFile: path, encoding: String.Encoding.utf8)
  let lines = content.components(separatedBy: .newlines)

  outer: for i in 0..<lines.count {
    let a = lines[i]

    for j in i+1..<lines.count {
      let b = lines[j]

      if let answer = compareLines(a, b) {
        print("Root string one: \(a)")
        print("Root string two: \(b)")
        print("The correct ID : \(answer)")
        break outer
      }
    }
  }

} catch let error {
  print("Error \(error)")
}
