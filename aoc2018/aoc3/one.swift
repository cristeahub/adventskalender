import Foundation

let path = "input.txt"

do {
  let content = try String(contentsOfFile: path, encoding: String.Encoding.utf8)

  var claimsData = [[Int]]()

  content.enumerateLines { line, _ in
    claimsData.append(
      line.components(separatedBy: ["#", "@", ",", ":", "x"])
        .filter { !$0.isEmpty  }
        .map { Int($0.trimmingCharacters(in: .whitespaces))! }
    )
  }

  var claimsMap = [String: [Int]]()
  var overlappingMap = [Int: [Int]]()

  for claim in claimsData {
    let num = claim[0]
    let xPos = claim[1]
    let yPos = claim[2]
    let width = claim[3]
    let height = claim[4]

    for i in xPos..<xPos + width {
      for j in yPos..<yPos + height {
        if var claimObject = claimsMap["\(i), \(j)"] {
          for number in claimsMap["\(i), \(j)"]! {
            if var x = overlappingMap[number] {
              x.append(num)
            } else {
              overlappingMap[number] = [num]
            }
            if var x = overlappingMap[num] {
              x.append(number)
            } else {
              overlappingMap[num] = [number]
            }
          }
          claimObject.append(num)
        } else {
          claimsMap["\(i), \(j)"] = [num]
        }
      }
    }
  }

  print("One ", claimsMap.filter { $0.value.count > 1 }.count)
  print("Two ", overlappingMap.filter { $0.value.count == 0 }.0)

} catch let error {
  print("Error \(error)")
}
