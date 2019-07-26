/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

// See https://docusaurus.io/docs/site-config for all the possible
// site configuration options.

const siteConfig = {
    title: 'django-training', // Title for your website.
    tagline: 'Master the Django ORM for fun and profit',
    url: 'https://tophat.github.io', // Your website URL
    baseUrl: '/django-training/', // Base URL for your project */
    // For github.io type URLs, you would set the url and baseUrl like:
    //   url: 'https://facebook.github.io',
    //   baseUrl: '/test-site/',

    // Used for publishing and more
    projectName: 'django-training',
    organizationName: 'tophat',
    // For top-level user or org sites, the organization is still the same.
    // e.g., for the https://JoelMarcey.github.io site, it would be set like...
    //   organizationName: 'JoelMarcey'

    // For no header links in the top nav bar -> headerLinks: [],
    headerLinks: [
        { doc: 'overview', label: 'Docs' },
        {
            href: 'https://github.com/tophat/django-training',
            label: 'GitHub',
        },
    ],

    /* path to images for header/footer */
    headerIcon: 'img/django-training.svg',
    footerIcon: 'img/django-training.svg',
    favicon: 'img/django-training.svg',

    /* Colors for website */
    colors: {
        primaryColor: '#3471c5',
        secondaryColor: '#f9316d',
    },

    // This copyright info is used in /core/Footer.js and blog RSS/Atom feeds.
    copyright: `Copyright © ${new Date().getFullYear()} Top Hat Monocle Corp.`,

    highlight: {
        // Highlight.js theme to use for syntax highlighting in code blocks.
        theme: 'default',
    },

    // Add custom scripts here that would be placed in <script> tags.
    scripts: ['https://buttons.github.io/buttons.js'],

    // On page navigation for the current documentation page.
    onPageNav: 'separate',
    // No .html extensions for paths.
    cleanUrl: true,

    // Open Graph and Twitter card images.
    ogImage: 'img/django-training.svg',
    twitterImage: 'img/django-training.svg',

    // Show documentation's last contributor's name.
    enableUpdateBy: true,

    // Show documentation's last update time.
    enableUpdateTime: true,

    // You may provide arbitrary config keys to be used as needed by your
    // template. For example, if you need your repo's URL...
    //   repoUrl: 'https://github.com/facebook/test-site',
}

module.exports = siteConfig
