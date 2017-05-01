segment_width = 3.175;
max_amplitude = 152.4;
//min_amplitude = 65.1;
min_amplitude = 70.1;

module segment(height=19.05,width=3.175,pos_amp=65.1,neg_amp=65.1,diameter=184.15,cut_height=84.15){
    difference(){
        translate([0,-neg_amp,0]) cube([width,pos_amp+neg_amp,height]);
        translate([0,pos_amp,cut_height])rotate([0,90,0]) cylinder(d=diameter,h=width);
        translate([0,-neg_amp,cut_height])rotate([0,90,0]) cylinder(d=diameter,h=width);
    };
};




