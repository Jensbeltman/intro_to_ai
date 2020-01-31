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

#define fA 1.4083196699619294
#define bA 4.057445287704468
#define lA 2.8050299286842346
#define rA 2.340702384710312
#define pA 2.5883273945914373

#define fpA (pA + fA)
#define rpA (pA + rA)
#define lpA (pA + lA)

using namespace std;

typedef vector<char> TableRow;
typedef vector<TableRow> Table;
typedef tuple<Table, string, int, int, double> SAH; // state and heuristic
typedef pair<char, char> MoveChange; // state and heuristic

struct heuristic_compare {
  bool operator()(const SAH a, const SAH b) const {
    return get<4>(a) < get<4>(b);
  }
};

struct move_change_comp{
    bool operator()(const MoveChange a,const MoveChange b){
        return (a.first<b.first && a.second<b.second);
    }
};

map<MoveChange,double,move_change_comp> get_maph(){
map<MoveChange,double,move_change_comp>  maph;

//No push
//continue (forward)
maph[std::make_pair('l','l')] = fA;
maph[std::make_pair('r','r')] = fA;
maph[std::make_pair('u','u')] = fA;
maph[std::make_pair('d','d')] = fA;
//reverse (back)
maph[std::make_pair('l','r')] = bA;
maph[std::make_pair('r','l')] = bA;
maph[std::make_pair('u','d')] = bA;
maph[std::make_pair('d','u')] = bA;
//direction change (turn)
maph[std::make_pair('l','u')] = rA;
maph[std::make_pair('l','d')] = lA;
maph[std::make_pair('r','u')] = lA;
maph[std::make_pair('r','d')] = rA;
maph[std::make_pair('u','l')] = lA;
maph[std::make_pair('u','r')] = rA;
maph[std::make_pair('d','l')] = rA;
maph[std::make_pair('d','r')] = lA;
//With push
//continue push
maph[std::make_pair('L','L')] = fA;
maph[std::make_pair('R','R')] = fA;
maph[std::make_pair('U','U')] = fA;
maph[std::make_pair('D','D')] = fA;
maph[std::make_pair('l','L')] = fpA;
maph[std::make_pair('r','R')] = fpA;
maph[std::make_pair('u','U')] = fpA;
maph[std::make_pair('d','D')] = fpA;
//direction change (turn push)
maph[std::make_pair('l','U')] = rpA;
maph[std::make_pair('l','D')] = lpA;
maph[std::make_pair('r','U')] = lpA;
maph[std::make_pair('r','D')] = rpA;
maph[std::make_pair('u','L')] = lpA;
maph[std::make_pair('u','R')] = rpA;
maph[std::make_pair('d','L')] = rpA;
maph[std::make_pair('d','R')] = lpA;
//reverse (back push)
maph[std::make_pair('L','r')] = bA;
maph[std::make_pair('R','l')] = bA;
maph[std::make_pair('U','d')] = bA;
maph[std::make_pair('D','u')] = bA;
//turn
maph[std::make_pair('L','u')] = rA;
maph[std::make_pair('L','d')] = lA;
maph[std::make_pair('R','u')] = lA;
maph[std::make_pair('R','d')] = rA;
maph[std::make_pair('U','l')] = lA;
maph[std::make_pair('U','r')] = rA;
maph[std::make_pair('D','l')] = rA;
maph[std::make_pair('D','r')] = lA;
// turn push
maph[std::make_pair('L','U')] = rpA;
maph[std::make_pair('L','D')] = lpA;
maph[std::make_pair('R','U')] = lpA;
maph[std::make_pair('R','D')] = rpA;
maph[std::make_pair('U','L')] = lpA;
maph[std::make_pair('U','R')] = rpA;
maph[std::make_pair('D','L')] = rpA;
maph[std::make_pair('D','R')] = lpA;

return maph;
}
