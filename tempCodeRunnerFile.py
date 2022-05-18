
if forecast_function_coefficients[0][0] < 0:
    line_color = 'red'
elif forecast_function_coefficients[0][0] == 0:
    line_color = 'blue'
else:
    line_color = 'green'

plt.figure(figsize=[10, 7])
ax = plt.axes()

ax.plot(full_data['date'].head(24), full_data['price'].head(24), color='#277abe', linewidth=2)
ax.plot(full_data['date'].tail(5), full_data['price'].tail(5),
        color=line_color, linestyle='dashed', linewidth=3)

plt.xlabel('Date')
plt.ylabel("USD$ Price")
plt.title(plot_title)
plt.fill_between(full_data['date'], full_data['price'], min(full_data['price']), alpha=.15)

ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
ax.yaxis.set_major_formatter(tck.FormatStrFormatter('%.f$'))

plt.show()

