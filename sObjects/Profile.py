class Profile:

    def __init__(self, Id=None, Name=None, PermissionsEmailSingle=None, PermissionsEmailMass=None, PermissionsEditTask=None, PermissionsEditEvent=None, PermissionsExportReport=None, PermissionsImportPersonal=None, PermissionsDataExport=None, PermissionsManageUsers=None, PermissionsEditPublicFilters=None, PermissionsEditPublicTemplates=None, PermissionsModifyAllData=None, PermissionsManageCases=None, PermissionsMassInlineEdit=None, PermissionsEditKnowledge=None, PermissionsManageKnowledge=None, PermissionsManageSolutions=None, PermissionsCustomizeApplication=None, PermissionsEditReadonlyFields=None, PermissionsRunReports=None, PermissionsViewSetup=None, PermissionsTransferAnyEntity=None, PermissionsNewReportBuilder=None, PermissionsActivateContract=None, PermissionsActivateOrder=None, PermissionsImportLeads=None, PermissionsManageLeads=None, PermissionsTransferAnyLead=None, PermissionsViewAllData=None, PermissionsEditPublicDocuments=None, PermissionsViewEncryptedData=None, PermissionsEditBrandTemplates=None, PermissionsEditHtmlTemplates=None, PermissionsChatterInternalUser=None, PermissionsManageTranslation=None, PermissionsManageEncryptionKeys=None, PermissionsDeleteActivatedContract=None, PermissionsChatterInviteExternalUsers=None, PermissionsSendSitRequests=None, PermissionsManageRemoteAccess=None, PermissionsCanUseNewDashboardBuilder=None, PermissionsManageCategories=None, PermissionsConvertLeads=None, PermissionsPasswordNeverExpires=None, PermissionsUseTeamReassignWizards=None, PermissionsEditActivatedOrders=None, PermissionsInstallMultiforce=None, PermissionsPublishMultiforce=None, PermissionsChatterOwnGroups=None, PermissionsEditOppLineItemUnitPrice=None, PermissionsCreateMultiforce=None, PermissionsBulkApiHardDelete=None, PermissionsSolutionImport=None, PermissionsManageCallCenters=None, PermissionsManageSynonyms=None, PermissionsViewContent=None, PermissionsManageEmailClientConfig=None, PermissionsEnableNotifications=None, PermissionsManageDataIntegrations=None, PermissionsDistributeFromPersWksp=None, PermissionsViewDataCategories=None, PermissionsManageDataCategories=None, PermissionsAuthorApex=None, PermissionsManageMobile=None, PermissionsApiEnabled=None, PermissionsManageCustomReportTypes=None, PermissionsEditCaseComments=None, PermissionsTransferAnyCase=None, PermissionsContentAdministrator=None, PermissionsCreateWorkspaces=None, PermissionsManageContentPermissions=None, PermissionsManageContentProperties=None, PermissionsManageContentTypes=None, PermissionsManageExchangeConfig=None, PermissionsManageAnalyticSnapshots=None, PermissionsScheduleReports=None, PermissionsManageBusinessHourHolidays=None, PermissionsManageEntitlements=None, PermissionsManageDynamicDashboards=None, PermissionsCustomSidebarOnAllPages=None, PermissionsManageInteraction=None, PermissionsViewMyTeamsDashboards=None, PermissionsModerateChatter=None, PermissionsResetPasswords=None, PermissionsFlowUFLRequired=None, PermissionsCanInsertFeedSystemFields=None, PermissionsActivitiesAccess=None, PermissionsManageKnowledgeImportExport=None, PermissionsEmailTemplateManagement=None, PermissionsEmailAdministration=None, PermissionsManageChatterMessages=None, PermissionsAllowEmailIC=None, PermissionsChatterFileLink=None, PermissionsForceTwoFactor=None, PermissionsViewEventLogFiles=None, PermissionsManageNetworks=None, PermissionsManageAuthProviders=None, PermissionsRunFlow=None, PermissionsCreateCustomizeDashboards=None, PermissionsCreateDashboardFolders=None, PermissionsViewPublicDashboards=None, PermissionsManageDashbdsInPubFolders=None, PermissionsCreateCustomizeReports=None, PermissionsCreateReportFolders=None, PermissionsViewPublicReports=None, PermissionsManageReportsInPubFolders=None, PermissionsEditMyDashboards=None, PermissionsEditMyReports=None, PermissionsViewAllUsers=None, PermissionsAllowUniversalSearch=None, PermissionsConnectOrgToEnvironmentHub=None, PermissionsWorkCalibrationUser=None, PermissionsCreateCustomizeFilters=None, PermissionsWorkDotComUserPerm=None, PermissionsContentHubUser=None, PermissionsGovernNetworks=None, PermissionsSalesConsole=None, PermissionsTwoFactorApi=None, PermissionsDeleteTopics=None, PermissionsEditTopics=None, PermissionsCreateTopics=None, PermissionsAssignTopics=None, PermissionsIdentityEnabled=None, PermissionsIdentityConnect=None, PermissionsAllowViewKnowledge=None, PermissionsContentWorkspaces=None, PermissionsCreateWorkBadgeDefinition=None, PermissionsManageSearchPromotionRules=None, PermissionsCustomMobileAppsAccess=None, PermissionsViewHelpLink=None, PermissionsManageProfilesPermissionsets=None, PermissionsAssignPermissionSets=None, PermissionsManageRoles=None, PermissionsManageIpAddresses=None, PermissionsManageSharing=None, PermissionsManageInternalUsers=None, PermissionsManagePasswordPolicies=None, PermissionsManageLoginAccessPolicies=None, PermissionsViewPlatformEvents=None, PermissionsManageCustomPermissions=None, PermissionsCanVerifyComment=None, PermissionsManageUnlistedGroups=None, PermissionsStdAutomaticActivityCapture=None, PermissionsInsightsAppDashboardEditor=None, PermissionsManageTwoFactor=None, PermissionsInsightsAppUser=None, PermissionsInsightsAppAdmin=None, PermissionsInsightsAppEltEditor=None, PermissionsInsightsAppUploadUser=None, PermissionsInsightsCreateApplication=None, PermissionsLightningExperienceUser=None, PermissionsViewDataLeakageEvents=None, PermissionsConfigCustomRecs=None, PermissionsSubmitMacrosAllowed=None, PermissionsBulkMacrosAllowed=None, PermissionsShareInternalArticles=None, PermissionsManageSessionPermissionSets=None, PermissionsManageTemplatedApp=None, PermissionsUseTemplatedApp=None, PermissionsSendAnnouncementEmails=None, PermissionsChatterEditOwnPost=None, PermissionsChatterEditOwnRecordPost=None, PermissionsWaveTabularDownload=None, PermissionsAutomaticActivityCapture=None, PermissionsImportCustomObjects=None, PermissionsDelegatedTwoFactor=None, PermissionsChatterComposeUiCodesnippet=None, PermissionsSelectFilesFromSalesforce=None, PermissionsModerateNetworkUsers=None, PermissionsMergeTopics=None, PermissionsSubscribeToLightningReports=None, PermissionsManagePvtRptsAndDashbds=None, PermissionsAllowLightningLogin=None, PermissionsCampaignInfluence2=None, PermissionsViewDataAssessment=None, PermissionsRemoveDirectMessageMembers=None, PermissionsCanApproveFeedPost=None, PermissionsAddDirectMessageMembers=None, PermissionsAllowViewEditConvertedLeads=None, PermissionsShowCompanyNameAsUserBadge=None, PermissionsAccessCMC=None, PermissionsViewHealthCheck=None, PermissionsManageHealthCheck=None, PermissionsPackaging2=None, PermissionsManageCertificates=None, PermissionsCreateReportInLightning=None, PermissionsPreventClassicExperience=None, PermissionsHideReadByList=None, PermissionsListEmailSend=None, PermissionsFeedPinning=None, PermissionsChangeDashboardColors=None, PermissionsIotUser=None, PermissionsManageRecommendationStrategies=None, PermissionsManagePropositions=None, PermissionsCloseConversations=None, PermissionsSubscribeReportRolesGrps=None, PermissionsSubscribeDashboardRolesGrps=None, PermissionsUseWebLink=None, PermissionsHasUnlimitedNBAExecutions=None, PermissionsViewOnlyEmbeddedAppUser=None, PermissionsViewAllActivities=None, PermissionsSubscribeReportToOtherUsers=None, PermissionsLightningConsoleAllowedForUser=None, PermissionsSubscribeReportsRunAsUser=None, PermissionsSubscribeToLightningDashboards=None, PermissionsSubscribeDashboardToOtherUsers=None, PermissionsCreateLtngTempInPub=None, PermissionsTransactionalEmailSend=None, PermissionsViewPrivateStaticResources=None, PermissionsCreateLtngTempFolder=None, PermissionsApexRestServices=None, PermissionsEnableCommunityAppLauncher=None, PermissionsGiveRecognitionBadge=None, PermissionsLtngPromoReserved01UserPerm=None, PermissionsManageSubscriptions=None, PermissionsWaveManagePrivateAssetsUser=None, PermissionsCanEditDataPrepRecipe=None, PermissionsAddAnalyticsRemoteConnections=None, PermissionsManageSurveys=None, PermissionsViewRoles=None, PermissionsCanManageMaps=None, PermissionsLMOutboundMessagingUserPerm=None, PermissionsModifyDataClassification=None, PermissionsPrivacyDataAccess=None, PermissionsQueryAllFiles=None, PermissionsModifyMetadata=None, PermissionsManageCMS=None, PermissionsSandboxTestingInCommunityApp=None, PermissionsCanEditPrompts=None, PermissionsViewUserPII=None, PermissionsManageHubConnections=None, PermissionsB2BMarketingAnalyticsUser=None, PermissionsTraceXdsQueries=None, PermissionsViewSecurityCommandCenter=None, PermissionsManageSecurityCommandCenter=None, PermissionsViewAllCustomSettings=None, PermissionsViewAllForeignKeyNames=None, PermissionsAddWaveNotificationRecipients=None, PermissionsHeadlessCMSAccess=None, PermissionsLMEndMessagingSessionUserPerm=None, PermissionsConsentApiUpdate=None, PermissionsPaymentsAPIUser=None, PermissionsAccessContentBuilder=None, PermissionsAccountSwitcherUser=None, PermissionsViewAnomalyEvents=None, PermissionsManageC360AConnections=None, PermissionsManageReleaseUpdates=None, PermissionsViewAllProfiles=None, PermissionsSkipIdentityConfirmation=None, PermissionsLearningManager=None, PermissionsSendCustomNotifications=None, PermissionsPackaging2Delete=None, PermissionsUseOmnichannelInventoryAPIs=None, PermissionsViewRestrictionAndScopingRules=None, PermissionsFSCComprehensiveUserAccess=None, PermissionsBotManageBots=None, PermissionsBotManageBotsTrainingData=None, PermissionsOmnichannelInventorySync=None, PermissionsManageLearningReporting=None, PermissionsIsotopeCToCUser=None, PermissionsIsotopeAccess=None, PermissionsIsotopeLEX=None, PermissionsQuipMetricsAccess=None, PermissionsQuipUserEngagementMetrics=None, PermissionsManageExternalConnections=None, PermissionsUseSubscriptionEmails=None, PermissionsAIViewInsightObjects=None, PermissionsAICreateInsightObjects=None, PermissionsLifecycleManagementAPIUser=None, PermissionsNativeWebviewScrolling=None, UserLicenseId=None, UserType=None, CreatedDate=None, CreatedById=None, LastModifiedDate=None, LastModifiedById=None, SystemModstamp=None, Description=None, LastViewedDate=None, LastReferencedDate=None):
        self.Id = Id
        self.Name = Name
        self.PermissionsEmailSingle = PermissionsEmailSingle
        self.PermissionsEmailMass = PermissionsEmailMass
        self.PermissionsEditTask = PermissionsEditTask
        self.PermissionsEditEvent = PermissionsEditEvent
        self.PermissionsExportReport = PermissionsExportReport
        self.PermissionsImportPersonal = PermissionsImportPersonal
        self.PermissionsDataExport = PermissionsDataExport
        self.PermissionsManageUsers = PermissionsManageUsers
        self.PermissionsEditPublicFilters = PermissionsEditPublicFilters
        self.PermissionsEditPublicTemplates = PermissionsEditPublicTemplates
        self.PermissionsModifyAllData = PermissionsModifyAllData
        self.PermissionsManageCases = PermissionsManageCases
        self.PermissionsMassInlineEdit = PermissionsMassInlineEdit
        self.PermissionsEditKnowledge = PermissionsEditKnowledge
        self.PermissionsManageKnowledge = PermissionsManageKnowledge
        self.PermissionsManageSolutions = PermissionsManageSolutions
        self.PermissionsCustomizeApplication = PermissionsCustomizeApplication
        self.PermissionsEditReadonlyFields = PermissionsEditReadonlyFields
        self.PermissionsRunReports = PermissionsRunReports
        self.PermissionsViewSetup = PermissionsViewSetup
        self.PermissionsTransferAnyEntity = PermissionsTransferAnyEntity
        self.PermissionsNewReportBuilder = PermissionsNewReportBuilder
        self.PermissionsActivateContract = PermissionsActivateContract
        self.PermissionsActivateOrder = PermissionsActivateOrder
        self.PermissionsImportLeads = PermissionsImportLeads
        self.PermissionsManageLeads = PermissionsManageLeads
        self.PermissionsTransferAnyLead = PermissionsTransferAnyLead
        self.PermissionsViewAllData = PermissionsViewAllData
        self.PermissionsEditPublicDocuments = PermissionsEditPublicDocuments
        self.PermissionsViewEncryptedData = PermissionsViewEncryptedData
        self.PermissionsEditBrandTemplates = PermissionsEditBrandTemplates
        self.PermissionsEditHtmlTemplates = PermissionsEditHtmlTemplates
        self.PermissionsChatterInternalUser = PermissionsChatterInternalUser
        self.PermissionsManageTranslation = PermissionsManageTranslation
        self.PermissionsManageEncryptionKeys = PermissionsManageEncryptionKeys
        self.PermissionsDeleteActivatedContract = PermissionsDeleteActivatedContract
        self.PermissionsChatterInviteExternalUsers = PermissionsChatterInviteExternalUsers
        self.PermissionsSendSitRequests = PermissionsSendSitRequests
        self.PermissionsManageRemoteAccess = PermissionsManageRemoteAccess
        self.PermissionsCanUseNewDashboardBuilder = PermissionsCanUseNewDashboardBuilder
        self.PermissionsManageCategories = PermissionsManageCategories
        self.PermissionsConvertLeads = PermissionsConvertLeads
        self.PermissionsPasswordNeverExpires = PermissionsPasswordNeverExpires
        self.PermissionsUseTeamReassignWizards = PermissionsUseTeamReassignWizards
        self.PermissionsEditActivatedOrders = PermissionsEditActivatedOrders
        self.PermissionsInstallMultiforce = PermissionsInstallMultiforce
        self.PermissionsPublishMultiforce = PermissionsPublishMultiforce
        self.PermissionsChatterOwnGroups = PermissionsChatterOwnGroups
        self.PermissionsEditOppLineItemUnitPrice = PermissionsEditOppLineItemUnitPrice
        self.PermissionsCreateMultiforce = PermissionsCreateMultiforce
        self.PermissionsBulkApiHardDelete = PermissionsBulkApiHardDelete
        self.PermissionsSolutionImport = PermissionsSolutionImport
        self.PermissionsManageCallCenters = PermissionsManageCallCenters
        self.PermissionsManageSynonyms = PermissionsManageSynonyms
        self.PermissionsViewContent = PermissionsViewContent
        self.PermissionsManageEmailClientConfig = PermissionsManageEmailClientConfig
        self.PermissionsEnableNotifications = PermissionsEnableNotifications
        self.PermissionsManageDataIntegrations = PermissionsManageDataIntegrations
        self.PermissionsDistributeFromPersWksp = PermissionsDistributeFromPersWksp
        self.PermissionsViewDataCategories = PermissionsViewDataCategories
        self.PermissionsManageDataCategories = PermissionsManageDataCategories
        self.PermissionsAuthorApex = PermissionsAuthorApex
        self.PermissionsManageMobile = PermissionsManageMobile
        self.PermissionsApiEnabled = PermissionsApiEnabled
        self.PermissionsManageCustomReportTypes = PermissionsManageCustomReportTypes
        self.PermissionsEditCaseComments = PermissionsEditCaseComments
        self.PermissionsTransferAnyCase = PermissionsTransferAnyCase
        self.PermissionsContentAdministrator = PermissionsContentAdministrator
        self.PermissionsCreateWorkspaces = PermissionsCreateWorkspaces
        self.PermissionsManageContentPermissions = PermissionsManageContentPermissions
        self.PermissionsManageContentProperties = PermissionsManageContentProperties
        self.PermissionsManageContentTypes = PermissionsManageContentTypes
        self.PermissionsManageExchangeConfig = PermissionsManageExchangeConfig
        self.PermissionsManageAnalyticSnapshots = PermissionsManageAnalyticSnapshots
        self.PermissionsScheduleReports = PermissionsScheduleReports
        self.PermissionsManageBusinessHourHolidays = PermissionsManageBusinessHourHolidays
        self.PermissionsManageEntitlements = PermissionsManageEntitlements
        self.PermissionsManageDynamicDashboards = PermissionsManageDynamicDashboards
        self.PermissionsCustomSidebarOnAllPages = PermissionsCustomSidebarOnAllPages
        self.PermissionsManageInteraction = PermissionsManageInteraction
        self.PermissionsViewMyTeamsDashboards = PermissionsViewMyTeamsDashboards
        self.PermissionsModerateChatter = PermissionsModerateChatter
        self.PermissionsResetPasswords = PermissionsResetPasswords
        self.PermissionsFlowUFLRequired = PermissionsFlowUFLRequired
        self.PermissionsCanInsertFeedSystemFields = PermissionsCanInsertFeedSystemFields
        self.PermissionsActivitiesAccess = PermissionsActivitiesAccess
        self.PermissionsManageKnowledgeImportExport = PermissionsManageKnowledgeImportExport
        self.PermissionsEmailTemplateManagement = PermissionsEmailTemplateManagement
        self.PermissionsEmailAdministration = PermissionsEmailAdministration
        self.PermissionsManageChatterMessages = PermissionsManageChatterMessages
        self.PermissionsAllowEmailIC = PermissionsAllowEmailIC
        self.PermissionsChatterFileLink = PermissionsChatterFileLink
        self.PermissionsForceTwoFactor = PermissionsForceTwoFactor
        self.PermissionsViewEventLogFiles = PermissionsViewEventLogFiles
        self.PermissionsManageNetworks = PermissionsManageNetworks
        self.PermissionsManageAuthProviders = PermissionsManageAuthProviders
        self.PermissionsRunFlow = PermissionsRunFlow
        self.PermissionsCreateCustomizeDashboards = PermissionsCreateCustomizeDashboards
        self.PermissionsCreateDashboardFolders = PermissionsCreateDashboardFolders
        self.PermissionsViewPublicDashboards = PermissionsViewPublicDashboards
        self.PermissionsManageDashbdsInPubFolders = PermissionsManageDashbdsInPubFolders
        self.PermissionsCreateCustomizeReports = PermissionsCreateCustomizeReports
        self.PermissionsCreateReportFolders = PermissionsCreateReportFolders
        self.PermissionsViewPublicReports = PermissionsViewPublicReports
        self.PermissionsManageReportsInPubFolders = PermissionsManageReportsInPubFolders
        self.PermissionsEditMyDashboards = PermissionsEditMyDashboards
        self.PermissionsEditMyReports = PermissionsEditMyReports
        self.PermissionsViewAllUsers = PermissionsViewAllUsers
        self.PermissionsAllowUniversalSearch = PermissionsAllowUniversalSearch
        self.PermissionsConnectOrgToEnvironmentHub = PermissionsConnectOrgToEnvironmentHub
        self.PermissionsWorkCalibrationUser = PermissionsWorkCalibrationUser
        self.PermissionsCreateCustomizeFilters = PermissionsCreateCustomizeFilters
        self.PermissionsWorkDotComUserPerm = PermissionsWorkDotComUserPerm
        self.PermissionsContentHubUser = PermissionsContentHubUser
        self.PermissionsGovernNetworks = PermissionsGovernNetworks
        self.PermissionsSalesConsole = PermissionsSalesConsole
        self.PermissionsTwoFactorApi = PermissionsTwoFactorApi
        self.PermissionsDeleteTopics = PermissionsDeleteTopics
        self.PermissionsEditTopics = PermissionsEditTopics
        self.PermissionsCreateTopics = PermissionsCreateTopics
        self.PermissionsAssignTopics = PermissionsAssignTopics
        self.PermissionsIdentityEnabled = PermissionsIdentityEnabled
        self.PermissionsIdentityConnect = PermissionsIdentityConnect
        self.PermissionsAllowViewKnowledge = PermissionsAllowViewKnowledge
        self.PermissionsContentWorkspaces = PermissionsContentWorkspaces
        self.PermissionsCreateWorkBadgeDefinition = PermissionsCreateWorkBadgeDefinition
        self.PermissionsManageSearchPromotionRules = PermissionsManageSearchPromotionRules
        self.PermissionsCustomMobileAppsAccess = PermissionsCustomMobileAppsAccess
        self.PermissionsViewHelpLink = PermissionsViewHelpLink
        self.PermissionsManageProfilesPermissionsets = PermissionsManageProfilesPermissionsets
        self.PermissionsAssignPermissionSets = PermissionsAssignPermissionSets
        self.PermissionsManageRoles = PermissionsManageRoles
        self.PermissionsManageIpAddresses = PermissionsManageIpAddresses
        self.PermissionsManageSharing = PermissionsManageSharing
        self.PermissionsManageInternalUsers = PermissionsManageInternalUsers
        self.PermissionsManagePasswordPolicies = PermissionsManagePasswordPolicies
        self.PermissionsManageLoginAccessPolicies = PermissionsManageLoginAccessPolicies
        self.PermissionsViewPlatformEvents = PermissionsViewPlatformEvents
        self.PermissionsManageCustomPermissions = PermissionsManageCustomPermissions
        self.PermissionsCanVerifyComment = PermissionsCanVerifyComment
        self.PermissionsManageUnlistedGroups = PermissionsManageUnlistedGroups
        self.PermissionsStdAutomaticActivityCapture = PermissionsStdAutomaticActivityCapture
        self.PermissionsInsightsAppDashboardEditor = PermissionsInsightsAppDashboardEditor
        self.PermissionsManageTwoFactor = PermissionsManageTwoFactor
        self.PermissionsInsightsAppUser = PermissionsInsightsAppUser
        self.PermissionsInsightsAppAdmin = PermissionsInsightsAppAdmin
        self.PermissionsInsightsAppEltEditor = PermissionsInsightsAppEltEditor
        self.PermissionsInsightsAppUploadUser = PermissionsInsightsAppUploadUser
        self.PermissionsInsightsCreateApplication = PermissionsInsightsCreateApplication
        self.PermissionsLightningExperienceUser = PermissionsLightningExperienceUser
        self.PermissionsViewDataLeakageEvents = PermissionsViewDataLeakageEvents
        self.PermissionsConfigCustomRecs = PermissionsConfigCustomRecs
        self.PermissionsSubmitMacrosAllowed = PermissionsSubmitMacrosAllowed
        self.PermissionsBulkMacrosAllowed = PermissionsBulkMacrosAllowed
        self.PermissionsShareInternalArticles = PermissionsShareInternalArticles
        self.PermissionsManageSessionPermissionSets = PermissionsManageSessionPermissionSets
        self.PermissionsManageTemplatedApp = PermissionsManageTemplatedApp
        self.PermissionsUseTemplatedApp = PermissionsUseTemplatedApp
        self.PermissionsSendAnnouncementEmails = PermissionsSendAnnouncementEmails
        self.PermissionsChatterEditOwnPost = PermissionsChatterEditOwnPost
        self.PermissionsChatterEditOwnRecordPost = PermissionsChatterEditOwnRecordPost
        self.PermissionsWaveTabularDownload = PermissionsWaveTabularDownload
        self.PermissionsAutomaticActivityCapture = PermissionsAutomaticActivityCapture
        self.PermissionsImportCustomObjects = PermissionsImportCustomObjects
        self.PermissionsDelegatedTwoFactor = PermissionsDelegatedTwoFactor
        self.PermissionsChatterComposeUiCodesnippet = PermissionsChatterComposeUiCodesnippet
        self.PermissionsSelectFilesFromSalesforce = PermissionsSelectFilesFromSalesforce
        self.PermissionsModerateNetworkUsers = PermissionsModerateNetworkUsers
        self.PermissionsMergeTopics = PermissionsMergeTopics
        self.PermissionsSubscribeToLightningReports = PermissionsSubscribeToLightningReports
        self.PermissionsManagePvtRptsAndDashbds = PermissionsManagePvtRptsAndDashbds
        self.PermissionsAllowLightningLogin = PermissionsAllowLightningLogin
        self.PermissionsCampaignInfluence2 = PermissionsCampaignInfluence2
        self.PermissionsViewDataAssessment = PermissionsViewDataAssessment
        self.PermissionsRemoveDirectMessageMembers = PermissionsRemoveDirectMessageMembers
        self.PermissionsCanApproveFeedPost = PermissionsCanApproveFeedPost
        self.PermissionsAddDirectMessageMembers = PermissionsAddDirectMessageMembers
        self.PermissionsAllowViewEditConvertedLeads = PermissionsAllowViewEditConvertedLeads
        self.PermissionsShowCompanyNameAsUserBadge = PermissionsShowCompanyNameAsUserBadge
        self.PermissionsAccessCMC = PermissionsAccessCMC
        self.PermissionsViewHealthCheck = PermissionsViewHealthCheck
        self.PermissionsManageHealthCheck = PermissionsManageHealthCheck
        self.PermissionsPackaging2 = PermissionsPackaging2
        self.PermissionsManageCertificates = PermissionsManageCertificates
        self.PermissionsCreateReportInLightning = PermissionsCreateReportInLightning
        self.PermissionsPreventClassicExperience = PermissionsPreventClassicExperience
        self.PermissionsHideReadByList = PermissionsHideReadByList
        self.PermissionsListEmailSend = PermissionsListEmailSend
        self.PermissionsFeedPinning = PermissionsFeedPinning
        self.PermissionsChangeDashboardColors = PermissionsChangeDashboardColors
        self.PermissionsIotUser = PermissionsIotUser
        self.PermissionsManageRecommendationStrategies = PermissionsManageRecommendationStrategies
        self.PermissionsManagePropositions = PermissionsManagePropositions
        self.PermissionsCloseConversations = PermissionsCloseConversations
        self.PermissionsSubscribeReportRolesGrps = PermissionsSubscribeReportRolesGrps
        self.PermissionsSubscribeDashboardRolesGrps = PermissionsSubscribeDashboardRolesGrps
        self.PermissionsUseWebLink = PermissionsUseWebLink
        self.PermissionsHasUnlimitedNBAExecutions = PermissionsHasUnlimitedNBAExecutions
        self.PermissionsViewOnlyEmbeddedAppUser = PermissionsViewOnlyEmbeddedAppUser
        self.PermissionsViewAllActivities = PermissionsViewAllActivities
        self.PermissionsSubscribeReportToOtherUsers = PermissionsSubscribeReportToOtherUsers
        self.PermissionsLightningConsoleAllowedForUser = PermissionsLightningConsoleAllowedForUser
        self.PermissionsSubscribeReportsRunAsUser = PermissionsSubscribeReportsRunAsUser
        self.PermissionsSubscribeToLightningDashboards = PermissionsSubscribeToLightningDashboards
        self.PermissionsSubscribeDashboardToOtherUsers = PermissionsSubscribeDashboardToOtherUsers
        self.PermissionsCreateLtngTempInPub = PermissionsCreateLtngTempInPub
        self.PermissionsTransactionalEmailSend = PermissionsTransactionalEmailSend
        self.PermissionsViewPrivateStaticResources = PermissionsViewPrivateStaticResources
        self.PermissionsCreateLtngTempFolder = PermissionsCreateLtngTempFolder
        self.PermissionsApexRestServices = PermissionsApexRestServices
        self.PermissionsEnableCommunityAppLauncher = PermissionsEnableCommunityAppLauncher
        self.PermissionsGiveRecognitionBadge = PermissionsGiveRecognitionBadge
        self.PermissionsLtngPromoReserved01UserPerm = PermissionsLtngPromoReserved01UserPerm
        self.PermissionsManageSubscriptions = PermissionsManageSubscriptions
        self.PermissionsWaveManagePrivateAssetsUser = PermissionsWaveManagePrivateAssetsUser
        self.PermissionsCanEditDataPrepRecipe = PermissionsCanEditDataPrepRecipe
        self.PermissionsAddAnalyticsRemoteConnections = PermissionsAddAnalyticsRemoteConnections
        self.PermissionsManageSurveys = PermissionsManageSurveys
        self.PermissionsViewRoles = PermissionsViewRoles
        self.PermissionsCanManageMaps = PermissionsCanManageMaps
        self.PermissionsLMOutboundMessagingUserPerm = PermissionsLMOutboundMessagingUserPerm
        self.PermissionsModifyDataClassification = PermissionsModifyDataClassification
        self.PermissionsPrivacyDataAccess = PermissionsPrivacyDataAccess
        self.PermissionsQueryAllFiles = PermissionsQueryAllFiles
        self.PermissionsModifyMetadata = PermissionsModifyMetadata
        self.PermissionsManageCMS = PermissionsManageCMS
        self.PermissionsSandboxTestingInCommunityApp = PermissionsSandboxTestingInCommunityApp
        self.PermissionsCanEditPrompts = PermissionsCanEditPrompts
        self.PermissionsViewUserPII = PermissionsViewUserPII
        self.PermissionsManageHubConnections = PermissionsManageHubConnections
        self.PermissionsB2BMarketingAnalyticsUser = PermissionsB2BMarketingAnalyticsUser
        self.PermissionsTraceXdsQueries = PermissionsTraceXdsQueries
        self.PermissionsViewSecurityCommandCenter = PermissionsViewSecurityCommandCenter
        self.PermissionsManageSecurityCommandCenter = PermissionsManageSecurityCommandCenter
        self.PermissionsViewAllCustomSettings = PermissionsViewAllCustomSettings
        self.PermissionsViewAllForeignKeyNames = PermissionsViewAllForeignKeyNames
        self.PermissionsAddWaveNotificationRecipients = PermissionsAddWaveNotificationRecipients
        self.PermissionsHeadlessCMSAccess = PermissionsHeadlessCMSAccess
        self.PermissionsLMEndMessagingSessionUserPerm = PermissionsLMEndMessagingSessionUserPerm
        self.PermissionsConsentApiUpdate = PermissionsConsentApiUpdate
        self.PermissionsPaymentsAPIUser = PermissionsPaymentsAPIUser
        self.PermissionsAccessContentBuilder = PermissionsAccessContentBuilder
        self.PermissionsAccountSwitcherUser = PermissionsAccountSwitcherUser
        self.PermissionsViewAnomalyEvents = PermissionsViewAnomalyEvents
        self.PermissionsManageC360AConnections = PermissionsManageC360AConnections
        self.PermissionsManageReleaseUpdates = PermissionsManageReleaseUpdates
        self.PermissionsViewAllProfiles = PermissionsViewAllProfiles
        self.PermissionsSkipIdentityConfirmation = PermissionsSkipIdentityConfirmation
        self.PermissionsLearningManager = PermissionsLearningManager
        self.PermissionsSendCustomNotifications = PermissionsSendCustomNotifications
        self.PermissionsPackaging2Delete = PermissionsPackaging2Delete
        self.PermissionsUseOmnichannelInventoryAPIs = PermissionsUseOmnichannelInventoryAPIs
        self.PermissionsViewRestrictionAndScopingRules = PermissionsViewRestrictionAndScopingRules
        self.PermissionsFSCComprehensiveUserAccess = PermissionsFSCComprehensiveUserAccess
        self.PermissionsBotManageBots = PermissionsBotManageBots
        self.PermissionsBotManageBotsTrainingData = PermissionsBotManageBotsTrainingData
        self.PermissionsOmnichannelInventorySync = PermissionsOmnichannelInventorySync
        self.PermissionsManageLearningReporting = PermissionsManageLearningReporting
        self.PermissionsIsotopeCToCUser = PermissionsIsotopeCToCUser
        self.PermissionsIsotopeAccess = PermissionsIsotopeAccess
        self.PermissionsIsotopeLEX = PermissionsIsotopeLEX
        self.PermissionsQuipMetricsAccess = PermissionsQuipMetricsAccess
        self.PermissionsQuipUserEngagementMetrics = PermissionsQuipUserEngagementMetrics
        self.PermissionsManageExternalConnections = PermissionsManageExternalConnections
        self.PermissionsUseSubscriptionEmails = PermissionsUseSubscriptionEmails
        self.PermissionsAIViewInsightObjects = PermissionsAIViewInsightObjects
        self.PermissionsAICreateInsightObjects = PermissionsAICreateInsightObjects
        self.PermissionsLifecycleManagementAPIUser = PermissionsLifecycleManagementAPIUser
        self.PermissionsNativeWebviewScrolling = PermissionsNativeWebviewScrolling
        self.UserLicenseId = UserLicenseId
        self.UserType = UserType
        self.CreatedDate = CreatedDate
        self.CreatedById = CreatedById
        self.LastModifiedDate = LastModifiedDate
        self.LastModifiedById = LastModifiedById
        self.SystemModstamp = SystemModstamp
        self.Description = Description
        self.LastViewedDate = LastViewedDate
        self.LastReferencedDate = LastReferencedDate


