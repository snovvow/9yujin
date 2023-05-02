const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [A, B] = input.shift().split(" ").map(Number);
const [N, M] = input.shift().split(" ").map(Number);
let robots = input
  .splice(0, N)
  .map((v) => v.split(" ").map((m, i) => (i !== 2 ? Number(m) : m)));
const commands = input.map((v) =>
  v.split(" ").map((m, i) => (i !== 1 ? Number(m) : m))
);

// NWES a:가로 - b:세로
const da = [0, -1, 0, 1];
const db = [-1, 0, 1, 0];
const direction = ["N", "W", "S", "E"];

//LRF 로직
const commandFunc = {
  L: (robot) => {
    const cur = direction.findIndex((v) => v == robots[robot][2]);
    robots[robot][2] = direction[(cur + 1) % 4];
  },
  R: (robot) => {
    const cur = direction.findIndex((v) => v == robots[robot][2]);
    robots[robot][2] = direction[(cur + 3) % 4];
  },
  F: (robot) => {
    const cur = direction.findIndex((v) => v == robots[robot][2]);
    robots[robot][0] += da[cur];
    robots[robot][1] += db[cur];
  },
};

const checkCrashWall = (robot) => {
  if (
    robots[robot][0] < 1 ||
    robots[robot][0] > A ||
    robots[robot][1] < 1 ||
    robots[robot][1] > B
  ) {
    console.log(`Robot ${robot + 1} crashes into the wall`);
    process.exit();
  }
};

const checkCrashRobot = (robot) => {
  robots.forEach((v, i) => {
    if (i !== robot) {
      if (v[0] === robots[robot][0] && v[1] === robots[robot][1]) {
        console.log(`Robot ${robot + 1} crashes into robot ${i + 1}`);
        process.exit();
      }
    }
  });
};

commands.forEach(([robot, command, count]) => {
  for (let i = 0; i < count; i++) {
    commandFunc[command](robot - 1);
    checkCrashWall(robot - 1);
    checkCrashRobot(robot - 1);
  }
});
console.log("OK");
