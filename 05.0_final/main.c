#include "GBA_main.h"
#include <string.h>     // needed to memcpy()

// I suck to manage render through frames (it should be at 30 fps but is at 60 laggy fps)

#include "bad_apple.h"

#define black       CLR_BLACK
#define white       CLR_WHITE
#define blackID     0
#define whiteID     1
#define maxpos      SCREEN_PIXELS
//#define maxpos      214*160

inline u8* getNext(u8*);

inline void slowPlotFrame(u8*, COLOR*);

int main(){
    pal_bg_mem[blackID] = black;
    pal_bg_mem[whiteID] = white;

    //REG_DISPCNT = DCNT_MODE3 | DCNT_BG2;
    REG_DISPCNT = DCNT_MODE4 | DCNT_BG2;

    COLOR fill = blackID;
    u8* currFrame = bad, nextFrame;
    while(1){
        VID_VSYNC;
        slowPlotFrame(currFrame, &fill);
        currFrame = getNext(currFrame);
        VID_FLIP;
    }

    return 0;
}

inline u8* getNext(u8* istr){
    u8* next = istr;
    while((*(next++)) != 254);
    return next;
}

inline void slowPlotFrame(u8* curr, COLOR* clrID){
    if((*curr) == 255) return; // is dead_frame
    u8* istr = curr;
    int pos = 0, tar;
    while((*istr) < 254){
        if(istr){
            if((*istr) < 248){
                tar = pos+(*istr);
            }else{
                tar = pos+(240<<((*istr)-247));
            }
            m4_fast_scanline(pos, tar, *clrID);
            pos = tar;
        }
        *clrID = !(*clrID);
        istr++;
    }
    if(*istr==254)
        m4_fast_scanline(pos, maxpos, *clrID);
}