function validIPAddress(queryIP: string): string {
  // Validate IPv4
  if (queryIP.split(".").length === 4) {
    return validateIPv4(queryIP) ? "IPv4" : "Neither";
  }

  // Validate IPv6
  if (queryIP.split(":").length === 8) {
    return validateIPv6(queryIP) ? "IPv6" : "Neither";
  }
  return "Neither";
}

function validateIPv4(ip: string): boolean {
  const ipArr = ip.split(".");
  for (let i = 0; i < ipArr.length; i++) {
    const num = parseInt(ipArr[i]);
    if (num < 0 || num > 255 || num.toString() !== ipArr[i]) {
      return false;
    }
  }
  return true;
}

function validateIPv6(ip: string): boolean {
  const ipArr = ip.split(":");
  // Maximum for each block is 4 characters, FFFF is the maximum, so 65535
  for (let i = 0; i < ipArr.length; i++) {
    // only digits, letters a-f, A-F
    for (let j = 0; j < ipArr[i].length; j++) {
      if (
        (ipArr[i][j] < "0" || ipArr[i][j] > "9") &&
        (ipArr[i][j] < "a" || ipArr[i][j] > "f") &&
        (ipArr[i][j] < "A" || ipArr[i][j] > "F")
      ) {
        return false;
      }
    }

    const num = parseInt(ipArr[i], 16);
    if (
      ipArr[i].length === 0 ||
      ipArr[i].length > 4 ||
      num < 0 ||
      num > 65535 ||
      num.toString(16) !== ipArr[i].toLowerCase()
    ) {
      return false;
    }
  }
  return true;
}
