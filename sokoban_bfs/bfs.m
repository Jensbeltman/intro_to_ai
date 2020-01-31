%%
clear 
clc

d1 = importdata('testing_breadth_fs.csv');
d2 = importdata('testing_best_fs.csv');


close all
[i,~,j]  = unique(d1(:,1), 'rows');

M1 = [i, accumarray(j, d1(:,2), [], @mean)];
O1 = [i, accumarray(j, d1(:,3), [], @mean)];
T1 = [i, accumarray(j, d1(:,4), [], @mean)];
Msd1 = [i, accumarray(j, d1(:,2), [], @std)];
Osd1 = [i, accumarray(j, d1(:,3), [], @std)];
Tsd1 = [i, accumarray(j, d1(:,4), [], @std)];


[i,~,j]  = unique(d2(:,1), 'rows');

M2 = [i, accumarray(j, d2(:,2), [], @mean)];
O2 = [i, accumarray(j, d2(:,3), [], @mean)];
T2 = [i, accumarray(j, d2(:,4), [], @mean)];
Msd2 = [i, accumarray(j, d2(:,2), [], @std)];
Osd2 = [i, accumarray(j, d2(:,3), [], @std)];
Tsd2 = [i, accumarray(j, d2(:,4), [], @std)];


xlims = [0.9 4.1];

VertSpace = 1.3;
PaddingBottom = 0.1;
ML = 0.07;

figure
subaxis(1,3,1,'PaddingBottom',PaddingBottom,'MR',0,'ML',ML)
hold on
plot(M1(:,1),M1(:,2))
plot(M2(:,1),M2(:,2))
hold off
title("# actions");
xlim(xlims);
xlabel("# cans");
ax = gca;
ax.YAxis.Exponent = 3;

subaxis(1,3,2,'PaddingBottom',PaddingBottom,'MR',0,'ML',ML)
hold on
plot(O1(:,1),O1(:,2))
plot(O2(:,1),O2(:,2))
hold off
title("open-list size");
xlabel("# cans");
xlim(xlims);
ax = gca;
ax.YAxis.Exponent = 3;
legend("BRFS","BEFS")

subaxis(1,3,3,'PaddingBottom',PaddingBottom,'MR',0,'ML',ML)
hold on
plot(T1(:,1),T1(:,2))
plot(T2(:,1),T2(:,2))
hold off
xlabel("# cans");
title("exec. time [s]");
xlim(xlims);



%%
close all
[i,~,j]  = unique(d(:,1), 'rows');

M = [i, accumarray(j, d(:,2), [], @mean)];
O = [i, accumarray(j, d(:,3), [], @mean)];
O2 = O;
T = [i, accumarray(j, d(:,4), [], @mean)];
Msd = [i, accumarray(j, d(:,2), [], @std)];
Osd = [i, accumarray(j, d(:,3), [], @std)];
Tsd = [i, accumarray(j, d(:,4), [], @std)];

xlims = [0.9 4.1];


figure
subplot(3,2,1)
plot(M(:,1),M(:,2))
ylabel("moves");
xlim(xlims);
title('Breadth Search First')

subplot(3,2,3)
plot(O(:,1),O(:,2))
ylabel("openlist size");
xlim(xlims);
ax = gca;
ax.YAxis.Exponent = 3;

subplot(3,2,5)
plot(T(:,1),T(:,2))
xlabel("# cans");
ylabel("exec. time [s]");
xlim(xlims);



d = importdata('testing_best_fs.csv');

[i,~,j]  = unique(d(:,1), 'rows');

M = [i, accumarray(j, d(:,2), [], @mean)];
O = [i, accumarray(j, d(:,3), [], @mean)];
T = [i, accumarray(j, d(:,4), [], @mean)];
Msd = [i, accumarray(j, d(:,2), [], @std)];
Osd = [i, accumarray(j, d(:,3), [], @std)];
Tsd = [i, accumarray(j, d(:,4), [], @std)];

xlims = [0.9 4.1];




subplot(3,2,2)
plot(M(:,1),M(:,2))
xlim(xlims);
title('Best Search First')
subplot(3,2,4)
plot(O(:,1),O(:,2))
xlim(xlims);
ax = gca;
ax.YAxis.Exponent = 3;

subplot(3,2,6)
plot(T(:,1),T(:,2))
xlabel("# cans");
xlim(xlims);
ylim([0 30])


% figure
% subplot(3,1,1)
% errorbar(M(:,1),M(:,2),Msd(:,2))
% xlabel("Cans");
% ylabel("moves");
% xlim(xlims);
% subplot(3,1,2)
% errorbar(O(:,1),O(:,2),Osd(:,2))
% xlabel("Cans");
% ylabel("openlist size");
% xlim(xlims);
% subplot(3,1,3)
% errorbar(T(:,1),T(:,2),Tsd(:,2))
% xlabel("Cans");
% ylabel("exec. time [s]");
% xlim(xlims);