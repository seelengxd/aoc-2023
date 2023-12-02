import * as fs from "fs";
const data = fs.readFileSync("./day02.in", "utf-8");
const games = data.split("\n");

type Color = "red" | "blue" | "green";
type ColorTuple = [string, Color];
type Data = ColorTuple[][];

let ans1 = 0;
let ans2 = 0;
for (const [index, game] of games.entries()) {
  const gameData: Data = game
    .split(":")[1]
    ?.split(";")
    ?.map((str) => str.split(","))
    .map((strArr) =>
      strArr.map((str) => {
        const [value, color] = str.trim().split(" ");
        return [value, color as Color] as ColorTuple;
      })
    );
  if (!gameData) {
    continue;
  }
  const counter: { [key in Color]: number } = { red: 0, green: 0, blue: 0 };
  for (const row of gameData) {
    for (const [value, color] of row) {
      counter[color] = Math.max(counter[color], parseInt(value, 10));
    }
  }

  if (counter["red"] <= 12 && counter["green"] <= 13 && counter["blue"] <= 14) {
    ans1 += index + 1;
  }
  ans2 += Object.values(counter).reduce((i, j) => i * j);
}

console.log(ans1);
console.log(ans2);
