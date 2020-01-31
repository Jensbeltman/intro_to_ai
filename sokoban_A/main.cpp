#include "types_and_mapping.hpp"
#include <array>
#include <boost/algorithm/string.hpp>
#include <boost/unordered_set.hpp>
#include <chrono> // for high_resolution_clock
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

struct Board {
    Table sData, dData;
    int px, py;
    int maxOpenListSize;
    double total_time;
    int jewels = 0;

    Board(string b) {
        vector<string> data;
        boost::split(data, b, boost::is_any_of("\n"));

        size_t width = 0;
        for (auto &row : data)
            width = max(width, row.size());

        map<char, char>
                maps = {{' ', ' '},
                        {'.', '.'},
                        {'@', ' '},
                        {'#', '#'},
                        {'$', ' '}},
                mapd = {{' ', ' '},
                        {'.', ' '},
                        {'@', '@'},
                        {'#', ' '},
                        {'$', '*'}};

        for (size_t r = 0; r < data.size(); r++) {
            TableRow sTemp, dTemp;
            for (size_t c = 0; c < width; c++) {
                char ch = c < data[r].size() ? data[r][c] : ' ';
                if (ch == '$')
                    jewels++;
                sTemp.push_back(maps[ch]);
                dTemp.push_back(mapd[ch]);
                if (ch == '@') {
                    px = c;
                    py = r;
                }
            }
            sData.push_back(sTemp);
            dData.push_back(dTemp);
        }
    }

    bool move(int x, int y, int dx, int dy, Table &data) {
        if (sData[y + dy][x + dx] == '#' || data[y + dy][x + dx] != ' ')
            return false;

        data[y][x] = ' ';
        data[y + dy][x + dx] = '@';
        return true;
    }

    bool push(int x, int y, int dx, int dy, Table &data) {
        if (sData[y + 2 * dy][x + 2 * dx] == '#' ||
            data[y + 2 * dy][x + 2 * dx] != ' ')
            return false;

        data[y][x] = ' ';
        data[y + dy][x + dx] = '@';
        data[y + 2 * dy][x + 2 * dx] = '*';
        return true;
    }

    bool isSolved(const Table &data) {
        for (size_t r = 0; r < data.size(); r++)
            for (size_t c = 0; c < data[r].size(); c++)
                if ((sData[r][c] == '.') != (data[r][c] == '*'))
                    return false;
        return true;
    }

    string solve() {
        boost::unordered_set<Table, boost::hash<Table>> visited;
        visited.insert(dData);

        multiset<SAH, heuristic_compare> open;
        open.insert(make_tuple(dData, "", px, py, 0));

        vector<tuple<int, int, char, char>> dirs = {
                make_tuple(0, -1, 'u', 'U'), make_tuple(1, 0, 'r', 'R'),
                make_tuple(0, 1, 'd', 'D'), make_tuple(-1, 0, 'l', 'L')};

        map<MoveChange, double, move_change_comp> maph = get_maph();

        while (open.size() > 0) {
            auto open_it_begin = open.begin();

            Table temp, cur = get<0>(*open_it_begin);
            string cSol = get<1>(*open_it_begin);
            char pMove;
            double h = get<4>(*open_it_begin); // heuristic
            int x = get<2>(*open_it_begin);
            int y = get<3>(*open_it_begin);

            if (cSol.empty()) {
                pMove = 'u';
            } else {
                pMove = cSol.back();
            }

            open.erase(open_it_begin);

            for (int i = 0; i < 4; ++i) {
                temp = cur;
                int dx = get<0>(dirs[i]);
                int dy = get<1>(dirs[i]);
                try { maph.at(MoveChange(pMove, get<3>(dirs[i])));} catch (const std::out_of_range& e) {cout<<"No map match found !!"<<endl; }

                if (temp[y + dy][x + dx] == '*') {
                    if (push(x, y, dx, dy, temp) && visited.find(temp) == visited.end()) {
                        if (isSolved(temp)) {
                            maxOpenListSize = open.size();
                            total_time = h + maph[MoveChange(pMove, get<3>(dirs[i]))];
                            return cSol + get<3>(dirs[i]);
                        }
                        open.insert(
                                make_tuple(temp, cSol + get<3>(dirs[i]), x + dx, y + dy,
                                           h + maph[MoveChange(pMove, get<3>(dirs[i]))]));
                        visited.insert(temp);
                    }
                } else if (move(x, y, dx, dy, temp) &&
                           visited.find(temp) == visited.end()) {
                    if (isSolved(temp)) {
                        maxOpenListSize = open.size();
                        total_time = h + maph[MoveChange(pMove, get<2>(dirs[i]))];
                        return cSol + get<2>(dirs[i]);
                    }
                    open.insert(make_tuple(temp, cSol + get<2>(dirs[i]), x + dx, y + dy,
                                           h + maph[MoveChange(pMove, get<2>(dirs[i]))]));
                    visited.insert(temp);
                }
            }
        }
        return "No solution";
    }
};

int main() {
    string level;
    std::ifstream infile("/home/jens/AI/sokoban_bfs/levels.txt");
    std::ofstream outfile("/home/jens/AI/sokoban_A/testing.csv");
    std::string line;

    while (std::getline(infile, line)) {
        std::istringstream iss(line);
        if (line.size() > 2) {
            level.append(iss.str() + '\n');
        } else {

            // Record start time
            auto start = std::chrono::high_resolution_clock::now();

            cout << level << endl << endl;
            Board board(level);
            string moves = board.solve();
            std::cout << moves << std::endl;

            // Record end time
            auto finish = std::chrono::high_resolution_clock::now();

            std::chrono::duration<double> elapsed = finish - start;
            std::cout << "Elapsed time: " << elapsed.count() << " s\n";
            std::cout << "Open-list size: " << board.maxOpenListSize << " \n";
            std::cout << "Number of jewels: " << board.jewels << " \n";
            std::cout << "Number of moves: " << moves.size() << " \n";
            std::cout << "Actual solution time: " << board.total_time << " s\n";
            outfile << board.jewels << "," << moves.size() << ","
                    << board.maxOpenListSize << "," << elapsed.count() << "\n";

            level.clear();
        }
    }
    outfile.close();
    return 0;
}
